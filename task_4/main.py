import random
from argparse import Namespace
from string import ascii_letters, digits


class Passwords:
    def __init__(self, count, length, alphabet):
        if not count:
            count = 1

        if not length:
            length = 5

        if not alphabet:
            alphabet = digits + ascii_letters
        self.count = count
        self.length = length
        self.alphabet = alphabet


    def generate_passwords(self) -> list[str]:
        answer = []
        for _ in range(self.count):
            result = []
            while len(result) < self.length:
                collection_index = random.randint(0, len(self.alphabet) - 1)
                result.append(random.choice(self.alphabet[collection_index]))
            answer.append("".join(result))
        return answer


def parse_args() -> Namespace:
    import argparse
    parser = argparse.ArgumentParser(description='Console password generator')
    parser.add_argument('--count', type=int, help='count')
    parser.add_argument('--length', type=int, help='length')
    parser.add_argument('--alphabet', type=str, help='alphabet')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    passwords = Passwords(args.count, args.length, args.alphabet)
    print(*passwords.generate_passwords(), sep='\n')

if __name__ == '__main__':
    main()
