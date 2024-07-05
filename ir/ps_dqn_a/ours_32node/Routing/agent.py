import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import random
import time
from collections import deque

class MA_PS_DQN(nn.Module):
    def __init__(self, num_agents, input_size, output_size,link_num):
        super(MA_PS_DQN, self).__init__()
        self.hidden_dim = 32
        self.hidden_dim_2 = 32
        self.hidden_dim_3 = 32
        self.encoder_h = 16
        self.attend_heads=1
        self.attend_dim= 16
        self.num_agents=num_agents

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.encoder = nn.Sequential(nn.Linear( link_num,self.encoder_h),nn.ReLU())
        self.multihead_attn = nn.MultiheadAttention(self.attend_dim, self.attend_heads,batch_first=True)

        self.feature_extraction = nn.Sequential(
            nn.Linear(input_size+self.attend_dim , self.hidden_dim ),
            nn.ReLU(),
            nn.Linear(self.hidden_dim , self.hidden_dim_2 ),
            nn.ReLU()
        )

        # Independent output layers for each agent
        self.q_values = nn.ModuleList([
            nn.Linear(self.hidden_dim_2, output_size) for _ in range(num_agents)
        ])

        for layer in self.feature_extraction:
            if isinstance(layer, nn.Linear):
                nn.init.kaiming_uniform_(layer.weight, mode='fan_in', nonlinearity='relu')
        for layer in self.encoder:
            if isinstance(layer, nn.Linear):
                nn.init.kaiming_uniform_(layer.weight, mode='fan_in', nonlinearity='relu')
        
    
    def cal_attention_v(self,path_vector,training=False):
        if not training:
            path_vector = [path_vector]
            path_vector_tensor = torch.tensor(path_vector, dtype=torch.float32).to(self.device)
        else:
            path_vector_tensor = torch.tensor(path_vector, dtype=torch.float32).to(self.device)

        e_path_vector_tensor = self.encoder(path_vector_tensor)
        attention_vector,_ = self.multihead_attn(e_path_vector_tensor,e_path_vector_tensor,e_path_vector_tensor)
        
        return attention_vector

    def forward(self, states,attention_vector, agent_idx):
        features_ = torch.cat((states,attention_vector), dim=-1)
        features = self.feature_extraction(features_)
        q_values = self.q_values[agent_idx](features)

        return q_values


class Agent:
    def __init__(self, num_agents_, state_dim, action_dim,link_num):
        self.lr = 0.01
        self.gamma = 0.9
        self.num_agents = num_agents_
        self.action_size = action_dim
        self.a1=1.0
        self.a2=0.0
        self.a3=0.0
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


        self.dqn_model = MA_PS_DQN(num_agents_,state_dim,action_dim,link_num).to(self.device)
        self.dqn_target = MA_PS_DQN(num_agents_,state_dim,action_dim,link_num).to(self.device)

        

        self.dqn_opt = optim.Adam(params=self._get_parameters(self.dqn_model),lr=self.lr)

        self.batch_size=32
        self.tau = 0.005
        self.memory = deque(maxlen=2000)   

    def _get_parameters(self, networks):
        params = []
        params += list(networks.parameters())
        return params

    def update_target(self):
        self.dqn_target.load_state_dict(self.dqn_model.state_dict())

    def get_action(self, state, agent_index,epsilon,attention_vector):
        state_tensor = torch.tensor(state, dtype=torch.float32).to(self.device)
        e_attention_vector = attention_vector.clone().unsqueeze(0)
        q_value = self.dqn_model(state_tensor,e_attention_vector,agent_index).detach()
        qval_ = q_value.cpu().data.numpy()
        if np.random.rand() <= epsilon:
            action = np.random.choice(self.action_size)
        else:
            action = np.argmax(qval_) 
        return action

    def append_sample(self, state, actions, next_state, reward,path_vector):
        self.memory.append((state, actions, next_state, reward,path_vector))


    
    def save_model(self, SIZE):
        k = 0
        torch.save(self.dqn_model, "model/dqn_model/model")
    
    def save_model_es(self, model):
        torch.save(model, "model/dqn_model/model")

    def load_model(self, SIZE):
        k = 0
        self.dqn_model = torch.load("model/dqn_model/model", map_location=self.device)
    
    def load_model_es(self, SIZE):
        k = 0
        self.dqn_model.load_state_dict(torch.load("model/dqn_model/model", map_location=self.device))
    
    def update(self):
        mini_batch = random.sample(self.memory, self.batch_size)
        states = torch.tensor([i[0] for i in mini_batch], dtype=torch.float32).to(self.device)
        actions = torch.tensor([i[1] for i in mini_batch], dtype=torch.float32).to(self.device)
        next_states = torch.tensor([i[2] for i in mini_batch], dtype=torch.float32).to(self.device)
        rewards = torch.tensor([i[3] for i in mini_batch], dtype=torch.float32).to(self.device)
        path_vector = [i[4] for i in mini_batch]

        attention_vector= self.dqn_model.cal_attention_v(path_vector,training=True)
        target_attention_vector= self.dqn_target.cal_attention_v(path_vector,training=True)

        dqn_loss_all = 0

        for i in range(self.num_agents):
            q_value = self.dqn_model(states,attention_vector[:,i,],i)
            main_q_value = q_value.gather(dim=1, index=actions[:, i].unsqueeze(-1).long()).squeeze()
            next_q_value = self.dqn_target(next_states,target_attention_vector[:,i,],i).detach()
            max_q_value, argmax_actions = torch.max(next_q_value, dim=1)
            target_q_values = rewards[:, i] + self.gamma * max_q_value
            dqn_loss = F.mse_loss(main_q_value,target_q_values)
            self.dqn_opt.zero_grad()
            dqn_loss.backward(retain_graph=True)
            self.dqn_opt.step()
            dqn_loss_all += dqn_loss.item()

        return dqn_loss_all
