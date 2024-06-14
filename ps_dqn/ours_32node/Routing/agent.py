import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import random
from collections import deque


class MA_PS_DQN(nn.Module):
    def __init__(self, num_agents, input_size, output_size):
        super(MA_PS_DQN, self).__init__()
        self.hidden_dim = 32
        self.hidden_dim_2 = 32
        self.hidden_dim_3 = 32

        # Shared feature extraction layers
        self.feature_extraction = nn.Sequential(
            nn.Linear(input_size, self.hidden_dim ),
            nn.ReLU(),
            nn.Linear(self.hidden_dim , self.hidden_dim_2 ),
            nn.ReLU()
        )

        # Independent output layers for each agent
        self.q_values = nn.ModuleList([
            nn.Linear(self.hidden_dim_2 , output_size) for _ in range(num_agents)
        ])
        """self.q_values = nn.ModuleList([
            nn.Sequential(
                nn.Linear(self.hidden_dim_2, self.hidden_dim_3),
                nn.ReLU(),
                nn.Linear(self.hidden_dim_3, output_size)
            ) for _ in range(num_agents)
        ])"""

    def forward(self, states, agent_idx):
        # Shared feature extraction
        #print(states)
        features = self.feature_extraction(states)
        #print(features)
        # Get Q-values for the specified agent
        q_values = self.q_values[agent_idx](features)
        #print(q_values)

        return q_values


class Agent:
    def __init__(self, num_agents_, state_dim, action_dim):
        self.lr = 0.01
        #self.critic_lr = 0.0015
        self.gamma = 0.9
        self.num_agents = num_agents_
        self.action_size = action_dim
        self.a1=1.0
        self.a2=0.0
        self.a3=0.0
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.dqn_model = MA_PS_DQN(num_agents_,state_dim,action_dim).to(self.device)
        self.dqn_target = MA_PS_DQN(num_agents_,state_dim,action_dim).to(self.device)

        

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

    def get_action(self, state, agent_index,epsilon):
        state_tensor = torch.tensor(state, dtype=torch.float32).detach().to(self.device)
        q_value = self.dqn_model(state_tensor,agent_index)
        #qval_ = q_value.data.numpy()
        qval_ = q_value.cpu().data.numpy()
        #print(qval_)
        if np.random.rand() <= epsilon:
            action = np.random.choice(self.action_size)
        else:
            action = np.argmax(qval_) 
        return action

    def append_sample(self, state, actions, next_state, reward):
        self.memory.append((state, actions, next_state, reward))


    
    def save_model(self, SIZE):
        k = 0
        torch.save(self.dqn_model, "model/dqn_model/model")
        """for i in range(1, SIZE):
            for j in range(1, SIZE):
                if i != j:
                    torch.save(self.actors[k], "model/actor_model/{}_{}".format(i, j))
                    torch.save(self.critics[k], "model/critic_model/{}_{}".format(i, j))
                    k = k + 1"""

    def load_model(self, SIZE):
        k = 0
        self.dqn_model = torch.load("model/dqn_model/model", map_location=self.device)
        """for i in range(1, SIZE):
            for j in range(1, SIZE):
                if i != j:
                    self.actors[k] = torch.load("model/actor_model/{}_{}".format(i, j))
                    k = k + 1"""

    def update(self):
        mini_batch = random.sample(self.memory, self.batch_size)
        states = torch.tensor([i[0] for i in mini_batch], dtype=torch.float32).to(self.device)
        actions = torch.tensor([i[1] for i in mini_batch], dtype=torch.float32).to(self.device)
        next_states = torch.tensor([i[2] for i in mini_batch], dtype=torch.float32).to(self.device)
        rewards = torch.tensor([i[3] for i in mini_batch], dtype=torch.float32).to(self.device)
        #print(.shape)
        #global_rewards = torch.tensor([i[4] for i in mini_batch], dtype=torch.float32).to(self.device)

        #next_actions = [self.target_actors[j](torch.tensor(next_states, dtype=torch.float32)) for j in range(self.num_agents)]
        #q_value = [self.dqn_model(states,j) for j in range(self.num_agents)]
        #next_q_value = [self.dqn_target_model(next_states,j) for j in range(self.num_agents)]
        #print("aa")

        dqn_loss_all = 0
        #print(actions)
        #print(rewards[:, 0])
        #actor_loss_all = 0

        for i in range(self.num_agents):
            #q_values = self.critics[i](torch.cat((states, actions[:, i, :]), dim=1))
            #target_q_values = rewards[:, i] + self.gamma * self.target_critics[i](torch.cat((next_states, next_actions[i]), dim=1))
            q_value = self.dqn_model(states,i)
            #print(q_value)
            main_q_value = q_value.gather(dim=1, index=actions[:, i].unsqueeze(-1).long()).squeeze()
            #main_q_value = q_value.gather(dim=1, index=actions[:, i].unsqueeze(-1).long()).squeeze(0)
            #print(main_q_value)
            next_q_value = self.dqn_target(next_states,i)
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
            #critic_loss = nn.MSELoss()(q_values, target_q_values)
            #print(critic_loss,i)
            self.dqn_opt.zero_grad()
            #critic_loss.backward(retain_graph=True)
            #dqn_loss.backward(retain_graph=True)
            dqn_loss.backward()
            #max_grad_norm = 10000.0  # 设置梯度裁剪的阈值
            #nn.utils.clip_grad_norm_(self.dqn_model.parameters(), max_grad_norm)
            #for param in self.dqn_model.parameters():
                #print(param.grad)
            self.dqn_opt.step()
            dqn_loss_all += dqn_loss.item()


        return dqn_loss_all
