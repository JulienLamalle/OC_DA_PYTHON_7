from data_reader.csv_data_reader import csv_data_reader
import time

def optimized(max_price_in_euros, actions):
  start_time = time.time()
  max_price_in_cents = max_price_in_euros * 100
  
  for index, action in enumerate(actions):
    action = (action[0], action[1], action[1] * action[2] / 100)
    actions[index] = action
    
  matrice = [[0 for x in range(max_price_in_cents + 1)] for x in range(len(actions) + 1)]
  
  for i in range(1, len(actions) + 1):
    for w in range(1, max_price_in_cents + 1):
      if actions[i-1][1] <= w:

        matrice[i][w] = max(actions[i-1][2] + matrice[i-1][w - actions[i-1][1]], matrice[i-1][w])
      else:
        matrice[i][w] = matrice[i-1][w]
        
  w = max_price_in_cents
  n = len(actions)
  selected_actions = []
  
  while w >= 0 and n >= 0:
    e = actions[n-1]
    if matrice[n][w] == matrice[n-1][w - e[1]] + e[2]:
      selected_actions.append(e[0])
      w -= e[1]
    n -= 1
    
  execution_delay = time.time() - start_time
  
  print(f"Le meilleur bénéfice obtenu est de {round(matrice[-1][-1] / 100, 2)} €, avec les actions suivantes : {selected_actions} ! Le montant total dépensé est de {(max_price_in_cents - w) / 100} €.")
  print(f"Délai d'exécution: {execution_delay} secondes ")

#optimized(500, csv_data_reader("data/dataset1_Python_P7.csv"))
#optimized(500, csv_data_reader("data/dataset2_Python_P7.csv"))
optimized(500, csv_data_reader("data/twenty_actions.csv"))