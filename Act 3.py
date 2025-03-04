def productfun(num):
    list1=list(num)
    mult=1
    for a in list1:
        mult=mult*a
    return mult

n=(18,9,-27,-456)
print("Tuple:",n)
print("Product are:",productfun(n))