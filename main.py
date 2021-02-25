from random import randint
from random import choice
import sys

# sys.setrecursionlimit(4000)

PRINT_FLAG = False

class Experiment:
    def __init__(self):
        self.nodes_sent = []

    def process1(self, t):
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

    def perfromMarkingRules(self, t, i):
        # Check if current node is marked
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
        if PRINT_FLAG: print('==================================================')
        if PRINT_FLAG: print(f'M: {t}')
        self.perfromMarkingRules(t, i)
        if PRINT_FLAG: print(f'N: {t}')
        self.climbUp(t, i if i==0 else (i-1)//2)

    def run(self, process):
        for trial in range(0, 10):
            print(f'    TRIAL {trial}')
            for n in range(10, 21):
            # for n in range(10, 11):#21):
                print(f'        FOR n = {n}')
                if process == e.process2: self.nodes_sent = []
                N = 2**n - 1
                binary_tree = [0]*(N)
                steps = 0
                while 0 in binary_tree:
                    steps += 1
                    i = process(binary_tree)
                    self.mark(binary_tree, i)
                print(f'            STEPS: {steps}')

e = Experiment()
print('==================================================')
print('PROCESS 1')
print('==================================================')
e.run(e.process1)
print('==================================================')
print('PROCESS 2')
print('==================================================')
e.run(e.process2)
print('==================================================')
print('PROCESS 3')
print('==================================================')
e.run(e.process3)