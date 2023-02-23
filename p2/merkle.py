from typing import Optional, List
import hashlib


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
        self.tree = tree
        self.objects = objects
        if (len(objects)) <= 1:
            raise ValueError('there is less than 1 object in the list!')
        hash_values_list = []
        subtree_dict = []
        for obj in objects:
            hash_values_list.append(self.get_hex_form(obj))
        level = 0
        subtree_dict[level] = hash_values_list

        self.tree.append(subtree_dict)

        while len(tree[0]) < len(obj):
            parenttree_dict = []
            level = 1
            for i in range(0, len(objects), 2):
                    if i + 1 < len(objects):
                        parenttree_dict[level] = (
                            self.get_hex_form(subtree_dict[level][i] + subtree_dict[level][i+1]))
                    else:
                        parenttree_dict[level] = (
                            self.get_hex_form(subtree_dict[level][i] + subtree_dict[level][i]))
            
            self.tree.append(parenttree_dict[level])
            level = level + 1
   #         subtree = parenttree_dict
            self.root = tree[0]
        return tree[0]

    def get_leaf(self, index: int) -> Optional[str]:
        if index < 0 or index >= len(self.objects):
            return None
        return self.objects[index]

    def generate_proof(self, index: int) -> Optional[str]:
        # finds the index of the object
        if index < 0:
            return None
        if index >= len(self.objects):
            return None

        proofArray = []
        # Returns the proof as an array of hash objects
        # for the leaf at the given index.
        tree = self.tree
        for i in range(0, len(tree), 2):
            if (index % 2 == 0):  # this is a even node
                print('are we in this branch')
                sibling_object = self.get_leaf(index+1)
                print('what is printing this ')
                proofArray.append(f'{sibling_object}' + '')
                index = index // 2
            else:  # this is an odd node
                print('we are in else ')
                sibling_object = self.get_leaf(index-1)
                proofArray.append(f'{sibling_object}' + '')

            # take the floor of the index to get to the parent node

        return proofArray


# Convert the proof string to a list of hashes.
# Apply the SHA-256 hash function to pairs of hashes, working from the bottom of the tree up to the root, using the proof to determine which hashes to include in each step. This should result in a single hash, which should match the commitment string.
# If the final hash matches the commitment string, return True, indicating that the proof is valid. Otherwise, return False, indicating that the proof is invalid.
if __name__ == "__main__":

    objects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    tree = Prover()
    print(tree.build_merkle_tree(objects))
    # tree.get_leaf(1)
    # print(tree.generate_proof(2))
