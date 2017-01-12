import random

def user_agent():
	f = open("user_agent.txt")
	agent_list=[]
	[agent_list.append(line) for line in f]
	return agent_list[random.randint(0,agent_list.__len__())]