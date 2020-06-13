def interest(p, r, t):
    si = (p * r * t) / 100
    return si
    
if __name__ == "__main__":
    p = int(input("Principle Amount = "))
    r = float(input("Interest Rate per Year = "))
    t = int(input("time in year = "))
    simple_interest = interest(p, r, t)
    print('simple Interest = %.2f' % simple_interest)
