# XOR decryption
# Problem 59
# https://projecteuler.net/problem=59

# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange). For
# example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# A modern encryption method is to take a text file, convert the bytes to ASCII,
# then XOR each byte with a given value, taken from a secret key. The advantage
# with the XOR function is that using the same encryption key on the cipher
# text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42
# = 65.
# For unbreakable encryption, the key is the same length as the plain text
# message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and without
# both "halves", it is impossible to decrypt the message.
# Unfortunately, this method is impractical for most users, so the modified
# method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the
# message. The balance for this method is using a sufficiently long password
# key for security, but short enough to be memorable.
# Your task has been made easy, as the encryption key consists of three lower
# case characters. Using p059_cipher.txt (right click and 'Save Link/Target
# As...'), a file containing the encrypted ASCII codes, and the knowledge that
# the plain text must contain common English words, decrypt the message and
# find the sum of the ASCII values in the original text.

from src.lib.utility import read_delimited_data
import string


ENGLISH_LETTER_SCORES = {
    'E': 12.02
    # 'T': 9.10
}


def encrypt(data: list[int], key: list[int]) -> list[int]:
    '''applies a looping xor encryption on the data'''
    encryption = []
    for index, value in enumerate(data):
        key_value = key[index % len(key)]
        encrypted_value = value ^ key_value
        encryption.append(encrypted_value)
    return encryption


def calculate_score(data: list[int]) -> float:
    '''determines how likely the data is actual english text'''
    score = 0.0
    for value in data:
        char = chr(value).upper()
        if char in ENGLISH_LETTER_SCORES:
            score += ENGLISH_LETTER_SCORES[char]
    return score


def decrypt_section(data: list[int], allowed_chars: str) -> int:
    '''finds the most likely character as the key for data'''
    best_score, best_key = -1.0, 0
    for key_char in allowed_chars:
        possible_text = encrypt(data, [ord(key_char)])
        text_score = calculate_score(possible_text)
        if text_score > best_score:
            best_score, best_key = text_score, ord(key_char)
    return best_key


def decrypt(
    encryption: list[int],
    allowed_chars: str,
    key_length: int = 3
) -> tuple[list[int], list[int]]:
    '''decrypts the encrypted string with all possible key values and returns
    the most likely match'''
    # because the key is applied in a cyclical pattern, each character of key
    # can be solved individually
    # first, split the encryption into sections based on key length
    sections = [[] for _ in range(key_length)]
    for index, value in enumerate(encryption):
        sections[index % key_length].append(value)
    best_key = [decrypt_section(sec, allowed_chars) for sec in sections]
    return encrypt(encryption, best_key), best_key


def stringify(data: list[int]) -> str:
    '''returns the ascii string made from the list of int values'''
    return str().join(chr(value) for value in data)


def solve(data_file: str = 'd_059.txt') -> str:
    '''Problem 59 - XOR decryption'''
    data = read_delimited_data(data_file)
    encryption = [int(value) for value in data]
    decryption, key = decrypt(encryption, string.ascii_letters)
    # print(stringify(decryption), stringify(key))
    return str(sum(decryption))


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '129448'


if __name__ == '__main__':
    print(solve())
