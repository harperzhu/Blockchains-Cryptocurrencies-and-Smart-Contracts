import string
import random
import hashlib

# return the hash of a string
def SHA(s: string) -> string:
    return hashlib.sha256(s.encode()).hexdigest()

# transfer a hex string to integer
def toDigit(s: string) -> int:
    return int(s, 16)

# generate 2^d (si^{-1}, si) pairs based on seed r
def KeyPairGen(d: int, r: int) -> dict:
    pairs = {}
    random.seed(r)
    for i in range(1 << d):
        cur = random.randbytes(32).hex()
        while cur in pairs:
            cur = random.randbytes(32).hex()
        pairs[cur] = SHA(cur)
    return pairs


class MTSignature:
    def __init__(self, d, k):
        self.d = d
        self.k = k
        self.treenodes = [None] * (d+1)
        for i in range(d+1):
            self.treenodes[i] = [None] * (1 << i)
        self.sk = [None] * (1 << d)
        self.pk = None # same as self.treenodes[0][0]


    # Populate the fields self.treenodes, self.sk and self.pk. Returns self.pk.
    def KeyGen(self, d:int, seed: int) -> string:
        # generate preimage / image pairs from the seed 
        pairs = KeyPairGen(d, seed) 
        for pair in pairs: 
            preimages = pair[0] 
        for pair in pairs: 
            leaf_values = pair[1]
            
        #compute Merkle tree
            tree = leaf_values.copy()
            #we loop through each level of the Merkle tree, starting at the bottom and moving up. 
            for level in range(d):
                number_nodes = 2**(d-level)
                level_values = []
                
                #route back to the parent node
            for i in range(number_nodes//2):
                if(number_nodes %2 == 0): 
                    left_node = tree.pop(0)
                    right_node = tree.pop(0)
                    node_value = hashlib.sha256(int.to_bytes(i, 32, 'big') + left_node + right_node).digest()
                    level_values.append(node_value)
                    tree.append(node_value)
                else: 
                    #when there's odd number of nodes in this level
                    only_node = tree.pop(0)
                    node_value = hashlib.sha256(int.to_bytes((number_nodes//2), 32, 'big') + only_node).digest()
                    level_values.append(only_node)
                    tree.append(only_node)
        self.treenodes = tree
        self.pk = tree[0].hex()
        return self.pk

    # Returns the path SPj for the index j
    # The order in SPj follows from the leaf to the root.
    def Path(self, j: int) -> string:
        path = []
        node_index = j
        for level in range(self.d):
            #the left node (even)
            if node_index % 2 == 0:
                sibling_index = node_index + 1 
            else: #the node node (odd)
                sibling_index = node_index - 1
                
            if sibling_index < len(self.tree[level]):
                sibling_hash = self.tree[level][sibling_index]
            else :
                raise ValueError('the sibling index is invalid as it is bigger than the length of the tree node in this level')
            
            path.append(sibling_hash)
            node_index //= 2
        return path
    
    
    # Returns the signature. The format of the signature is as follows: ([sigma], [SP]).
    # The first is a sequence of sigma values and the second is a list of sibling paths.
    # Each sibling path is in turn a d-length list of tree node values. 
    # All values are 64 bytes. Final signature is a single string obtained by concatentating all values.
    def Sign(self, msg: string) -> string:
        message_hash = hashlib.sha256(msg.encode('utf-8')).digest()
        path = self.Path(0)
        for node in path:
            #returns the SHA-256 hash of the input node string encoded as bytes
            if hashlib.sha256(node.encode()).digest() == node:
                left_node = node
            else:
                right_node = node
                if left_node + right_node == message_hash:
                    return left_node
                elif right_node + left_node == message_hash:
                    return right_node
                else:
                    message_hash = hashlib.sha256(left_node + right_node).digest()
        return None
    
    
    
    
    
    
    

    d = 10
    k = 2
    r = 2023
    # Sign a message and print the signature
    message = "Attack at night"
    signature = Sign(message)
    print("Message:", message)
    print("Signature:", signature.hex())
    
    new_message = "Attack at dusk"
    new_message_hash = hashlib.sha256(new_message.encode()).digest()
    right_node = signature
    for i in range(d):
        if i == 0:
            node = new_message_hash
    else:
        node = nodes[i-1]
    left_node = node
    message_hash = hashlib.sha256(left_node + right_node).digest()
    right_node = node
    forged_signature = left_node
    print("Forged Message:", new_message)
    print("Forged Signature:", forged_signature.hex())

        
        
        
    # Find a different message with the same signature    