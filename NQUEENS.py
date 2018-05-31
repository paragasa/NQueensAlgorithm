#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:32:17 2018

@author: paragasa
"""
#imports
import random

fitGoal = 0

def fitness(individual):
#    print(individual)
    horizontalHits = 0
    diagonalHits = 0
    horizontalHits = sum(individual.count(q)-1 for q in individual)/2
    #create vertical board VISUALIZATION
#    gene = len(individual)
#    print("-----------------------")
#    qstring= ""
#    for x in individual:
#        for z in range(1,gene+1):
#            if(x == z ):
#                qstring+=" Q "
#                
#            else:
#                qstring+=" . "
#        print(qstring + "\n")
#        qstring=""
#    print("-----------------------")
#    cb = enumerate(individual)
#    for i, column in cb:
#         for j, diagonal in cb:
#             diff = abs(i-j)
#             if diagonal + diff == column or diagonal - diff == column:
#                diagonalHits += 1
    for i in range(0,len(individual)-1):
        for j in range(0,i):
            if(individual[i] + (i-j) == individual[j]):
                diagonalHits += 1
            if(individual[i] - (i -j) == individual[j]):
                diagonalHits+= 1
        for j in range(i+1,len(individual)-1):
            if(individual[i] + (i- j) == individual[j]):
                diagonalHits += 1
            if(individual[i] - (i -j) == individual[j]):
                diagonalHits += 1
              
    diagonalHits /=2   
    fit = (int(fitGoal - (horizontalHits + diagonalHits)))
    return fit
   

def populate(n):
    arr = []
    for i in range(500): #change for population size
        arr.append(encode(n))
    return arr
        
#encode
def encode(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1,n))
    return arr
    
# crossover
def crossover(childOne, childTwo):
    genes = len(childOne)
    selection = random.randint(0, genes - 1)
    newchild = childOne[0:selection] + childTwo[selection:genes]
    return newchild

#mutation
def mutate(child):
    genes = len(child)
    chromosome = random.randint(0, genes - 1)
    mutation = random.randint(1,genes)
    child[chromosome]= mutation
    return child

def randomSelection(population, probabilities):
    Probs = zip(population, probabilities)
    sumProb = sum(prob for pop, prob in Probs)
    pick = random.uniform(0,sumProb)    
    #prob counters
    #counter = 0
    probOfSelection = 0
    for k,j in zip(population,probabilities):
        if (j + probOfSelection >= pick):
            return k #population[counter]
        probOfSelection += j 
#        if (counter < 99):
#            counter += 1
            
#fitness function
    
def probability(individual):
    return fitness(individual)/ fitGoal
    
def geneticAlg(population):
    #input: population, set of ind
    #FITNESS-FN measure fitness of ind
    #mutation rate
    
      #repeat
        #new_population 
        #for i =1 to size of pop do
            #x random,fit
            #y random,fit
            #child reproduce (x,y)
            #if(random prob) then child mutate
            #add child to new pop
        #population = new_population
    #until fit ind is fit, or time elapse
    #return best ind
    #CHANGE FOR MUTATION RATE
    probabilityMut= 0.1 
    retpopulation = []
    
    for n in queens:
        prob = probability(n)
        probabilities.append(prob)
    
    for i in range(len(population)):
        #parent
        x = randomSelection(population, probabilities)
        y = randomSelection(population, probabilities)
        #generate child
        child = crossover(x,y)
        #mutation
        if( random.uniform(0,1) < probabilityMut):
            child= mutate(child)
        #attach child 
        retpopulation.append(child)
        #check if child fits goal
        if(fitness(child) == fitGoal):
            break;
    return retpopulation

#_________________________________MAIN______________________
#variation of population samples
NumQueens = 8 #CHANGE FOR 4,8,16 QUEENS
queens = populate(NumQueens)
for k in range(NumQueens):
    fitGoal += k
 
probabilities = []
#show number of iterations to converge
iteration = 1    

isFitReached = False
while(isFitReached != True):
    maxFit= 0
    avgFit = 0
    print("Iteration = {}".format(iteration))
    queens = geneticAlg(queens)
#    print("Queens:")
    for i in queens:
        avgFit += fitness(i)
        #print("{}".format(i))
        if(fitness(i) == fitGoal):
            #print("Max Fitness at iteration {} = {}".format(iteration,fitGoal))
            isFitReached = True
            print (i)
        if(fitness(i)> maxFit):
            #print (i)
            maxFit = fitness(i)
    avgFit /= len(queens)
    iteration += 1
    print("Top Fitness for iteration {} = {}".format(iteration, maxFit))
    print("Average Fitness for iteration {} = {}".format(iteration, avgFit))
print("Iteration completes at {}".format(iteration))


#results

#average value of fitness func of chromoes in population each iteration
#final solution

