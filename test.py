#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from genetic import generations


def main():
    string = "Hello, world!"
    i = 1
    for gen in generations(string, 1000, pop_size=100,
                           mutate=0.7, rate=0.1):
        best = gen.best_individual
        print("Gen: {}  \t| Fitness: {}\t| {} | {}"
              .format(i, best.fitness, best, gen.diversity))
        i += 1


if __name__ == "__main__":
    main()

