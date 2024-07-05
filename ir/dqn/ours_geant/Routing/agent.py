import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import random
from collections import deque

class DQN(nn.Module):
    def __init__(self, input_size, output_size):
        super(DQN, self).__init__()
        self.hidden_dim = 64

        
        self.fc1 = nn.Linear(input_size, self.hidden_dim)
        self.fc2 = nn.Linear(self.hidden_dim, self.hidden_dim)
        self.fc3 = nn.Linear(self.hidden_dim, self.hidden_dim)
        self.fc4 = nn.Linear(self.hidden_dim,output_size)

    

    def forward(self, states):
        x = F.relu(self.fc1(states))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        q_values = self.fc4(x)

        return q_values


class Agent:
    def __init__(self, num_agents_, state_dim, action_dim):
        self.lr = 0.01
        self.gamma = 0.9
        self.num_agents = num_agents_
        self.action_size = action_dim

        self.dqn_model = [DQN(state_dim, action_dim) for _ in range(self.num_agents)]
        self.dqn_target = [DQN(state_dim, action_dim) for _ in range(self.num_agents)]

        self.dqn_opt = optim.Adam(params=self._get_parameters(self.dqn_model),lr=self.lr)

        self.batch_size = 64
        self.tau = 0.005
        self.memory = deque(maxlen=2000)

    def _get_parameters(self, networks):
        params = []
        for net in networks:
            params += list(net.parameters())
        return params
    
    def update_target(self):
        for i in range(self.num_agents):
            self.dqn_target[i].load_state_dict(self.dqn_model[i].state_dict())

    def get_action(self, state, agent_index,epsilon):
        state_tensor = torch.tensor(state, dtype=torch.float32).detach()
        q_value = self.dqn_model[agent_index](state_tensor)
        qval_ = q_value.data.numpy()
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


    def load_model(self, SIZE):
        k = 0
        self.dqn_model = torch.load("model/dqn_model/model")


    def update(self):
        mini_batch = random.sample(self.memory, self.batch_size)
        states = torch.tensor([i[0] for i in mini_batch], dtype=torch.float32)
        actions = torch.tensor([i[1] for i in mini_batch], dtype=torch.float32)
        next_states = torch.tensor([i[2] for i in mini_batch], dtype=torch.float32)
        rewards = torch.tensor([i[3] for i in mini_batch], dtype=torch.float32)

        dqn_loss_all = 0

        for i in range(self.num_agents):
            q_value = self.dqn_model[i](states)
            main_q_value = q_value.gather(dim=1, index=actions[:, i].unsqueeze(-1).long()).squeeze()
            next_q_value = self.dqn_target[i](next_states)
            max_q_value, argmax_actions = torch.max(next_q_value, dim=1)
            target_q_values = rewards[:, i] + self.gamma * max_q_value
            dqn_loss = F.mse_loss(main_q_value,target_q_values)
            self.dqn_opt.zero_grad()
            dqn_loss.backward()
            self.dqn_opt.step()
            dqn_loss_all += dqn_loss.item()


        return dqn_loss_all
