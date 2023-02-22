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
        pass
    # return a hex

    def hash(data):
        return hashlib.sha256(data.encode())

    def get_hex_form(self, data):
        return self.hash(data).hexdigest()

# Build a merkle tree and return the commitment
    def build_merkle_tree(self, objects: List[str]) -> str:
        if len(objects) == 0:
            return 'error message: the input is an empty list!'
        # Compute the hash value of each object
        for obj in objects:
            hash_values_list = self.get_hex_form(obj) 

        # duplicate the last object in the list if the number of objects is odd
        list_length = len(hash_values_list)
        if list_length % 2 != 0:
            lastObject = hash_values_list[-1]
            hash_values_list.append(lastObject)
            list_length = list_length + 1

        # if the number of objects is even
        # Make each object's hash value to be nodes in the tree.
        tree = []
        for i in range(list_length):
            tree.append(hash_values_list[i])
            # leave out the root node
            for i in range(list_length - 1):
                tree.append(None)
        # Compute the hash value of each non-leaf node  adding
        # by summing the hash values of the two child nodes and hashing the sum result.

        for i in range(list_length - 2, -1, -1):
            left_child = tree[2 * i + 1]
            right_child = tree[2 * i + 2]
            parent_hash = self.hash(left_child + right_child).hexdigest()
            tree[i] = parent_hash

        return tree[0]

    def get_leaf(self, index: int) -> Optional[str]:
        for node in self.tree:
            if node.left and node.right:
                #initiate the leaf nodes list
                leaf_nodes = []
                if index < 0 or index >= len(leaf_nodes):
                    return None
                return leaf_nodes[index].value


def generate_proof(self, index: int) -> Optional[str]:
    # finds the index of the object
    if index < 0:
        return ValueError("index is smaller than 0 ")
    if index >= len(self.objects):
        return ValueError("index is larger than the length of the object string")

    # store the hash value of nodes in this merkle_proof
    merkle_proof = []

    # Start from the leaf node and find the path to the root node
    curr_index = index + self.list_length - 1

    while curr_index > 0:
        # Find the sibling index
        if curr_index % 2 == 0:  # if this is even index
            sibling_index = curr_index - 1
        else:  # if this is odd index
            sibling_index = curr_index + 1
        # Append the sibling value to the proof
        merkle_proof.append(self.tree[sibling_index])

        # move the current index to its parent node
        curr_index = (curr_index - 1) // 2

    return merkle_proof




# Convert the proof string to a list of hashes.
# Apply the SHA-256 hash function to pairs of hashes, working from the bottom of the tree up to the root, using the proof to determine which hashes to include in each step. This should result in a single hash, which should match the commitment string.
# If the final hash matches the commitment string, return True, indicating that the proof is valid. Otherwise, return False, indicating that the proof is invalid.
