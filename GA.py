import copy 
import random



def get_fitnessValue(node) :
  return 2*node*node + 1 #2x^2+1


#tournament selection  
def selection_operator(curr_population) :
        parents = []
        maxi = 0
        
        for k_population in range(2) :
            k_population = []
            for j in range(3) :
              k_population.append(random.choice(curr_population))
            for j in range(len(k_population)) :
                if get_fitnessValue(k_population[maxi]) < get_fitnessValue(k_population[j]) :
                  maxi = j
            parents.append(k_population[maxi])
        return parents
  
 
#crossover probability = 1/2  and the method is arithemetic crossover
def get_successors_bycrossover(node1,node2) :
     beta = random.uniform(0,1)
     random_number = random.uniform(0,1)
     if random_number <=1/2 :
        return (1-beta)*node1 + beta*node2
     return node1
     
     
 # mutation probability = 1 and the method is random resetting 
def apply_mutation(node) :
    random_number = random.uniform(0,1)
    if random_number <=1 :
       return random.uniform(0,6)
    return node




curr_population = []
 
for i in range(5) :
    curr_population.append(random.uniform(0,6))

total_nodes = 0    
for i in range(1000) :
    max_node = 0
    curr_population_fitness = []
    for j in curr_population :
        curr_population_fitness.append(get_fitnessValue(j))
        max_node = max(max_node,j)
        print("node = ",j)
        print("fitness_value = ",get_fitnessValue(j))
    print("")
    print("")
    total_nodes+=len(curr_population)
    flag = True
    for j in range(len(curr_population_fitness)) :
        if j and curr_population_fitness[j-1]!=curr_population_fitness[j] :
           flag = False
    if flag==True :
        break
    # Elitism
    next_genaration = []
    next_genaration.append(max_node)
    for i in range(2) :
        parents = selection_operator(curr_population)
        next_genaration.append(get_successors_bycrossover(parents[0],parents[1]))
        next_genaration.append(get_successors_bycrossover(parents[1],parents[0]))
    curr_population = next_genaration.copy()   
print("total number of nodes generated =",total_nodes)