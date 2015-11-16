import genome

#import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

NoneType = type(None)

pset = gp.PrimitiveSetTyped("main", [], NoneType)

#logical
pset.addPrimitive(genome.Or, [bool, bool, NoneType], NoneType)
pset.addPrimitive(genome.And, [bool, bool, NoneType], NoneType)
pset.addPrimitive(genome.Not, [bool, NoneType], NoneType)
pset.addPrimitive(genome.If_Then, [bool, NoneType], NoneType)

#actions
pset.addTerminal(genome.TurnGunToEnemy, NoneType)
pset.addTerminal(genome.TurnGunLeft5, NoneType)
pset.addTerminal(genome.TurnGunLeft10, NoneType)
pset.addTerminal(genome.TurnGunRight5, NoneType)
pset.addTerminal(genome.TurnGunRight10, NoneType)
pset.addTerminal(genome.Fire1, NoneType)
pset.addTerminal(genome.Fire2, NoneType)
pset.addTerminal(genome.Fire3, NoneType)

#tests
pset.addTerminal(genome.TestEnemyEnergy, bool)
pset.addTerminal(genome.TestEnemyEnergy0, bool)
pset.addTerminal(genome.TestEnemyEnergyBelow10, bool)
pset.addTerminal(genome.TestEnergyBelow10, bool)
pset.addTerminal(genome.TestEnergyGreaterThanEnemys, bool)
pset.addTerminal(genome.TestEnergyLessThanEnemys, bool)
pset.addTerminal(genome.TestEnemyWithin10Ticks, bool)
pset.addTerminal(genome.TestEnemyWithin20Ticks, bool)
pset.addTerminal(genome.TestEnemyWithin50Ticks, bool)
pset.addTerminal(genome.TestGunIsHot, bool)
pset.addTerminal(genome.TestGunWithin5Ticks, bool)
pset.addTerminal(genome.TestTurnToEnemyWithin10Ticks, bool)
pset.addTerminal(genome.TestTurnToEnemyWithin5TIcks, bool)

#begin genetic programming
#initialize population
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin, pset=pset)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genFull, pset=pset, min_=1, max_=3)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalRobot(individual):
    # Transform the tree expression in a callable function
    #func = toolbox.compile(expr=individual)
    print("eval!")
    result = 0 #call robocode
    return result

#genetic parameters
toolbox.register("evaluate", evalRobot)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

#random.seed(10)
pop = toolbox.population(n=100)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
#stats.register("avg", numpy.mean)
#stats.register("std", numpy.std)
#stats.register("min", numpy.min)
#stats.register("max", numpy.max)

algorithms.eaSimple(pop, toolbox, 0.5, 0.2, 40, stats, halloffame=hof)