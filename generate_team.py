
import random

members = [ "Samuel", "Thomas", "Thibault", "Cedric", "Gael", "Benjamin", "Nicolas LDP", "Nicolas Labro", "Dieter", "Lucas", "mael" ] 

team = []
i=1
while len(members) > 0:
	team.append(members.pop(random.randrange(len(members))))
	if len(team) == 2:
		print("Team ", i, str(team))
		team = []
		i+=1

