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
  
optimized(500, actions)