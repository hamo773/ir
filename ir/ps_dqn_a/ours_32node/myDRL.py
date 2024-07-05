import sys
sys.path.insert(0,'./Routing')
import agent
import pandas as pd
import numpy as np
import time
import json,ast
#import tensorflow as tf
import torch
import setting
import copy
import os

SIZE = 33
link_num = 60
actions_list = np.arange(20)
paths_metrics_minmax_dict = {}
link_index = {} 

def seed_torch(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def DRL_thread():
    print("enter thread")
    column, row = SIZE,SIZE
    madqn_agents = agent.Agent((SIZE-1)*(SIZE-2), 60*3,20,link_num)
    gen_link_index()
    all_path_list = state_to_action()
    init_minmax_dic()

    step = 0
    epsilon_ini = 0.5
    epsilon_final = 0.01
    epsilon = 0.5
    action_memory = []
    reward_memory = []
    path_vector_memory = []
    state_memory = np.zeros((SIZE,SIZE))

    reward_list = []
    mlu_list = []
    reward_list_bwd = []
    reward_list_delay = []
    reward_list_loss = []
    loss_value_list = []
    delay_value_list = []
    dqn_loss_list = []
    change_path_list = []
    reward_delta_list = []
    drl_paths = {}
    print("Start learning")
    while True:
        time_in = time.time()
        step += 1
        state,mlu = get_state()  # get new state
        state=state.flatten()
        all_reward,all_reward_indicator,loss_value_path,delay_value_path = path_metrics_to_reward()
        reward_all = 0
        reward_delta = 0
        reward_all_bwd = 0
        reward_all_delay = 0
        reward_all_loss = 0
        change_path_counter = 0

        agent_index = 0 
        all_agent_reward_list = []
        all_agent_delta_reward_list = []
        all_agent_action_list = []
        path_vector = []

        path_vector = gen_path_vector(drl_paths)
        attention_vector= madqn_agents.dqn_model.cal_attention_v(path_vector)
        attention_vector = attention_vector[0].detach()

        for i in range(1,SIZE):
            drl_paths.setdefault(str(i), {})
            for j in range(1,SIZE):
                if i != j:
                    if step>=3:
                        reward = all_reward[str(i)][str(j)][action_memory[0][agent_index]]
                        all_agent_reward_list.append(reward)
                        reward_all += reward
                        reward_bwd = all_reward_indicator[str(i)][str(j)][action_memory[0][agent_index]][0]
                        reward_all_bwd += reward_bwd
                        reward_delay = all_reward_indicator[str(i)][str(j)][action_memory[0][agent_index]][1]
                        reward_all_delay += reward_delay
                        reward_loss = all_reward_indicator[str(i)][str(j)][action_memory[0][agent_index]][2]
                        reward_all_loss += reward_loss

                    if step>=4:
                        all_agent_delta_reward_list.append(100*(reward-reward_memory[agent_index]))
                        reward_delta += (reward-reward_memory[agent_index])                     #r3-r2

                    action = madqn_agents.get_action([state],agent_index,epsilon,attention_vector[agent_index])
                    all_agent_action_list.append(action)
                    chosen_path = action 
                   
                    drl_paths[str(i)][str(j)] = [all_path_list[i][j][chosen_path]]
                    agent_index = agent_index + 1
                    

        action_memory.append(all_agent_action_list)
        print(all_agent_action_list[0])
        reward_memory = all_agent_reward_list 
        with open('./drl_paths.json','w') as json_file:
            json.dump(drl_paths, json_file, indent=2)
        if step >= 3:
            if step ==3:
                action_memory.pop(0)
            else:
                madqn_agents.append_sample(state_memory,action_memory[0], state,all_agent_delta_reward_list,path_vector_memory)   #(s2,a1,p1,r3-r2,s3)
                print(action_memory[0][0])
                action_memory.pop(0)
        state_memory = state
        path_vector_memory = path_vector
        if len(madqn_agents.memory) > madqn_agents.batch_size:
            dqn_loss = madqn_agents.update()
            if step % 30 == 0:
                madqn_agents.update_target()
            dqn_loss_list.append(float(dqn_loss))
            path = 'dqn_loss.txt'
            f = open(path, 'w')
            f.writelines(str(dqn_loss_list))
            f.close()
        if step == 10:
            madqn_agents.save_model(SIZE)
            return

        path = 'output_all.txt'
        if step==1:
            with open(path, 'w') as f:
                f.write(str(all_agent_reward_list) + '\n')
        else:    
            with open(path, 'a') as f:
                f.write(str(all_agent_reward_list) + '\n')
        reward_list.append(float(reward_all))
        path = 'output.txt'
        f = open(path, 'w')
        f.writelines(str(reward_list))
        f.close()
        mlu_list.append(float(mlu))
        path = 'training_mlu.txt'
        f = open(path, 'w')
        f.writelines(str(mlu_list))
        f.close()
        reward_list_bwd.append(int(reward_all_bwd))
        path = 'output_bwd.txt'
        f = open(path, 'w')
        f.writelines(str(reward_list_bwd))
        f.close()
        reward_list_delay.append(int(reward_all_delay))
        path = 'output_delay.txt'
        f = open(path, 'w')
        f.writelines(str(reward_list_delay))
        f.close()
        reward_list_loss.append(int(reward_all_loss))
        path = 'output_loss.txt'
        f = open(path, 'w')
        f.writelines(str(reward_list_loss))
        f.close()
        path = 'output_delta.txt'
        reward_delta_list.append(reward_delta)
        f = open(path, 'w')
        f.writelines(str(reward_delta_list))
        f.close()
        print("------------------------------------------ step %d ------------------------------------------" % step)
        print("------------------------------------------  epsilon  %f ------------------------------------------   " % epsilon)
        if epsilon > 0.1:
            epsilon -= (epsilon_ini - 0.1)/1000
        elif epsilon >epsilon_final:
            epsilon -= (0.1 - epsilon_final)/1000
        time_end = time.time()
        #if time_end - time_in < 10 :
            #time.sleep(10 - (time_end - time_in)) # wait for monitor period


def DRL_eval():
    madqn_agents = agent.Agent((SIZE-1)*(SIZE-2), 60*3,20,link_num)
    print("load model...")
    try:
        madqn_agents.load_model(SIZE)
    except:
        print("No model, have to train model first")
        return 
    gen_link_index()
    print("load model success....")
    all_path_list = state_to_action()
    print("Start eval")
    change_path_counter = 0
    

    chosen_path_memory = np.zeros((SIZE,SIZE))
    drl_paths = {}
    while True:
        time_in = time.time()
        state,mlu = get_state() 
        state = state.flatten()
        agent_index=0
        path_vector = gen_path_vector(drl_paths)
        attention_vector= madqn_agents.dqn_model.cal_attention_v(path_vector)
        attention_vector = attention_vector[0]
 
        for i in range(1,SIZE):
            drl_paths.setdefault(str(i), {})
            for j in range(1,SIZE):
                if i != j:
                    action = madqn_agents.get_action([state],agent_index,0,attention_vector[agent_index])
                    chosen_path = action
                    chosen_path_memory[i][j] = chosen_path
                    drl_paths[str(i)][str(j)] = [all_path_list[i][j][chosen_path]]
                    agent_index = agent_index + 1

        with open('./drl_paths.json','w') as json_file:
            json.dump(drl_paths, json_file, indent=2)
        print("dump")
        time_end = time.time()
        if time_end - time_in < setting.MONITOR_PERIOD :
            time.sleep(setting.MONITOR_PERIOD - (time_end - time_in)) # wait for monitor period

def gen_path_vector(drl_paths):
    path_vector = np.zeros((((SIZE-1)*(SIZE-2)), link_num))
    agent_idx = 0
    if not drl_paths:
        return path_vector
    for i in range(1,SIZE):
        for j in range(1,SIZE):
            if i != j:
                for k in range(1,len(drl_paths[str(i)][str(j)][0])):
                    link=(drl_paths[str(i)][str(j)][0][k-1],drl_paths[str(i)][str(j)][0][k])
                    reversed_link=(drl_paths[str(i)][str(j)][0][k],drl_paths[str(i)][str(j)][0][k-1])
                    if link in link_index:
                        index = link_index[link]
                    else:
                        index = link_index[reversed_link]
                    path_vector[agent_idx][index] =  100
                agent_idx=agent_idx+1
    return path_vector

def gen_link_index():
    graph = {}
    with open('bw_r.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            src, dst,_, bw = map(int, data)  
            add_link(src,dst,graph)



def add_link(node1, node2,graph):
    link = (node1, node2)
    reversed_link = (node2, node1)

    if link in link_index:
        index = link_index[link]
    elif reversed_link in link_index:
        index = link_index[reversed_link]
    else:
        index = len(link_index) 
        link_index[link] = index
        graph[index] = link


def init_minmax_dic():
    #paths_metrics_minmax_dict.setdefault(i, {})
    metrics = ['bwd_paths','delay_paths','loss_paths']
    for i in range(1,SIZE):
        paths_metrics_minmax_dict.setdefault(str(i), {})
        for j in range(1,SIZE):
            paths_metrics_minmax_dict[str(i)].setdefault(str(j), {})
            for m in metrics:
                paths_metrics_minmax_dict[str(i)][str(j)].setdefault(m,{})
                paths_metrics_minmax_dict[str(i)][str(j)][m]['min']=100000000
                paths_metrics_minmax_dict[str(i)][str(j)][m]['max']= -1
                




def path_metrics_to_reward():
        
    # read path metrices file
    file = './paths_metrics.json'
    rewards_dic = {}
    rewards_indicator = {}
    loss_value = {}
    delay_value = {}
    metrics = ['bwd_paths','delay_paths','loss_paths']
    try:
        with open(file,'r') as json_file:
            paths_metrics_dict = json.load(json_file)
            paths_metrics_dict = ast.literal_eval(json.dumps(paths_metrics_dict))
    except:
        time.sleep(0.35) # wait until file is ok
        with open(file,'r') as json_file:
            paths_metrics_dict = json.load(json_file)
            paths_metrics_dict = ast.literal_eval(json.dumps(paths_metrics_dict))


    for i in paths_metrics_dict:
        rewards_dic.setdefault(i,{})
        rewards_indicator.setdefault(i,{})
        loss_value.setdefault(i,{})
        delay_value.setdefault(i,{})
        for j in paths_metrics_dict[i]:
            rewards_dic.setdefault(j,{})
            rewards_indicator.setdefault(j,{})
            loss_value.setdefault(j,{})
            delay_value.setdefault(i,{})
            loss_value[i][j] = paths_metrics_dict[str(i)][str(j)]['loss_paths'][0]
            delay_value[i][j] = paths_metrics_dict[str(i)][str(j)]['delay_paths'][0]
            for m in metrics:
                if m == metrics[0]:
                    bwd_cost = []
                    for val in paths_metrics_dict[str(i)][str(j)][m][0]:
                        bwd_cost.append(round(val, 15))
                    paths_metrics_dict[str(i)][str(j)][m][0] = bwd_cost
                    paths_metrics_minmax_dict[i][j][m]['max'] = max(paths_metrics_minmax_dict[i][j][m]['max'],max(paths_metrics_dict[str(i)][str(j)][m][0]))
                    paths_metrics_minmax_dict[i][j][m]['min'] = min(paths_metrics_minmax_dict[i][j][m]['min'],min(paths_metrics_dict[str(i)][str(j)][m][0]))
                    met_norm = [normalize(met_val, 0,100, paths_metrics_minmax_dict[i][j][m]['min'], max(paths_metrics_dict[str(i)][str(j)][m][0])) for met_val in paths_metrics_dict[str(i)][str(j)][m][0]]
                elif m == metrics[1]:
                    cost = [] 
                    for val in paths_metrics_dict[str(i)][str(j)][m][0]:
                        if val >1.5 :
                            temp = 1/val
                            cost.append(round(temp, 15))
                        else:
                            cost.append(1.5)
                    paths_metrics_dict[str(i)][str(j)][m][0] = cost
                    paths_metrics_minmax_dict[i][j][m]['max'] = max(paths_metrics_minmax_dict[i][j][m]['max'],max(cost))
                    paths_metrics_minmax_dict[i][j][m]['min'] = min(paths_metrics_minmax_dict[i][j][m]['min'],min(cost))
                    met_norm = [normalize(met_val, 0, 100, paths_metrics_minmax_dict[i][j][m]['min'], paths_metrics_minmax_dict[i][j][m]['max']) for met_val in paths_metrics_dict[str(i)][str(j)][m][0]]
                elif m == metrics[2]:    
                    cost = [] 
                    for val in paths_metrics_dict[str(i)][str(j)][m][0]:
                        if val > 0.001: 
                            temp = 1/val
                            cost.append(round(temp, 15))
                        else:
                            cost.append(1/0.001)
                    paths_metrics_dict[str(i)][str(j)][m][0] = cost
                    paths_metrics_minmax_dict[i][j][m]['max'] = max(paths_metrics_minmax_dict[i][j][m]['max'],max(cost))
                    paths_metrics_minmax_dict[i][j][m]['min'] = min(paths_metrics_minmax_dict[i][j][m]['min'],min(cost))
                    met_norm = [normalize(met_val, 0, 100, paths_metrics_minmax_dict[i][j][m]['min'], paths_metrics_minmax_dict[i][j][m]['max']) for met_val in paths_metrics_dict[str(i)][str(j)][m][0]]
               
                paths_metrics_dict[str(i)][str(j)][m].append(met_norm)
    
    for i in paths_metrics_dict:
        for j in paths_metrics_dict[i]:
            rewards_actions = []   
            rewards_actions_indicator = []           
            for act in range(20):
                rewards_actions.append(reward(i,j,paths_metrics_dict,act,metrics))
                rewards_actions_indicator.append(rewards_indicator_fun(i,j,paths_metrics_dict,act,metrics))
                rewards_dic[i][j] = rewards_actions
                rewards_indicator[i][j] = rewards_actions_indicator
    return rewards_dic,rewards_indicator,loss_value,delay_value


def normalize(value, minD, maxD, min_val, max_val):
    if max_val == min_val:
        value_n = (maxD + minD) / 2 
    else:
        value_n = (maxD - minD) * (value - min_val) / (max_val - min_val) + minD
    return round(value_n,15)
                    

def get_state(): # get the current network state
    state = np.zeros((60,3))
    bwd = np.full(60, 200000)
    mlu=0
    try:
        file = "./net_info.csv"
        data = pd.read_csv(file)
        for i in range(60):
            mlu=max(mlu,(200000-data["bwd"][i])/bwd[i])
            state[i][0] = data["bwd"][i]/1000
            state[i][1] = data["delay"][i]
            state[i][2] = data["pkloss"][i]
        return state,mlu
    except:
        time.sleep(0.35)
        file = "./net_info.csv"
        data = pd.read_csv(file)
        for i in range(60):
            mlu=max(mlu,(200000-data["bwd"][i])/bwd[i])
            state[i][0] = data["bwd"][i]/1000
            state[i][1] = data["delay"][i]
            state[i][2] = data["pkloss"][i]
        return state,mlu



def reward(src, dst, paths_metrics_dict, act, metrics):
    '''
    paths_metrics_dict ={src:{dst:{metric1:[[orig value list],[normalized value list]]},metric2...}}
    '''
    beta1=1
    beta2=1
    beta3=1
    reward = beta1*paths_metrics_dict[str(src)][str(dst)][metrics[0]][1][act] + beta2*paths_metrics_dict[str(src)][str(dst)][metrics[1]][1][act] + beta3*paths_metrics_dict[str(src)][str(dst)][metrics[2]][1][act]
    return round(reward,15)

def rewards_indicator_fun(src, dst, paths_metrics_dict, act, metrics):
    '''
    paths_metrics_dict ={src:{dst:{metric1:[[orig value list],[normalized value list]]},metric2...}}
    '''
    beta1=1
    beta2=1
    beta3=1
    reward = beta1*paths_metrics_dict[str(src)][str(dst)][metrics[0]][1][act] + beta2*paths_metrics_dict[str(src)][str(dst)][metrics[1]][1][act] + beta3*paths_metrics_dict[str(src)][str(dst)][metrics[2]][1][act]
    #return (round(paths_metrics_dict[str(src)][str(dst)][metrics[0]][1][act] ,15),round(paths_metrics_dict[str(src)][str(dst)][metrics[1]][1][act] ,15),round(paths_metrics_dict[str(src)][str(dst)][metrics[2]][1][act] ,15))
    return (paths_metrics_dict[str(src)][str(dst)][metrics[0]][1][act],paths_metrics_dict[str(src)][str(dst)][metrics[1]][1][act],paths_metrics_dict[str(src)][str(dst)][metrics[2]][1][act])


def state_to_action(): # 20 paths according src,dst
    file = './Routing/k_paths.json'
    paths = []
    with open(file,'r') as json_file:
        paths = json.load(json_file)
    column, row = SIZE,SIZE
    paths_20 = [[0]*row for _ in range(column)]
    for i in range(1,SIZE):
        for j in range(1,SIZE):
            if i != j:
                paths_20[i][j] = paths[str(i)][str(j)]
    return paths_20
if __name__ == "__main__":
    print("1 : learning phase Reward classic\n2 : Performance test")
    i = input()
    if i == str(1):
        DRL_thread()
    else:
        DRL_eval()
