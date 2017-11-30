import random 
import matplotlib.pyplot
import datetime

#create a function that calculates the distance between two agents
def distance_between(agent0, agent1):     
    return(((agent0[0]-agent1[0])**2)+((agent0[1]-agent1[1])**2))**0.5

#create a function that will time how long it takes to calcualte distance for 
# different orders of magnitude of agent numbers
def getTimeMS():
    dt = datetime.datetime.now()
    return dt.microsecond + (dt.second * 1000000) + \
    (dt.minute * 1000000 * 60) + (dt.hour * 1000000 * 60 * 60)


#dictate the number of agents and initial iterations
num_of_agents = 10
num_of_iterations = 100
#create an empty list for the agents, distances and run times
agents = []
distance_list = []
run_time_list = []
run_times = []


#assign each agent a randomly generated starting location
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])


#make the agents move randomly around
for i in range(num_of_iterations):    
    for i in range(num_of_agents):    
        if random.random() < 0.5:
            agents[i][0] += 1 % 99    
        else:
            agents[i][0] -= 1 % 99
        
        if random.random() > 0.5:
            agents[i][1] += 1 % 99
        else:
            agents[i][1] -= 1 % 99

#time how long it takes to calculate all the distances for the different 
# numbers of iterations
while (num_of_iterations <= 1000000000):
   
    start = getTimeMS()
    
    #append all distances generated into the empty distance list, ensuring 
    # that agents are not being tested against themselves
    for agent0 in agents:
        for agent1 in agents:
            if agent0 != agent1:   
                distance = distance_between(agent0, agent1)     
                distance_list.append([distance])    
       
    #record end time for timing function         
    end = getTimeMS()
    
    #calculate run time and make it an integer
    run_time_int = int(end-start)
    run_times.append(run_time_int)
    #save the run time figures to the empty list with corresponding number of 
    # iterations
    run_time_list.append([num_of_iterations,run_time_int])

    num_of_iterations = num_of_iterations * 10


#can calculate the maximum and minimum distances between agents
print(min(distance_list))
print(max(distance_list))


#plot scatter graph of iterations vs run time
matplotlib.pyplot.xlim(100,1000000000)
matplotlib.pyplot.ylim((min(run_times)-10),(max(run_times)+10))
matplotlib.pyplot.xlabel('No. of iterations')
matplotlib.pyplot.ylabel('Run time (microseconds)')
matplotlib.pyplot.xscale('log')   #makes the x axis logarithmic
for i in range(len(run_time_list)):
    matplotlib.pyplot.scatter(run_time_list[i][0],run_time_list[i][1])
matplotlib.pyplot.show()