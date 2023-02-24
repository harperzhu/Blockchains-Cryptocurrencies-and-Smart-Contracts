import sys
import random
import string
from merkle import Prover, verify
from collections import defaultdict
from matplotlib import pyplot as plt
from hashlib import sha256
from math import log2, ceil
from copy import deepcopy


def get_sibling(index: int, level: int):
        test_tree = [['a','b','c','d'],['ab','cd'],['abcd']]
        treeLevel = len(test_tree)
        treeIndex_at_Level = len(test_tree[level])
        
        if(level>treeLevel ):
            raise ValueError('the level is out of bounds!')
    
        
        if (index % 2 == 0):  # this is a even node
            if(index+1>treeIndex_at_Level):
                raise ValueError('index+1 is out of bounds!')
            sibling_node = test_tree[level][index+1]
            print('i am sibling node', sibling_node)
        else:  # this is a odd node   
            if(index-1>treeIndex_at_Level):
                raise ValueError('index-1 is out of bounds!')
            if(index-1<0):
                raise ValueError('index-1 is smaller than 0')   
            index = int(index)
            # print('index-1',index-1)
            sibling_node = test_tree[level][index-1]
        return sibling_node
    
    
p = Prover()
p.build_merkle_tree(['a','b','c','d'])
print(p.tree)
print(p.generate_proof(0))

