import itertools
import numpy as np

actions = [
    ("Action-1", 20, 5),
    ("Action-2", 30, 10),
    ("Action-3", 50, 15),
    ("Action-4", 70, 20),
    ("Action-5", 60, 17),
    ("Action-6", 80, 25),
    ("Action-7", 22, 7),
    ("Action-8", 26, 11),
    ("Action-9", 48, 13),
    ("Action-10", 34, 27),
    ("Action-11", 42, 17),
    ("Action-12", 110, 9),
    ("Action-13", 38, 23),
    ("Action-14", 14, 1),
    ("Action-15", 18, 3),
    ("Action-16", 8, 8),
    ("Action-17", 4, 12),
    ("Action-18", 10, 14),
    ("Action-19", 24, 21),
    ("Action-20", 114, 18),
]

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
    
bruteforce(actions)
