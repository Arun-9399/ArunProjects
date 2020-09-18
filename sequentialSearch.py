#SequentialSearch Algorithm
def sequentialSearch(alist,item):
    pos=0
    found=False
    while pos<len(alist) and not found:
        if alist[pos]==item:
            found=True
        else:
            pos +=1
    return found
if __name__ == "__main__":
    testlist =[1,2,32,8,7,19,17,42,93,13]
    print (sequentialSearch(testlist,3))
    print(sequentialSearch(testlist,13))
