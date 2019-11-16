
def fact_memoization(func):
    memory = {}

    def fact(num):
        if num not in memory:
            memory[num] = func(num)

        return memory[num]

    return fact


@fact_memoization
def factorial(num):
    if num == 1:
        return 1 
    return num * factorial(num - 1)


print(factorial(5))
print(factorial(7))