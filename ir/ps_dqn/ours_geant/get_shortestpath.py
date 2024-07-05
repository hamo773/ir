import json



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

SIZE=24
all_path_list = state_to_action()
drl_paths = {}


for i in range(1,SIZE):
    drl_paths.setdefault(str(i), {})
    for j in range(1,SIZE):
        if i!=j:
            drl_paths[str(i)][str(j)] = [all_path_list[i][j][0]]

with open('./drl_paths.json','w') as json_file:
    json.dump(drl_paths, json_file, indent=2)



