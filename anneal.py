#! /usr/bin/env python3
from math import exp
from random import random
from random import randint

class Anneal():
    '''
        A basic implementation of simulated annealing
    '''
    def __init__(self, costFunction, initalState, maxCycles, minT, maxT, limits, alpha):
        self.costF = costFunction 
        self.xInital = initalState
        self.xN = len(xInital)
        self.damping = damping
        self.maxCycles = maxCycles
        self.minT = minT
        self.temp = maxT
        self.maxT = maxT
        self.limits = limits[:] #shallow copy of limits 
        self.state = inital_state
        self.energy = self.costF(self.xInital)
        self.lowState = self.state
        self.lowEnergy = self.energy_level
        self.cycle = 1
        self.accepted = 0
        self.alpha = alpha
    '''
    Apply cooling factor to process - We are using linear multiplicitive cooling here.
    The new cycle temperature is found by multiplying the inital temperature by a factor that is
    inversely proportional to the temperature cycle we are in.
    '''
    def cool(self):
        self.temp = self.maxT / 1 + self.alpha * self.cycle

    ''' 
    Always accept the neighbor if it is better than current state
    Accept with probability of exp(-abs(energy delta) / current temperature) if not.
    '''
    def nAccept(self, neighbor):
        neighborEnergy = self.costF(neighbor)
        if neighborEnergy < self.energy:
            self.energy, self.state = neighborEnergy, neighbor
            if neighborEnergy < self.lowEnergy:
                self.lowEnergy, self.lowState = neighborEnergy, neighbor
        else:
            dE = neighborEnergy - self.energy
            pNaccept = exp(-abs(dE) / self.temp)
            if random() < pNaccept:
                self.energy, self.state = neighborEnergy, neighbor

    ''' 
    Start the simulated annealing process
    For each cycle:
      swap two random nodes
      check for acceptance
      adjust the temperature
    Stop when minT or maxCycle is reached
    Result will be in self.lowState with the distance for that state in self.lowEnergy
    '''
    def start(self):
        while minT < self.temp and self.cycle < self.maxCycle:
            neighbor = self.state[:] #shallow copy of state
            n1 = randint(0, self.xN-1)
            n2 = randint(0, self.xN-1)
            neighbor[n1], neighbor[n2] = neighbor[n2], neighbor[n1]
            self.nAccept(neighbor)
            self.cool()
            self.cycle += 1




        