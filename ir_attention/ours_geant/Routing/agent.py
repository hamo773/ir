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
        self.attend_heads = 1
        self.attend_dim= 16
        self.num_agents=num_agents

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.encoder = nn.Sequential(nn.Linear( link_num,self.encoder_h),
                                                       nn.ReLU())
        """self.key_extractors = nn.ModuleList()
        self.selector_extractors = nn.ModuleList()
        self.value_extractors = nn.ModuleList()

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        for i in range(self.attend_heads):
            #self.key_extractors.append(nn.Linear( self.encoder_h, self.attend_dim, bias=False))
            #self.selector_extractors.append(nn.Linear( self.encoder_h, self.attend_dim, bias=False))
            self.key_extractors.append(nn.Sequential(nn.Linear( self.encoder_h,
                                                                self.attend_dim),
                                                       nn.ReLU()))
            self.selector_extractors.append(nn.Sequential(nn.Linear( self.encoder_h,
                                                                self.attend_dim),
                                                       nn.ReLU()))
            self.value_extractors.append(nn.Sequential(nn.Linear( self.encoder_h,
                                                                self.attend_dim),
                                                       nn.LeakyReLU()))"""
        #self.multihead_attn = nn.MultiheadAttention(self.attend_dim, self.attend_heads,batch_first=True)
        self.multihead_attn = nn.MultiheadAttention(self.attend_dim, self.attend_heads,batch_first=True)
        """for i in range(self.attend_heads):
            self.key_extractors.append(nn.Linear( link_num, self.attend_dim, bias=False))
            self.selector_extractors.append(nn.Linear( link_num, self.attend_dim, bias=False))
            self.value_extractors.append(nn.Sequential(nn.Linear( link_num,
                                                                self.attend_dim),
                                                       nn.ReLU()))"""

        # Shared feature extraction layers
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
        """self.q_values = nn.ModuleList([
            nn.Sequential(
                nn.Linear(self.hidden_dim_2+self.attend_dim, self.hidden_dim_3),
                nn.ReLU(),
                nn.Linear(self.hidden_dim_3, output_size)
            ) for _ in range(num_agents)
        ])"""
    
    def cal_attention_v(self,path_vector,training=False):
        #time_in = time.time()
        if not training:
            path_vector = [path_vector]
            path_vector_tensor = torch.tensor(path_vector, dtype=torch.float32).to(self.device)
            #e_path_vector_tensor = self.encoder(path_vector_tensor)
            #query = torch.tensor(path_vector, dtype=torch.float32).detach().to(self.device)
            #key = torch.tensor(path_vector, dtype=torch.float32).detach().to(self.device)
            #value = torch.tensor(path_vector, dtype=torch.float32).detach().to(self.device)
            """query = e_path_vector_tensor.clone().detach().to(self.device)
            key = e_path_vector_tensor.clone().detach().to(self.device)
            value = e_path_vector_tensor.clone().detach().to(self.device)"""
        else:
            #print("aaaa")
            path_vector_tensor = torch.tensor(path_vector, dtype=torch.float32).to(self.device)
            """e_path_vector_tensor = self.encoder(path_vector_tensor)
            query = e_path_vector_tensor.clone().to(self.device)
            key = e_path_vector_tensor.clone().to(self.device)
            value = e_path_vector_tensor.clone().to(self.device)"""
        
        e_path_vector_tensor = self.encoder(path_vector_tensor)
        query = e_path_vector_tensor.clone().to(self.device)
        key = e_path_vector_tensor.clone().to(self.device)
        value = e_path_vector_tensor.clone().to(self.device)
        #print(query.shape)
        attention_vector,attention_weight = self.multihead_attn(query,key,value)
        #print(_.shape)
        #print(_.shape)
        #print(attention_vector.shape)
        
        return attention_vector ,attention_weight

    def forward(self, states,attention_vector, agent_idx):
        # Shared feature extraction
        #print(states.shape)
        #print(attention_vector.shape)
        #attention_vector_tensor = torch.stack(attention_vector)
        #features_ = torch.cat((states,attention_vector), dim=-1)
        #features = self.feature_extraction(features_)
        #q_values = self.q_values[agent_idx](features)
        
        
        # Get Q-values for the specified agent
        #q_values = self.q_values[agent_idx](features)
        """features = self.feature_extraction(states)
        sum_features = features+attention_vector

        q_values = self.q_values[agent_idx](sum_features)"""
        """features = self.feature_extraction(states)
        concatenated_features = torch.cat((features,attention_vector), dim=1)
        q_values = self.q_values[agent_idx](concatenated_features)"""
        features_ = torch.cat((states,attention_vector), dim=-1)
        #print(attention_vector)
        #features = self.feature_extraction(attention_vector)
        features = self.feature_extraction(features_)
        q_values = self.q_values[agent_idx](features)
        """features = self.feature_extraction(states)
        #print(states)
        #print(attention_vector)
        concatenated_features = torch.cat((features,attention_vector), dim=1)
        q_values = self.q_values[agent_idx](concatenated_features)"""
        #print(q_values)

        return q_values


class Agent:
    def __init__(self, num_agents_, state_dim, action_dim,link_num):
        self.lr = 0.01
        #self.critic_lr = 0.0015
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
        self.memory = deque(maxlen=2000)    #記得改140行 main q維度

    def _get_parameters(self, networks):
        params = []
        params += list(networks.parameters())
        return params

    """def soft_update_target_networks(self):
        for i in range(self.num_agents):
            for target_net, net in zip(self.target_actors[i].parameters(), self.actors[i].parameters()):
                target_net.data.copy_(self.tau * net.data + (1.0 - self.tau) * target_net.data)
            for target_net, net in zip(self.target_critics[i].parameters(), self.critics[i].parameters()):
                target_net.data.copy_(self.tau * net.data + (1.0 - self.tau) * target_net.data)"""
    
    def update_target(self):
    # Copy the weights from the DQN model to the target model
        #for i in range(self.num_agents):
        self.dqn_target.load_state_dict(self.dqn_model.state_dict())

    def get_action(self, state, agent_index,epsilon,attention_vector):
        state_tensor = torch.tensor(state, dtype=torch.float32).to(self.device)
        e_attention_vector = attention_vector.clone().unsqueeze(0)
        #e_attention_vector = torch.tensor(attention_vector).unsqueeze(0)
        #print(e_attention_vector.shape)
        q_value = self.dqn_model(state_tensor,e_attention_vector,agent_index).detach()
        #qval_ = q_value.data.numpy()
        qval_ = q_value.cpu().data.numpy()
        #print(qval_)
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
        #torch.save(model, "model/dqn_model/model")
        
        """for i in range(1, SIZE):
            for j in range(1, SIZE):
                if i != j:
                    torch.save(self.actors[k], "model/actor_model/{}_{}".format(i, j))
                    torch.save(self.critics[k], "model/critic_model/{}_{}".format(i, j))
                    k = k + 1"""
    
    def save_model_es(self, model):
        torch.save(model, "model/dqn_model/model")

    def load_model(self, SIZE):
        k = 0
        self.dqn_model = torch.load("model/dqn_model/model", map_location=self.device)
        #self.dqn_model.load_state_dict(torch.load("model/dqn_model/model", map_location=self.device))
        """for i in range(1, SIZE):
            for j in range(1, SIZE):
                if i != j:
                    self.actors[k] = torch.load("model/actor_model/{}_{}".format(i, j))
                    k = k + 1"""

    def load_model_es(self, SIZE):
        k = 0
        #self.dqn_model = torch.load("model/dqn_model/model", map_location=self.device)
        self.dqn_model.load_state_dict(torch.load("model/dqn_model/model", map_location=self.device))
    
    def update(self):
        mini_batch = random.sample(self.memory, self.batch_size)
        states = torch.tensor([i[0] for i in mini_batch], dtype=torch.float32).to(self.device)
        actions = torch.tensor([i[1] for i in mini_batch], dtype=torch.float32).to(self.device)
        next_states = torch.tensor([i[2] for i in mini_batch], dtype=torch.float32).to(self.device)
        rewards = torch.tensor([i[3] for i in mini_batch], dtype=torch.float32).to(self.device)
        #path_vector = torch.tensor([i[4] for i in mini_batch], dtype=torch.float32).to(self.device)
        path_vector = [i[4] for i in mini_batch]
        #global_rewards = torch.tensor([i[4] for i in mini_batch], dtype=torch.float32).to(self.device)

        #next_actions = [self.target_actors[j](torch.tensor(next_states, dtype=torch.float32)) for j in range(self.num_agents)]
        #q_value = [self.dqn_model(states,j) for j in range(self.num_agents)]
        #next_q_value = [self.dqn_target_model(next_states,j) for j in range(self.num_agents)]
        #print("aa")
        #print(path_vector)
        #print(states.shape)
        attention_vector,attention_weight = self.dqn_model.cal_attention_v(path_vector,training=True)
        target_attention_vector,target_attention_weight = self.dqn_target.cal_attention_v(path_vector,training=True)
        #print(states.shape)
        #print(attention_vector.shape)
        """target_attention_vector = self.dqn_target.cal_attention_v(path_vector,training=True)
        attention_vector_tensor = [torch.stack(vec) for vec in attention_vector]
        attention_vector_tensor_= torch.stack(attention_vector_tensor).to(self.device)
        target_attention_vector_tensor = [torch.stack(vec) for vec in target_attention_vector]
        target_attention_vector_tensor_= torch.stack(target_attention_vector_tensor).to(self.device)

        attention_vector_tensor_c = attention_vector_tensor_.clone()
        target_attention_vector_tensor_c = target_attention_vector_tensor_.clone()"""
        #target_attention_vector_tensor = torch.stack(target_attention_vector)
        #attention_vector = attention_vector[0]
        #target_attention_vector = target_attention_vector[0]
        #print(states.shape)
        #print(len(attention_vector))
        #print(attention_vector_tensor.shape)
        

        dqn_loss_all = 0
        #print(actions)
        #print(rewards[:, 0])
        #actor_loss_all = 0
        """for na,param in self.dqn_model.multihead_attn.named_parameters():
            print(param.data)"""
        """for na,param in self.dqn_model.encoder.named_parameters():
            print(param.data)"""

        for i in range(self.num_agents):
            #print("a")
            #q_values = self.critics[i](torch.cat((states, actions[:, i, :]), dim=1))
            #target_q_values = rewards[:, i] + self.gamma * self.target_critics[i](torch.cat((next_states, next_actions[i]), dim=1))
            #print(torch.tensor(attention_vector[:][i]).shape)
            q_value = self.dqn_model(states,attention_vector[:,i,],i)
            #print(q_value.shape)
            main_q_value = q_value.gather(dim=1, index=actions[:, i].unsqueeze(-1).long()).squeeze()
            #main_q_value = q_value.gather(dim=1, index=actions[:, i].unsqueeze(-1).long()).squeeze(0)
            #print(main_q_value)
            next_q_value = self.dqn_target(next_states,target_attention_vector[:,i,],i).detach()
            #print(next_q_value)
            max_q_value, argmax_actions = torch.max(next_q_value, dim=1)
            #print(max_q_value)
            #print(rewards[:,i])
            #print(next_q_value)
            #target_q_values = rewards[:, i] + self.gamma * max_q_value
            #target_q_values = (self.a1*rewards[:, i] + self.a3*global_rewards) + self.gamma * max_q_value
            target_q_values = rewards[:, i] + self.gamma * max_q_value
            #target_q_values = target_q_values.squeeze(0)
            #print("reward",rewards[:,i].shape)
            #print("target",target_q_values)
            #print(q_values.shape)
            dqn_loss = F.mse_loss(main_q_value,target_q_values)
            #print("b")
            #critic_loss = nn.MSELoss()(q_values, target_q_values)
            #print(critic_loss,i)
            self.dqn_opt.zero_grad()
            #critic_loss.backward(retain_graph=True)
            dqn_loss.backward(retain_graph=True)
            #print(attention_vector[:,i,].grad)
            #print("c")
            #print(dqn_loss.grad)
            #print(q_value.grad)
            #max_grad_norm = 10000.0  # 设置梯度裁剪的阈值
            """for na,param in self.dqn_model.multihead_attn.named_parameters():
                print(param.data)"""
            #nn.utils.clip_grad_norm_(self.dqn_model.parameters(), max_grad_norm)
            #for param in self.dqn_model.parameters():
                #print(param.grad)
            self.dqn_opt.step()
            #print("d")
            dqn_loss_all += dqn_loss.item()


        return dqn_loss_all
