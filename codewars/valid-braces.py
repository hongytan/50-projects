def find_outlier(integers):
    lst = [x % 2 for x in integers]
    parity = max(set(lst), key=lst.count)
    for x in integers:
        if x % 2 != parity:
            return x
        
list = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(list))