from typing import Optional, List
import hashlib
import math


def verify(obj: str, proof: str, commitment: str) -> bool:
    # Convert the object string to its corresponding leaf hash
    hash_obj = hashlib.sha256(obj.encode()).hexdigest()
    # Convert the proof string to a list of hashes.
    for siblingNode_hashed in proof:
        if siblingNode_hashed:
            hash_obj = hashlib.sha256(
                (hash_obj + siblingNode_hashed).encode()).hexdigest()

    return hash_obj == commitment


class Prover:
    def __init__(self):
        self.tree = []
        self.root = None
        self.objects = []
    # return a hex

    def hash(self, data):
        return hashlib.sha256(data.encode())

    def get_hex_form(self, data):
        return self.hash(data).hexdigest()

# Build a merkle tree and return the commitment
    def build_merkle_tree(self, objects: List[str]) -> str:

        self.objects = objects
        hash_values_list = []
        level = 0
        for obj in objects:
            hash_values_list.append(self.get_hex_form(obj))
        subtree = hash_values_list
        self.tree.append(subtree)
        parenttree = []
        while len(subtree) > 1:
            parenttree = []
            for i in range(0, len(subtree), 2):
                if i + 1 < len(subtree):
                    parenttree.append(self.get_hex_form(
                        subtree[i] + subtree[i+1]))
                else:
                    parenttree.append(self.get_hex_form(
                        subtree[i] + subtree[i]))
            self.tree.append(parenttree)
            subtree = parenttree
        self.root = subtree[0]
        # print('sjbdaskdj')
        # print(self.tree)
        return subtree[0]

    def get_leaf(self, index: int) -> Optional[str]:
        if index < 0 or index >= len(self.objects):
            return None
        return self.objects[index]

    def get_sibling(self, index: int, level: int) -> Optional[str]:
        treeLevel = len(self.tree)
        treeIndex_at_Level = len(self.tree[level])
        
        if(level>treeLevel ):
            raise ValueError('the level is out of bounds!')
    
        
        if (index % 2 == 0):  # this is a even node
            if(index+1>treeIndex_at_Level):
                raise ValueError('index+1 is out of bounds!')
            sibling_node = self.tree[level][index+1]
        else:  # this is a odd node   
            if(index-1>treeIndex_at_Level):
                raise ValueError('index-1 is out of bounds!')
            if(index-1<0):
                raise ValueError('index-1 is smaller than 0')   
            index = int(index)
            # print('index-1',index-1)
            sibling_node = self.tree[level][index-1]
        return sibling_node

    def generate_proof(self, index: int) -> Optional[str]:
        # finds the index of the object
        if index < 0:
            return None
        if index >= len(self.objects):
            return None
        # print('i am the index in generate proof', index)
        index = int(index)
        # print('i am the index in generate proof after int', index)
        proofArray = []
        level = 0
        # Returns the proof as an array of hash objects
        # for the leaf at the given index.

        tree = self.tree
        while (level < len(tree)-1):
            # print('type of index is',type(index))
            if (index % 2 == 0):  # this is a even node
                    parent_node_index = index // 2
                    # parent_node = tree[level+1][parent_node_index]
                    # self.get_sibling(index, level+1)
                    # print('2')
                    proofArray.append(self.get_sibling(index, level))
                    index = parent_node_index
                    # print('3')
                    level = level + 1
                    print(index)
                    

            else:  # this is an odd node
                    # print('we are in else ')
                print('4')
                parent_node_index = math.floor((index)/2)
                proofArray.append(self.get_sibling(index, level))
                index = parent_node_index
                level = level + 1
                print(index)

                # take the floor of the index to get to the parent node
        
        return proofArray


# Convert the proof string to a list of hashes.
# Apply the SHA-256 hash function to pairs of hashes, working from the bottom of the tree up to the root, using the proof to determine which hashes to include in each step. This should result in a single hash, which should match the commitment string.
# If the final hash matches the commitment string, return True, indicating that the proof is valid. Otherwise, return False, indicating that the proof is invalid.
if __name__ == "__main__":

    objects = ['a', 'b', 'c', 'd']
    tree = Prover()
    root = tree.build_merkle_tree(objects=objects)
    # proof = tree.generate_proof(2)
    test_tree = [['a','b','c','d'],['ab','cd'],['abcd']]
    test_tree.get_sibling(0,0)
    # print(proof)

    # print(tree)
    # tree.get_leaf(1)
    # print(tree.generate_proof(2))
