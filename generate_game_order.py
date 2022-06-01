
import random

game_name = [ "Foot", "Basket", "Volley" ] 

i=1
while len(game_name) > 0:
	print(i, ". ", game_name.pop(random.randrange(len(game_name))))
	i+=1
