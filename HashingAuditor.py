import bcrypt
import hashlib
import time


def variables():  # The building blocks we are going to use
    salt = bcrypt.gensalt()  # bcrypt only accepts this salt
    test_1 = "Ricky".encode()  # Changing str to byte
    test_2 = "Ricks".encode()  # Change only 1 char (Av. Effect)
    bcrypt_test(test_1, test_2, salt)
    md5_test(test_1, test_2)
    PBKDF2_test(test_1, test_2, salt)  # Feeds info to tests


def bcrypt_test(test_1, test_2, salt):  # Running test with Bcrypt
    print("----BCRYPT TEST----")
    start = time.perf_counter()  # Start timer
    hash_1 = bcrypt.hashpw(test_1, salt)
    hash_2 = bcrypt.hashpw(test_2, salt)  # hashing the password
    end = time.perf_counter()  # End timer
    counter(start, end)
    hash_to_bit(hash_1, hash_2)  # Feeds info to


def md5_test(test_1, test_2):  # Running test with MD5
    print("\n----MD5 TEST----")
    start = time.perf_counter()
    hash_1 = hashlib.md5(test_1).digest()  # HASH object to bytes
    hash_2 = hashlib.md5(test_2).digest()
    end = time.perf_counter()
    counter(start, end)
    hash_to_bit(hash_1, hash_2)


def PBKDF2_test(test_1, test_2, salt):  # Running test with PBKDF2
    print("\n----PBKDF2(600,000) TEST----")
    start = time.perf_counter()
    hash_1 = hashlib.pbkdf2_hmac('sha256', test_1, salt, 600000)
    hash_2 = hashlib.pbkdf2_hmac('sha256', test_2, salt, 600000)
    end = time.perf_counter()
    counter(start, end)
    hash_to_bit(hash_1, hash_2)


def counter(start, end):  # Time(s) to complete hash
    count = end - start
    # .6f cuts of decimals
    result = print(f"\n \t The time it took was {count:.6f} seconds")
    return result


def hash_to_bit(hash_1, hash_2):  # Converting bytes to bits
    bit_1 = ''.join(format(byte, '08b')
                    for byte in hash_1)  # '08b' signifies the change
    bit_2 = ''.join(format(byte, '08b')for byte in hash_2)
    avalanche_effect(bit_1, bit_2)


def avalanche_effect(bit_1, bit_2):  # Comparing the 2 tests
    difference = 0
    # Chooses the shortest to avoid crash
    total_bits = min(len(bit_1), len(bit_2))

    for i in range(total_bits):
        if bit_1[i] != bit_2[i]:
            difference += 1

    percentage_dif = (difference / total_bits) * 100
    result = print(
        f"\n \t Avalanche effect: {percentage_dif: .1f}% of the bits changed")
    return result


if __name__ == "__main__":
    variables()
