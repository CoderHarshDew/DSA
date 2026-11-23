class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = list()

        for i in range(1, n + 1):
            s = [0, 0]
            if i % 3 == 0:
                s[0] = 1
            if i % 5 == 0:
                s[1] = 1

            if sum(s) == 2:
                answer.append("FizzBuzz")
            elif sum(s) == 1:
                if s[0] == 1:
                    answer.append("Fizz")
                else:
                    answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer

# Problem Quick Note
# Wrongly assumed % would return zero when i < 3 or 5 and i % 3 (or 5). Hence, made the code unnecessarily complex. 