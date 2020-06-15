import re 
def validate_uid(uid):
    pattern = re.compile(r'^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)(?!.*[^0-9a-zA-Z])(?!.*(.).*(\1)).{10}$')
    a = pattern.search(uid)
    
    if a :
        print("Valid")
    else:
        print("Invalid")

def filter_uid(uidss):
    return list(filter(validate_uid, uidss))



if __name__ == "__main__":
    n = int(input())
    uidss = []
    for _ in range(n):
        uidss.append(input())
filter_uid(uidss)
