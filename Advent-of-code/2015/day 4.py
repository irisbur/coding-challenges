import hashlib


def secret_key():
    num = 1
    key = "key"
    result = hashlib.md5((key + str(num)).encode()).hexdigest()
    while result[:6] != "000000":
        num += 1
        result = hashlib.md5((key + str(num)).encode()).hexdigest()
    print(num)

    
secret_key()
