from random import randint
from random import choice
# from queue import LifoQueue
# import sys
import threading
import os
import logging

# sys.setrecursionlimit(4000)

PRINT_FLAG = False

class Experiment:
    def __init__(self):
        self.nodes_sent = []
        self.nodes_sent_2 = {}

    def process1(self, t):
        logging.info('here_p')
        return randint(0, len(t)-1)

    def process2(self, t):
        # if len(self.nodes_sent) == len(t):
        #     print('P2: All nodes have been sent')
        #     return -1
        unsent = [x for x in range(0, len(t)) if x not in self.nodes_sent]
        i = choice(unsent)
        self.nodes_sent.append(i)
        return i        

    def process3(self, t):
        # if not 0 in t:
        #     print('P3: All nodes have been marked')
        #     return -1
        unmarked = [x for x in range(0, len(t)) if t[x] == 0]
        i = choice(unmarked)
        return i

    def climbUp(self, t, i):
        if i == 0:
            self.climbDown(t, 2*i+1)
            self.climbDown(t, 2*i+2)
            # self.climbDown2(t, i)
        else:
            self.perfromMarkingRules(t, i)
            if PRINT_FLAG: print(f'U: {t}')
            self.climbUp(t, (i-1)//2)

    def climbDown(self, t, i):
        self.perfromMarkingRules(t, i)
        if PRINT_FLAG: print(f'D: {t}')
        if 2*i+2 < len(t):
            self.climbDown(t, 2*i+1)
            self.climbDown(t, 2*i+2)

    # def climbDown2(self, t, i):
    #     stack = LifoQueue(maxsize=len(t))
    #     stack.put(i)
    #     while not stack.empty():
    #         current = stack.get()
    #         self.perfromMarkingRules(t, current)
    #         if 2*current+2 < len(t):
    #             stack.put(2*current+1)
    #             stack.put(2*current+2)

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
        logging.info('here_m')
        if PRINT_FLAG: print('==================================================')
        if PRINT_FLAG: print(f'M: {t}')
        self.perfromMarkingRules(t, i)
        if PRINT_FLAG: print(f'N: {t}')
        self.climbUp(t, i if i==0 else (i-1)//2)

    # def run(self, process, p):
    #     for trial in range(0, 10):
    #         print(f'    TRIAL {trial}')
    #         for n in range(10, 21):
    #         # for n in range(10, 13):#21):
    #             # print(f'        FOR n = {n}')
    #             # if process == e.process2: self.nodes_sent = []
    #             # N = 2**n - 1
    #             # binary_tree = [0]*(N)
    #             # steps = 0
    #             # while 0 in binary_tree:
    #             #     steps += 1
    #             #     i = process(binary_tree)
    #             #     self.mark(binary_tree, i)
    #             # print(f'            STEPS: {steps}')
    #             t = threading.Thread(target=self.runInThread, name=f'=process_{p}_trial_{trial}_n_{n}', args=(self, p,trial,n,))
    #             t.daemon = True
    #             t.start()
    
    # def runInThread(self, process, p, trial, n):
    #     # print(f'        FOR n = {n}')
    #     if process == e.process2: self.nodes_sent = []
    #     N = 2**n - 1
    #     binary_tree = [0]*(N)
    #     steps = 0
    #     while 0 in binary_tree:
    #         steps += 1
    #         i = process(binary_tree)
    #         self.mark(binary_tree, i)
    #     # print(f'            STEPS: {steps}')
    #     s = f'{steps}'
    #     with open(f'results_{p}_{trial}_{n}', 'w') as file_object:
    #         file_object.write(s)

def runTrial(p, trial, n):
    print(os.getcwd())
    e = Experiment()
    if p == '1': process = e.process1
    if p == '2': process = e.process2
    if p == '3': process = e.process3
    N = 2**n - 1
    binary_tree = [0]*(N)
    steps = 0
    print('here1')
    while 0 in binary_tree:
        steps += 1
        i = process(binary_tree)
        e.mark(binary_tree, i)
    print('here2')
    with open(f'results_{p}_{trial}_{n}.txt', 'w') as file_object:
            file_object.write(f'{steps}')
    print('DONE')

def run_p(p):
    for trial in range(0, 1):
        for n in range(10, 12):
            t = threading.Thread(target=runTrial, name=f'=process_{p}_trial_{trial}_n_{n}', args=(p, trial, n,))
            # t.daemon = True
            t.start()
    
        
# e = Experiment()
print('==================================================')
print('PROCESS 1')
print('==================================================')
# e.run(e.process1, '1')
run_p('1')
print('==================================================')
print('PROCESS 2')
print('==================================================')
# e.run(e.process2, '2')
run_p('2')
print('==================================================')
print('PROCESS 3')
print('==================================================')
# e.run(e.process3, '3')
run_p('3')