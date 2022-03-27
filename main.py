import random
import math
import timeit
from wsgiref import headers
from tabulate import tabulate

start = timeit.default_timer()

with open('wordlist.txt', 'r') as f:
    allwords = [line.strip() for line in f]
		# filter out words with letter multiples

def filterList(list):
    result = []
    for w in list:
        letters = []
        for l in w:
            if not l in letters:
                letters.append(l)
        if len(letters) == 5:
            result.append(w)
    return result
    
wordlist = filterList(allwords)

with open('letterFreq.txt', 'r') as f:
    letterFreq = [line.strip() for line in f]

#  genetic representation of a solution 
#  4 integer values between 0 and 8246 (number of words)

sample = [7449, 8058, 2376, 1027]

#  funtion to generate new solutions 

def randomSolution():
    array = []
    for i in range(4):
        array.append(random.randint(0, len(wordlist) - 1))
    return array

#  fitness function 

def fitness(solution):
    words = []
    letters = []
    for i in solution:
        words.append(wordlist[i])
    for w in words:
        for l in w:
            if not l in letters:
                letters.append(l)
    avgFreq = 0
    for i in letters:
        avgFreq = avgFreq + (26 - letterFreq.index(i))
    avgFreq = avgFreq * (1/702)
    # value = (1/26 * len(letters)) * (2 * avgFreq)
    value = (1/6 * len(letters)) * (2 * avgFreq)
    return value        

#  selection function 
def selection(generation):
    select = []
    fitnesses = []
    currentMax = 0
    for i in generation:
        fitnesses.append(fitness(i))
    for i in fitnesses:
        if currentMax == max(fitnesses):
            fitnesses[fitnesses.index(currentMax)] = 0
        currentMax = max(fitnesses)
        select.append(generation[fitnesses.index(currentMax)])
        fitnesses[fitnesses.index(currentMax)] = 0
    n = 80
    del select[-n:]
    return select

#  crossover function 
def crossover(s1, s2):
    result = []
    maxFitness = 0
    for l1 in s1:
        for l2 in s1:
            for l3 in s2:
                for l4 in s2:
                    sampleRes = [l1, l2, l3, l4]
                    if fitness(sampleRes) > maxFitness:
                        result = sampleRes
                        maxFitness = fitness(sampleRes)
    return result
			
#  mutation function
def mutation(solution):
    solution[random.randint(0, len(solution)-1)] = random.randint(0, len(wordlist)-1)
    return solution

def letterNo(solution):
    words = []
    letters = []
    for i in solution:
        words.append(wordlist[i])
    for w in words:
        for l in w:
            if not l in letters:
                letters.append(l)
    return len(letters)

# simulation

currentGeneration = []
nextGeneration = []
# first generation
for i in range(100):
    nextGeneration.append(randomSolution())

parents = []

for g in range(1000): # no. of generations
    currentGeneration = []
    currentGeneration.extend(nextGeneration)
    parents = selection(currentGeneration)
    nextGeneration = []

    generationRoot = []
    generationRoot.extend(parents)
    del generationRoot[-math.floor(len(parents)/2):]
    
    # for i in range(math.floor(len(parents)/2)):
    #     generationRoot.append(crossover(parents[i*2-1], parents[i*2]))

    for i in range(2):
        for p1 in parents:
            generationRoot.append(crossover(p1, parents[random.randint(0, len(parents)-1)]))

    nextGeneration.extend(generationRoot)

    # for n in range(4):
    #     for i in generationRoot:
    #         nextGeneration.append(mutation(i))

    while len(nextGeneration) < 101 - 15:
        nextGeneration.append(mutation(generationRoot[random.randint(0, len(generationRoot)-1)]))
    
    for i in range(15):
        nextGeneration.append(randomSolution())


result = selection(nextGeneration)
output = []
for i in result:
    resultWords = []
    for w in i:
        resultWords.append(wordlist[w])
    # print(i, "     ", fitness(i), "     ", resultWords, "     ", letterNo(i))
    output.append([i, fitness(i), resultWords, letterNo(i)])

print(tabulate(output, headers=["Index", "Fitness", "Words", "Letters"]))

stop = timeit.default_timer()

print('------------------------\nExecution Time: ', stop - start)