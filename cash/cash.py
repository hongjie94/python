from cs50 import get_float

while True:
    d = get_float("Change owed: ")
    if d >= 0.00:
        break
    
cents = round(d*100)
coins = 0

while (cents >= 25):
    cents -= 25
    coins += 1
    
while (cents >= 10):
    cents -= 10
    coins += 1
    
while (cents >= 5):
    cents -= 5
    coins += 1
    
while (cents >= 1):
    cents -= 1
    coins += 1

print(coins)