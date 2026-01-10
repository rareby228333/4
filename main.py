import random
import operator

class Encryptor:
    def __init__(self, *numbers):
        self._numbers = numbers
        self._result = self._encrypt()

    def _encrypt(self):
        operations = [
            operator.add,
            operator.sub,
            operator.mul,
            operator.truediv
        ]
        op = random.choice(operations)

        result = self._numbers[0]
        for n in self._numbers[1:]:
            if op == operator.truediv and n == 0:
                n = 1
            result = op(result, n)
        return result

    def __str__(self):
        return f"{self._result}"

obj = Encryptor(5, 3, 2, 7, 9)
print(obj)