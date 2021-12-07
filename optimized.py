from data_reader.csv_data_reader import csv_data_reader

def optimized(capacity, actions):
  
  for index, action in enumerate(actions):
      action = (action[0], action[1], action[1] * action[2] / 100)
      actions[index] = action
    
  matrice = [[0 for x in range(capacity + 1)] for x in range(len(actions) + 1)]
  
  for i in range(1, len(actions) + 1):
    for w in range(1, capacity + 1):
      if actions[i-1][1] <= w:
        matrice[i][w] = max(actions[i-1][2] + matrice[i-1][w - actions[i-1][1]], matrice[i-1][w])
      else:
        matrice[i][w] = matrice[i-1][w]
        
  w = capacity
  n = len(actions)
  selected_actions = []
  
  while w >= 0 and n >= 0:
    e = actions[n-1]
    if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
      selected_actions.append(e)
      w -= e[1]
    n -= 1
    
  print(round(matrice[-1][-1], 2), selected_actions)
  
optimized(500, csv_data_reader("data/twenty_actions.csv"))