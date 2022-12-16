import random
from string import ascii_letters, punctuation, digits


class Dice:
    def __init__(self, verges_count=6, dices_count=1, seed=None):
        """Constructor of dices game
        :param verges_count
        :param dices_count
        :param seed (if we need not real random)
        :return nothing ;)
        """
        self.verges_count = verges_count
        self.dices_count = dices_count
        self.seed = seed

    def play(self) -> list:
        """Returns list with result of dice game with
        :param self.verges_count verges and
        :param self.dices_count dices
        :return list with dices results
        """
        results = []
        for _ in range(self.dices_count):
            self.__set_seed()
            results.append(random.randint(1, self.verges_count))
        return results

    def __set_seed(self):
        """if we need not real random
        :return nothing ;)
        """
        if self.seed is not None:
            random.seed(self.seed)
        else:
            random.seed()


def generate_random_filename(length: int, suffix: str) -> str:
    """
    Returns new file names with :param length and ending :param suffix
    :param length:
    :param suffix:
    :return :type str:
    """
    return "".join([random.choice(ascii_letters) for _ in range(length)]) + "." + suffix


class Password:
    """Use it to save your guard"""

    def __init__(self, symbols_to_use: list[str]):
        """
        Example: ["123", "ad"]
        :param symbols_to_use:
        """
        self.symbols_to_use = symbols_to_use

    def generate_password(self, length: int) -> str:
        """
        :param length:
        :return: password (:type str) that contains symbols from all collections with the :param length
        """
        result = []
        collection_index = 0
        while len(result) < length:
            result.append(random.choice(self.symbols_to_use[collection_index]))
            collection_index = (collection_index + 1) % len(self.symbols_to_use)
        return "".join(result)

    @staticmethod
    def validate_password(
        symbols_to_use: list[str], length: int, password: str
    ) -> bool:
        """
        :return only True or raise exception
        Exceptions on 2 tree:
        1) length
        2) contains collections symbols in password
        """
        if len(password) != length:
            raise Exception(
                f"Password length ({len(password)}) is not suggested with the rules length ({length})!"
            )

        for collection in symbols_to_use:
            is_used = False
            for symbol in collection:
                if symbol in password:
                    is_used = True
            if not is_used:
                raise Exception(
                    f"Collection {collection} is not used in password {password}!"
                )
        return True


class Solution:
    """Tests"""

    @staticmethod
    def run():
        """Execute all tasks"""
        task_names = [method for method in dir(Solution) if method.startswith("task_")]
        for task_name in task_names:
            try:
                getattr(Solution, task_name)()
                print()
            except Exception as e:
                print(f"Error at the {task_name}: {e}")

    @staticmethod
    def task_1():
        """
        Develop a Dice class that models the throwing of dice. An object of this class,
        during initialization, must receive information about the number of dice faces (6 by default)
        and the number of dice in a roll (1 by default). Implement a class method that returns a random
        throw result as a tuple or list
        """
        game_1 = Dice(verges_count=10, dices_count=3)
        game_2 = Dice()
        print(f"[task_1] Game with params: {game_1.play()=}")
        print(f"[task_1] Game without params: {game_2.play()=}")

    @staticmethod
    def task_2():
        """
        Modify the Dice class so that when you specify a specific seed value, when you
        initialize different objects of the class, you can get the same sequence of results.
        """
        game_1 = Dice(seed=999, dices_count=5)
        game_2 = Dice(seed=999, dices_count=3)
        print(f"[task_2] {game_1.play()=}")
        print(f"[task_2] {game_2.play()=}")

    @staticmethod
    def task_3():
        """
        Use the developed class to conduct a statistical experiment to calculate the frequency
        of different values falling out when throwing a pair of six-sided dice. The dropped value
        is taken equal to the sum of the readings on the faces of the bones (from 2 to 12).
        To get statistics, you need to roll the dice at least 100,000 times
        """
        game = Dice(dices_count=2)
        repeats_count, results = 100_000, {}
        for _ in range(repeats_count):
            play_result = sum(game.play())
            if play_result in results.keys():
                results[play_result] += 1
            else:
                results[play_result] = 1
        print(f"[task_3] {results=}")

    @staticmethod
    def task_4():
        """
        Develop a function to generate a random filename of a given length and with a given extension (suffix).
        The name should consist only of letters of the English alphabet in different cases.
        Write a program that demonstrates how this function works.
        """
        print(f"[task 4] {generate_random_filename(length=10, suffix='xyz')=}")
        print(f"[task 4] {generate_random_filename(length=15, suffix='pgu')=}")
        print(f"[task 4] {generate_random_filename(length=5, suffix='txt')=}")

    @staticmethod
    def task_5():
        """
        Develop a Password class to generate passwords. An object of this class, during initialization, must receive
        information about the character sets required for use in the password (at least one character from each set).
        Implement a class method that generates a password of a given length. The password length must be passed
        to the method as a parameter. The password must be returned as a string. Write a program to demonstrate
        how the class works and verify that it works correctly.
        """
        max_password_length_1 = 15
        max_password_length_2 = 15

        min_password_length_1 = 8
        min_password_length_2 = 8

        symbols_to_use_1 = [digits, "QWERTY"]
        symbols_to_use_2 = [punctuation, ascii_letters]

        length_1 = random.randint(
            max(min_password_length_1, len(symbols_to_use_1)), max_password_length_1
        )
        length_2 = random.randint(
            max(min_password_length_2, len(symbols_to_use_2)), max_password_length_2
        )

        password_1 = Password(symbols_to_use=symbols_to_use_1)
        password_2 = Password(symbols_to_use=symbols_to_use_2)

        generated_password_1 = password_1.generate_password(length_1)
        generated_password_2 = password_2.generate_password(length_2)

        is_correct_1 = password_1.validate_password(
            symbols_to_use=symbols_to_use_1,
            length=length_1,
            password=generated_password_1,
        )
        is_correct_2 = password_2.validate_password(
            symbols_to_use=symbols_to_use_2,
            length=length_2,
            password=generated_password_2,
        )

        print(f"[task 5] {generated_password_1=}\n{is_correct_1=} {length_1=}")
        print(f"[task 5] {generated_password_2=}\n{is_correct_2=} {length_2=}")


solution = Solution()
solution.run()
