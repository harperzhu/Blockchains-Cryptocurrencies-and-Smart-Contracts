# this is the python file to find the mint and code
import random
import hashlib
import secrets

k = 4
n = 28
netID = "rz386"


def get_watermark(netID):
    watermark = bin(
        int(hashlib.sha256(netID.encode(encoding="ascii")).hexdigest(), base=16)
    ).lstrip("0b")[:16]
    return watermark  # return the watermark as a binary, 16 character string


# def get_hex_watermark(watermark):
#     watermark_hex = format(int(watermark, 2), 'x')
#     return watermark_hex


# watermark = get_watermark(netID='rz386')
# watermark_hex = get_hex_watermark(watermark=watermark)
# # coin = find_coin(watermark_hex)
# print(watermark_hex)

# generate a unique identifier for each coin,
def get_byte_form(watermark, i):
    # the input watermark is already in byte form
    # 64 bits hex

    # print("watermark = ", watermark)
    # print("i = ", i)
    
    byte_str = int(watermark + i, 2).to_bytes(8,'big')
    
    # print('i type' , type(i))
    # print('watermark' , type(watermark_byte))
    print(byte_str)
    
    # byte_str = watermark_byte + i
    # print('byte string' + byte_str)
    # l = (len(watermark) + 3) // 4
    # watermark_hex = "{:0{}x}".format(int(watermark, 2), l)
    # print(hex_str)
    # print(i)
    # hex_str = hex_str.hex()
    return byte_str


def get_hashed_coin_bytes(byte_str):
    hashed_coin_bytes = hashlib.sha256(byte_str).hexdigest()[2:30]
    hashed_coin_bits = bin(int(hashed_coin_bytes, 16))
    return hashed_coin_bits


# A coin C = (c1,c2,...,ck) such that[H(ci)]n = y for all i ∈ [1,...,k] and for some value y
# Each preimage ci must be 8 bytes (64-bits) long and have w as its first 16 bits.
def find_coin(watermark):

    random_bits = bin(secrets.randbits(48)).lstrip('0b').zfill(48)
    # random_bits = int(random_bits,2).to_bytes(6,'big')
    
    #this is writing 14, 15 
    print(random_bits)
    print(len(random_bits))
    # while len(random_bits) == 48:
        # random_bits = secrets.randbits(48)
    #this is writing 14, 15 
    print(len(random_bits))
    # random_bits = hex(int(random_bits, 16))
    # print(random_bits)
    # random_bits = int(random_bits, 16)[2:18]
    print(random_bits)
    c_i = get_byte_form(watermark, random_bits)
    c_i = get_hashed_coin_bytes(c_i)  # first 28 bits
    same_coin = []
    did_find_coin = False
    while not did_find_coin:
        random_bits = bin(secrets.randbits(48)).lstrip('0b').zfill(48)
        # random_bits = int(random_bits,2).to_bytes(6,'big')
        
        # while len(random_bits) == 48:
        #     random_bits = random.getrandbits(48)
        # random_bits = (int(random_bits, 16))[2:18]
        # print(random_bits)
        c_j = get_byte_form(watermark, random_bits)
        c_j = get_hashed_coin_bytes(c_j)
        new_coin = watermark + random_bits
        new_coin = hex(int(new_coin,2))[2:30]
        print(new_coin)
        if c_j == c_i:
            same_coin.append(new_coin)
            if (len(same_coin)) == 4:
                did_find_coin = True
    # print(same_coin)
    # c_i = get_byte_form(c_i)
    # c_j = get_byte_form(watermark, m)
    # c_k = get_byte_form(watermark, p)
    # c_l = get_byte_form(watermark, q)
    # hashed_preimage = [get_hashed_coin_bytes(c_i),
    #                    get_hashed_coin_bytes(c_j),
    #                    get_hashed_coin_bytes(c_k),
    #                    get_hashed_coin_bytes(c_l)]
    # check if all four preimages produce the same hash value
    # which means we got a valid coin.
    # if all(preimage == hashed_preimage[0] for preimage in hashed_preimage):
    #     preimageArray = [c_i.hex(), c_j.hex(), c_k.hex(), c_l.hex()]
    #     print(preimageArray)
    #     break

    file = open("/Users/ruijiazhu/Downloads/given-code/p1/coin.txt",'w')
    for coin in same_coin:
        file.write(coin + "\n")

    file.close()


# Forging watermarks:
# For your coin C,
# forge an alternative netid nid∗.
# That is, present a netid nid∗ ̸= nid that is valid a valid watermark for your coin C.
# Your watermark must take the form lidj, where l is a letter, d is a digit, i ∈ {2, 3}, and j ∈ {1, . . . , 10}.
# An example is provided below.
# Please specify the forged netid nid∗ in a file forged-watermark.txt.


def generate_netid(netID):
    # forgedID = generate_netid('rz386')
    # print (forgedID)
    netID__number = "0123456789"
    netID__character = "abcdefghijklmnopqrstuvwxyz"
    # create a list to store all the generated random netIds
    random_netID_list = []
    for i in range(2, 4):
        l_list = random.sample(netID__character, i)
    for d in range(1, 11):
        d_list = random.sample(netID__number, d)

    for l in l_list:
        for d in d_list:
            random_netID_list = "".join(l + d)

    my_netID_watermark = get_watermark(netID)
    for random_netID in random_netID_list:
        watermark = get_watermark(random_netID)
        if my_netID_watermark != watermark:
            continue
        else:
            return random_netID


if __name__ == "__main__":
    find_coin(watermark=get_watermark(netID=netID))
    
