import random

def play (strategy_limit).

total = 0

while total < strategy_limit:

Card = random, ran dint (1, 10)

total += card

if total >21:

return 0

return total

def simulate_games (num_games = 10000):

Strategies = {
"Aggressive (>=18)":18,

"Safe (>=215) ": 15,

"very sate (>=12): 12

}
results= {s:o for s in strategies}

for in range (num_games):

scores = {5: Play(limit) for s, limit in strategies.

items( ) }

winner = max (scores ,key =scores.get)

if Scores [winner]!=0:

results [winner]+=1

for s in results:

results [s]= round (results [s] /num_games) * 100,2)

return results

winning_percentage = simulate_games()

print("winning strategy Analysis (out of 10,000 rounds):")

for strategy.win_rate in winning_percentages. items():

Print (f" {strategy} :{win-rate} % wins")
