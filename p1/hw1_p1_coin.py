#this is the python file to find the mint and code 
import hashlib

k = 4
n = 28
netID = 'rz386'


def get_watermark(netID):
    #hashlib.sha256() computes the SHA256 hash of the hex string and returns a hash object.
    #encodes the string as a bytes object and convert it to a hex string by hex()
    # hexdigest() method comvert the hex representation of the hash as a string.
    #bin() function converts the integer to a binary string with a '0b' prefix.
    #use lstrip to remove the leading characters of 0b
    #then fill the string with zeros until it is 256 characters long
    #then take the first 16 character of that string
    
    watermark = bin(int(hashlib.sha256(netID.encode()).hexdigest(), base=16)).lstrip(
        '0b').zfill(16)[:16]
    return watermark #return the watermark as a binary, 16 character string



def get_hex_watermark(watermark):
    watermark_hex = format(int(watermark, 2), 'x')
    return watermark_hex


# watermark = get_watermark(netID='rz386')
# watermark_hex = get_hex_watermark(watermark=watermark)
# # coin = find_coin(watermark_hex)
# print(watermark_hex)

#generate a unique identifier for each coin,
def get_byte_form(watermark,i):  
    hex_str = watermark + format(i, '016x')
    byte_str = bytes.fromhex(hex_str)

    return byte_str;

def get_hashed_coin_bytes(byte_str):
    hashed_coin_bytes = hashlib.sha256(byte_str).digest()[:n//8]
    return hashed_coin_bytes

    

#A coin C = (c1,c2,...,ck) such that[H(ci)]n = y for all i ∈ [1,...,k] and for some value y
# Each preimage ci must be 8 bytes (64-bits) long and have w as its first 16 bits.
def find_coin(watermark):
    preimageArray = []
    for i in range(50000):
        for m in range(i+1, 50000):
            for p in range(m+1, 50000):
                for q in range(p+1, 50000):
                    c_i = get_byte_form(watermark, i)
                    c_j = get_byte_form(watermark, m)
                    c_k = get_byte_form(watermark, p)
                    c_l = get_byte_form(watermark, q)
                    hashed_preimage = [get_hashed_coin_bytes(c_i),
                              get_hashed_coin_bytes(c_j),
                              get_hashed_coin_bytes(c_k),
                              get_hashed_coin_bytes(c_l)]
                    # check if all four preimages produce the same hash value
                    # which means we got a valid coin.
                    if all(preimage == hashed_preimage[0] for preimage in hashed_preimage):
                        preimageArray = [c_i.hex(), c_j.hex(), c_k.hex(), c_l.hex()]
                        print(preimageArray)
                        return preimageArray
                    

    return preimageArray

    


# Forging watermarks: 
# For your coin C, 
# forge an alternative netid nid∗. 
# That is, present a netid nid∗ ̸= nid that is valid a valid watermark for your coin C. 
# Your watermark must take the form lidj, where l is a letter, d is a digit, i ∈ {2, 3}, and j ∈ {1, . . . , 10}. 
# An example is provided below. 
# Please specify the forged netid nid∗ in a file forged-watermark.txt.

import random

def generate_netid(netID):
    # forgedID = generate_netid('rz386')
    # print (forgedID)
    netID__number = '0123456789'
    netID__character = 'abcdefghijklmnopqrstuvwxyz'
    #create a list to store all the generated random netIds
    random_netID_list = []
    for i in range(2, 4):
        l_list = random.sample(netID__character, i) 
    for d in range(1, 11): 
        d_list = random.sample(netID__number, d)

    for l in l_list:
        for d in d_list:
            random_netID_list = ''.join(l + d)
            
    my_netID_watermark = get_watermark(netID)
    for random_netID in random_netID_list:
        watermark = get_watermark(random_netID)
        if my_netID_watermark != watermark:
            continue
        else:
            return random_netID
            

# forged = generate_netid('rz386')
# print('1')
# print(forged)

    
