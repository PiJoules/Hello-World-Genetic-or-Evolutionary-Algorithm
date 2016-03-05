#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://www.reddit.com/r/dailyprogrammer/comments/40rs67/20160113_challenge_249_intermediate_hello_world/
"""

from __future__ import print_function

from random import choice, random, randint
from string import printable


def rand_str(length):
    """Generate a random printable string."""
    return "".join(choice(printable) for i in xrange(length))


class Individual(object):
    """Individual of a population."""

    def __init__(self, goal, data=None):
        self.__goal = goal
        self.__data = data or rand_str(len(goal))

    @property
    def fitness(self):
        """Fitness of an individual."""
        return sum(c1 != c2 for c1, c2 in zip(self.__goal, self.__data))

    def __str__(self):
        return self.__data

    def mutate(self, rate):
        data = self.__data
        i = randint(0, len(data) - 1)
        self.__data = data[:i] + choice(printable) + data[i+1:]

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return not(self.data == other.data)

    def __sub__(self, other):
        return sum(c1 != c2 for c1, c2 in zip(self.__data, other.data))

    @property
    def data(self):
        return self.__data

    @property
    def goal(self):
        return self.__goal

    def breed(self, other):
        half = len(self.__data) / 2
        data = self.__data[:half] + other.data[half:]
        return Individual(self.goal, data=data)


class Population(object):
    """Population of individuals (strings)."""

    def __init__(self, individuals, goal):
        self.__individuals = individuals
        self.__goal = goal

    @classmethod
    def random(cls, pop_size, goal):
        """Create a population of random individuals."""
        return Population([Individual(goal) for i in xrange(pop_size)], goal)

    def __iter__(self):
        for individual in self.__individuals:
            yield individual

    def __len__(self):
        return len(self.__individuals)

    @property
    def diversity(self):
        base = self.__individuals[0]
        return sum(x - base for x in self.__individuals)

    def evolve(self, retain=0.2, rand_select=0.05, mutate=0.05, rate=0.05):
        individuals = self.__individuals

        retain_count = int(len(individuals) * retain)
        if retain_count < 2:
            raise RuntimeError(
                "There must be at least 2 retained individuals in the"
                "population to breed.")
        sorted_pop = sorted(individuals, key=lambda x: x.fitness)
        parents = sorted_pop[:retain_count]
        ignored = sorted_pop[retain_count:]

        # Randomly add others to promote diversity
        parents += filter(lambda x: random() < rand_select, ignored)

        # Breed between parents to create children until the previous
        # population size is reached.
        children = []
        shortage = len(individuals) - len(parents)
        while len(children) < shortage:
            male = choice(parents)
            female = choice(parents)
            if male != female:
                children.append(male.breed(female))

        # Mutate some people
        next_gen = parents + children
        for individual in next_gen:
            if random() < mutate:
                individual.mutate(rate)

        self.__individuals = next_gen

    @property
    def best_individual(self):
        return min(self.__individuals, key=lambda x: x.fitness)

    @property
    def met_goal(self):
        return self.best_individual.data == self.__goal


def generations(goal, runs, pop_size=100, retain=0.2, rand_select=0.05,
                mutate=0.05, rate=0.05):
    """Yield generations until the goal is reached by an individual."""
    generation = Population.random(pop_size, goal)
    for i in xrange(runs):
        yield generation
        if generation.met_goal:
            break
        generation.evolve(retain=retain, rand_select=rand_select,
                          mutate=mutate)

