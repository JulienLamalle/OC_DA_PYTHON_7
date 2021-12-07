import itertools
import numpy as np
from data_reader.csv_data_reader import csv_data_reader

def bruteforce(actions):

    max_price = 500
    total_spent = 0
    actions_bought = []
    actions_bought_name = []
    all_combinations = []
    all_combinations_bought = []
    all_combinations_bought_name = []

    for r in range(len(actions) + 1):
        combinations_object = itertools.combinations(actions, r)
        all_combinations += list(combinations_object)

    for combination in all_combinations:
        for x in combination:
            total_spent += x[1]
            if total_spent <= 500:
                actions_bought_name.append(x[0])
                actions_bought.append(((x[1]) * (x[2])))
        total_spent = 0
        if len(actions_bought) > 1:
            actions_bought = np.sum(actions_bought)
            all_combinations_bought.append(actions_bought)
            all_combinations_bought_name.append(actions_bought_name)
        actions_bought = []
        actions_bought_name = []

    max_value = int(max(all_combinations_bought))
    max_index = all_combinations_bought.index((max_value))
    max_value /= 100
    print(f"Le meilleur bénéfice est obtenu avec les actions suivantes : {all_combinations_bought_name[max_index]} et il est de {max_value} €")
    
bruteforce(csv_data_reader("data/twenty_actions.csv"))
