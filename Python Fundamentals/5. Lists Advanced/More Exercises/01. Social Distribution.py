population = [int(n) for n in input().split(", ")]
minimum_wealth = int(input())

if sum(population) < minimum_wealth * len(population):
    print("No equal distribution possible")
else:

    poorest = population.index(min(population))
    richest = len(population) - 1

    while population[poorest] < minimum_wealth:

        needed = minimum_wealth - population[poorest]

        population[poorest] += needed
        population[richest] -= needed

        poorest = population.index(min(population))
        richest = population.index(max(population))

    print(population)


