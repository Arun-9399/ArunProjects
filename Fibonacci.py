def fibonacci(num):
    a = 0
    b = 1
    s = 0
    c = 1
    while c <= num:
        print(s, end="\n")
        c += 1
        a = b
        b = s
        s = a + b


if __name__ == "__main__":
    n = int(input("Enter the no of term of print"))

    fibonacci(n)
