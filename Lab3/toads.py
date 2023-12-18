# -*- coding: utf-8 -*-
"""



"""
'''
getPopulation(n):
    Initialize an empty list to store the toads
    For i = 1 to n:
        Create a new Toad object with a random is_trustworthy value
        Add the Toad object to the list
    Return the list of toads

TruthFulToadsA(population):
    Initialize an empty list to store the indices of trustworthy toads
    For each pair of toads (i, j) in population:
        If both toads i and j trust each other:
            Add the indices i and j to the list
    Return the list of indices of trustworthy toads
'''
import random

class Toad:
    def __init__(self, is_trustworthy):
        self.truthful = bool(int(is_trustworthy))
    
    def is_trustworthy(self):
        return self.truthful
    
    def tell_about(self, toad):
        b_trustworthy = toad.is_trustworthy()
        if self.is_trustworthy():
            return b_trustworthy
        else:
            r = random.random()
            if r < 0.5:
                return True
            else:
                return False

def getPopulation(n):
    toads = []
    for i in range(n):
        is_trustworthy = random.choice([0, 1])  # Randomly assign whether the toad is trustworthy
        toads.append(Toad(is_trustworthy))
    return toads

def TruthFulToadsA(population):
    trustworthy_toads = []
    n = len(population)
    
    for i in range(n):
        for j in range(i+1, n):
            if population[i].tell_about(population[j]) and population[j].tell_about(population[i]):
                trustworthy_toads.extend([i+1, j+1])  # Adding 1 to make indices 1-based
    
    return list(set(trustworthy_toads))

# Example usage
population = getPopulation(5)
trustworthy_indices = TruthFulToadsA(population)
print("Indices of trustworthy toads (Algorithm A):", trustworthy_indices)

'''
# pseudo code
TruthFulToadsB(population):
    Initialize an empty list to store the indices of trustworthy toads
    Initialize a new list to store the reduced population
    n = length of population
    
    For i = 1 to n (incrementing by 2):
        If both toads i and i+1 are trustworthy:
            Add both indices i and i+1 to the list of trustworthy toads
        Else:
            Randomly choose one of the toads and add its index to the list
    Return the list of indices of trustworthy toads

'''

def TruthFulToadsB(population):
    trustworthy_toads = []
    reduced_population = []
    n = len(population)
    
    for i in range(0, n, 2):
        # Compare trustworthiness of toads i and i+1
        if population[i].tell_about(population[i+1]) and population[i+1].tell_about(population[i]):
            trustworthy_toads.extend([i+1, i+2])  
        else:
            random_toad = random.choice([i+1, i+2])
            reduced_population.append(population[random_toad-1])  # Adding 1 to make indices 1-based
    
    return list(set(trustworthy_toads)), reduced_population

#Usage Example 
population = getPopulation(6)
trustworthy_indices, new_population = TruthFulToadsB(population)
print("Indices of trustworthy toads (Algorithm B):", trustworthy_indices)
print("Reduced Population:", len(new_population))

'''
# pseudo Code
TruthFulToadsC(population):
    Initialize an empty list to store the indices of trustworthy toads
    Initialize a new list to store the reduced population
    n = length of population
    
    For i = 1 to n-1 (incrementing by 2):
        If both toads i and i+1 are trustworthy:
            Add both indices i and i+1 to the list of trustworthy toads
        Else:
            Randomly choose one of the toads and add its index to the list
    
    # Handle the last toad for odd n
    If n is odd:
        Randomly choose whether to consider the last toad trustworthy
    Return the list of indices of trustworthy toads

'''

def TruthFulToadsC(population):
    trustworthy_toads = []
    n = len(population)
    
    for i in range(0, n-1, 2):
        # Compare trustworthiness of toads i and i+1
        if population[i].tell_about(population[i+1]) and population[i+1].tell_about(population[i]):
            trustworthy_toads.extend([i+1, i+2])  # Adding 1 to make indices 1-based
        else:
            random_toad = random.choice([i+1, i+2])
            trustworthy_toads.append(random_toad)  # Adding 1 to make indices 1-based
    
    # Handle the last toad for odd n
    if n % 2 == 1:
        random_toad = random.randint(1, n)
        trustworthy_toads.append(random_toad)  # Adding 1 to make indices 1-based
    
    return list(set(trustworthy_toads))

# Example usage
population = getPopulation(7)
trustworthy_indices = TruthFulToadsC(population)
print("Indices of trustworthy toads (Algorithm C):", trustworthy_indices)

'''
#pseudo code
FindTrustworthyToad(population):
    If the population size is 1:
        Return the only toad in the population as the trustworthy toad
    
    # Reduce the population size using the procedure from part (b) or (c)
    trustworthy_toads, reduced_population = TruthFulToadsB(population)  # For even n
    # trustworthy_toads, reduced_population = TruthFulToadsC(population)  # For odd n
    
    # Recur on the reduced population until a trustworthy toad is found
    return FindTrustworthyToad(reduced_population)

'''

def FindTrustworthyToad(population):
    if len(population) == 1:
        return population[0]
    else:
        trustworthy_toads, reduced_population = TruthFulToadsB(population)  # For even n
    # trustworthy_toads, reduced_population = TruthFulToadsC(population)  # For odd n
    
    return FindTrustworthyToad(reduced_population)

# Example usage
population = getPopulation(8)
trustworthy_toad = FindTrustworthyToad(population)
print("Index of a trustworthy toad (Recursive Algorithm):", population.index(trustworthy_toad) + 1)  # Adding 1 to make indices 1-based

'''
#pseudo code
FindAllTrustworthyToads(population):
    Initialize an empty list to store the indices of trustworthy toads
    FindTrustworthyToadRecursive(population, trustworthy_toads_list)
    Return the list of indices of trustworthy toads

FindTrustworthyToadRecursive(population, trustworthy_toads_list):
    If the population size is 1:
        Return the only toad in the population as the trustworthy toad
    
    # Reduce the population size using the procedure from part (b) or (c)
    trustworthy_toads, reduced_population = TruthFulToadsB(population)  # For even n
    # trustworthy_toads, reduced_population = TruthFulToadsC(population)  # For odd n
    
    # Recur on the reduced population to find a trustworthy toad
    trustworthy_toad = FindTrustworthyToadRecursive(reduced_population, trustworthy_toads_list)
    
    # If the found trustworthy toad has a group of trustworthy toads, add them to the list
    if trustworthy_toad in trustworthy_toads:
        trustworthy_toads_list.extend(trustworthy_toads)
    
    return trustworthy_toad

'''

def FindAllTrustworthyToads(population):
    trustworthy_toads_list = []
    FindTrustworthyToadRecursive(population, trustworthy_toads_list)
    return list(set(trustworthy_toads_list))

def FindTrustworthyToadRecursive(population, trustworthy_toads_list):
    if len(population) == 1:
        return [population[0]]
    
    trustworthy_toads, reduced_population = TruthFulToadsB(population)  # For even n
    # trustworthy_toads, reduced_population = TruthFulToadsC(population)  # For odd n
    
    trustworthy_toad = FindTrustworthyToadRecursive(reduced_population, trustworthy_toads_list)
    
    if trustworthy_toad in trustworthy_toads:
        trustworthy_toads_list.extend(trustworthy_toads)
    
    return trustworthy_toad

# Example usage
population = getPopulation(10)
trustworthy_indices = FindAllTrustworthyToads(population)
print("Indices of trustworthy toads (Procedure to find all trustworthy toads):", trustworthy_indices)
