#
# This file runs the processes
#

from random import randint
from random import choice
# import sys
import threading
import os
import logging
import multiprocessing

# sys.setrecursionlimit(4000)

class Experiment:
    def __init__(self):
        self.nodes_sent = []
        self.nodes_sent_2 = {}

    def process1(self, t):
        return randint(0, len(t)-1)

    def process2(self, t):
        unsent = [x for x in range(0, len(t)) if x not in self.nodes_sent]
        i = choice(unsent)
        self.nodes_sent.append(i)
        return i        

    def process3(self, t):
        unmarked = [x for x in range(0, len(t)) if t[x] == 0]
        i = choice(unmarked)
        return i

    def climbUp(self, t, i):
        if i == 0:
            self.climbDown(t, 2*i+1)
            self.climbDown(t, 2*i+2)
        else:
            self.perfromMarkingRules(t, i)
            self.climbUp(t, (i-1)//2)

    def climbDown(self, t, i):
        self.perfromMarkingRules(t, i)
        if 2*i+2 < len(t):
            self.climbDown(t, 2*i+1)
            self.climbDown(t, 2*i+2)

    def perfromMarkingRules(self, t, i):
        # Check if current node is marked
        if i == 0: return
        if t[i] == 1:
            # Check if current node is a left or right sibling
            if i % 2 == 0:
                # Check if left sibling is marked
                if t[i-1] == 1:
                    # Mark parent node
                    t[(i-1)//2] = 1
                    return
            else:
                # Check if right sibling is marked
                if t[i+1] == 1:
                    # Mark parent node
                    t[(i-1)//2] = 1
                    return

            # Check if parent is marked
            if t[(i-1)//2] == 1:
                # Check if current node is a left or right sibling
                if i % 2 == 0:
                    # Mark left sibling
                    t[i-1] = 1
                    return
                else:
                    # Mark right sibling
                    t[i+1] = 1
                    return

    def mark(self, t, i):
        if t[i] == 1: return
        t[i] = 1
        self.perfromMarkingRules(t, i)
        self.climbUp(t, i if i==0 else (i-1)//2)

def runTrial(p, trial, n):
    e = Experiment()
    if p == '1': process = e.process1
    if p == '2': process = e.process2
    if p == '3': process = e.process3
    N = 2**n - 1
    binary_tree = [0]*(N)
    steps = 0
    while 0 in binary_tree:
        steps += 1
        i = process(binary_tree)
        e.mark(binary_tree, i)
    with open(f'results_{p}_{trial}_{n}.txt', 'w') as file_object:
            file_object.write(f'{steps}')

def run_p(p):
    for trial in range(0, 10):
        for n in range(10, 21):
            t = multiprocessing.Process(target=runTrial, name=f'=process_{p}_trial_{trial}_n_{n}', args=(p, trial, n,))
            t.start()
    
if __name__ == '__main__':
    run_p('1')
    run_p('2')
    run_p('3')