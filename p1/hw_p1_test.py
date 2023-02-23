import hashlib 
byte_str = ['867a95c2a8781d95', '867a79c683c4b9de', '867a18839dcbd23f', 
            '867aee195b47b3d2']

def get_hashed_coin_bytes(byte_str):
    byte_str = 
    hashed_coin_bytes = hashlib.sha256(byte_str).hexdigest()[2:30]
    hashed_coin_bits = bin(int(hashed_coin_bytes, 16))
    return hashed_coin_bits

for x in byte_str:
    print(get_hashed_coin_bytes(byte_str=x))