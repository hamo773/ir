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
actions_list = np.arange(20)

def seed_torch(seed):
    #random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    #random.seed(SEED)
    #tf.random.set_seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

def DRL_thread():
    print("enter thread")
    #seed_tensorflow(8)
    column, row = SIZE,SIZE
    madqn_agents = agent.Agent((SIZE-1)*(SIZE-2), 60*3,20)

    all_path_list = state_to_action()

    step = 0
    epsilon_ini = 0.1
    epsilon_final = 0.01
    epsilon = 0.1
    action_memory = []
    chosen_path_memory = np.zeros((SIZE,SIZE))
    state_memory = np.zeros((SIZE,SIZE))

    reward_list = []
    reward_list_bwd = []
    reward_list_delay = []
    reward_list_loss = []
    loss_value_list = []
    delay_value_list = []
    dqn_loss_list = []
    change_path_list = []
    print("Start learning")
    while True:
        time_in = time.time()
        step += 1
        state = get_state().flatten()  # get new state
        all_reward,all_reward_indicator,loss_value_path,delay_value_path = path_metrics_to_reward()
        drl_paths = {}
        reward_all = 0
        reward_all_bwd = 0
        reward_all_delay = 0
        reward_all_loss = 0
        loss_value_all = 0
        delay_value_all = 0
        change_path_counter = 0

        agent_index = 0 
        all_agent_reward_list = []
        all_agent_action_list = []
        choose_path_list = []

        for i in range(1,SIZE):
            drl_paths.setdefault(str(i), {})
            for j in range(1,SIZE):
                if i != j:
                    reward = all_reward[str(i)][str(j)][int(chosen_path_memory[i][j])]
                    #print(reward)
                    all_agent_reward_list.append(reward)
                    reward_all += reward
                    reward_bwd = all_reward_indicator[str(i)][str(j)][int(chosen_path_memory[i][j])][0]
                    reward_all_bwd += reward_bwd
                    reward_delay = all_reward_indicator[str(i)][str(j)][int(chosen_path_memory[i][j])][1]
                    reward_all_delay += reward_delay
                    reward_loss = all_reward_indicator[str(i)][str(j)][int(chosen_path_memory[i][j])][2]
                    reward_all_loss += reward_loss

                    action = madqn_agents.get_action([state],agent_index,epsilon)
                    all_agent_action_list.append(action)
                    chosen_path = action 
                    if chosen_path!=chosen_path_memory[i][j]:
                        change_path_counter = change_path_counter + 1
                        print(i,j,chosen_path)
                    chosen_path_memory[i][j] = chosen_path
                    #print(chosen_path)
                    drl_paths[str(i)][str(j)] = [all_path_list[i][j][chosen_path]]
                    agent_index = agent_index + 1
                    
        if step != 1:
            madqn_agents.append_sample(state_memory,action_memory, state,all_agent_reward_list)
        if len(madqn_agents.memory) > madqn_agents.batch_size:
            dqn_loss = madqn_agents.update()
            if step % 30 == 0:
                madqn_agents.update_target()
            dqn_loss_list.append(float(dqn_loss))
            path = 'dqn_loss.txt'
            f = open(path, 'w')
            f.writelines(str(dqn_loss_list))
            f.close()
        if step == 3010:
            madqn_agents.save_model(SIZE)
            return

        action_memory = all_agent_action_list 

        # write route path
        with open('./drl_paths.json','w') as json_file:
            json.dump(drl_paths, json_file, indent=2)

        state_memory = state
        reward_list.append(float(reward_all))
        path = 'output.txt'
        f = open(path, 'w')
        f.writelines(str(reward_list))
        f.close()
        change_path_list.append(int(change_path_counter))
        path = 'changepath.txt'
        f = open(path, 'w')
        f.writelines(str(change_path_list))
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
        print("------------------------------------------ step %d ------------------------------------------" % step)
        print("------------------------------------------  epsilon  %f ------------------------------------------   " % epsilon)
        time_end = time.time()
        if time_end - time_in < 10 :
            time.sleep(10 - (time_end - time_in)) # wait for monitor period
        print(time_end-time_in)
        if epsilon > epsilon_final:
            epsilon -= (epsilon_ini - epsilon_final)/2000



def DRL_eval():
    madqn_agents = agent.Agent((SIZE-1)*(SIZE-2), 60*3,20)
    print("load model...")
    try:
        madqn_agents.load_model(SIZE)
        
    except:
        print("No model, have to train model first")
        return 
                
    print("load model success....")
    all_path_list = state_to_action()
    print("Start eval")
    temperature = 1.0

    chosen_path_memory = np.zeros((SIZE,SIZE))

    while True:
        time_in = time.time()
        state = get_state().flatten()  # get new state
        drl_paths = {}
        agent_index=0
        for i in range(1,SIZE):
            drl_paths.setdefault(str(i), {})
            for j in range(1,SIZE):
                if i != j:
                    action = madqn_agents.get_action([state],agent_index,0)
                    chosen_path = action
                    """if chosen_path!=chosen_path_memory[i][j]:
                        print(i,j)
                        print(chosen_path)"""
                    chosen_path_memory[i][j] = chosen_path
                    drl_paths[str(i)][str(j)] = [all_path_list[i][j][chosen_path]]
                    agent_index = agent_index + 1

        file_name = 'chosen_path_data.txt'
        n = chosen_path_memory.shape[0]
        index_value_array = np.column_stack((np.repeat(np.arange(n), n), np.tile(np.arange(n), n), chosen_path_memory.flatten()))
        np.savetxt(file_name, index_value_array, fmt='%d', header='Row, Column, Value', delimiter=',')

        # write route path
        with open('./drl_paths.json','w') as json_file:
            json.dump(drl_paths, json_file, indent=2)
        print("dump")
        time_end = time.time()
        if time_end - time_in < setting.MONITOR_PERIOD :
            time.sleep(setting.MONITOR_PERIOD - (time_end - time_in)) # wait for monitor period



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
                    met_norm = [normalize(met_val, 0,100, min(paths_metrics_dict[str(i)][str(j)][m][0]), max(paths_metrics_dict[str(i)][str(j)][m][0])) for met_val in paths_metrics_dict[str(i)][str(j)][m][0]]
                else:    
                    met_norm = [normalize(met_val, 100, 0, min(paths_metrics_dict[str(i)][str(j)][m][0]), max(paths_metrics_dict[str(i)][str(j)][m][0])) for met_val in paths_metrics_dict[str(i)][str(j)][m][0]]
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
    try:
        file = "./net_info.csv"
        data = pd.read_csv(file)
        for i in range(60):
            state[i][0] = data["bwd"][i]/100
            state[i][1] = data["delay"][i]
            state[i][2] = data["pkloss"][i]
            state_0 = np.full(60, 200000)
        #state = np.insert(state, 0, values=state_0, axis=1)
        return state
    except:
        time.sleep(0.35)
        file = "./net_info.csv"
        data = pd.read_csv(file)
        for i in range(60):
            state[i][0] = data["bwd"][i]/1000
            state[i][1] = data["delay"][i]
            state[i][2] = data["pkloss"][i]
        #state_0 = np.full(60, 200000)
        #state = np.insert(state, 0, values=state_0, axis=1)
        return state

def reward_rank(src, dst, paths_metrics_dict, act, metrics):

    beta1=1
    beta2=1
    beta3=1

    save_bwd = 0
    save_delay = 0
    save_loss = 0

    bwd_sort = sorted(paths_metrics_dict[str(src)][str(dst)][metrics[0]][1])
    for rank in range(20):
        if paths_metrics_dict[str(src)][str(dst)][metrics[0]][1][act] == bwd_sort[rank]:
            save_bwd = rank

    delay_sort = sorted(paths_metrics_dict[str(src)][str(dst)][metrics[1]][1])

    for rank in range(20):
        if paths_metrics_dict[str(src)][str(dst)][metrics[1]][1][act] == delay_sort[rank]:
            save_delay = rank

    loss_sort = sorted(paths_metrics_dict[str(src)][str(dst)][metrics[2]][1])

    for rank in range(20):
        if paths_metrics_dict[str(src)][str(dst)][metrics[2]][1][act] == loss_sort[rank]:
            save_loss = rank

    reward =beta1*save_bwd + beta2*save_delay + beta3*save_loss
    return reward

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
