def funcfact(a):
    n = 1

    for i in range(1, a + 1):
        n *= i

    print(f"Factorial of number is {n}")

num = int(input("Enter a number: "))

funcfact(num)