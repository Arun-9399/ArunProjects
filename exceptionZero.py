def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("There is a divide by zero error")
        return 0


if __name__ == "__main__": 
    x = float(input('Enter a number'))
    y = float(input('Enter value by which you want to divide the number'))
    result = divide(x, y)
    print(result)
