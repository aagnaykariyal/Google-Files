val = [1, 2, 2, 3, 3, 3, 4, 4, 5, 1, 2, 2, 3, 3, 1, 2, 2, 3, 3, 3, 4, 4, 5, 3, 4, 4, 5, 1, 2, 2, 3, 3, 3, 4, 4, 5, 1, 2,
       2, 3, 3, 3, 4, 4, 5, 1, 2, 2, 3, 3, 3, 4, 4, 5, 1, 2, 2, 3, 3, 3, 4, 4, 5, 1, 2, 2, 3, 3, 3, 4, 4, 5, 1, 2, 2, 3,
       3, 3, 4, 4, 5, 1, 2, 3, 4, 4, 5, 8, 9, 7]
num = 4


def solution(data, n):
    if type(n) != int:
        raise TypeError("Kindly provide an integer value")
    for d in data:
        if type(d) != int:
            raise TypeError("Kindly provide all integer values")
    if len(data) > 100:
        raise "Kindly input a list with less than 100 values"
    res = [dat for dat in data if data.count(dat) <= n]
    return res


print(solution(val, num))
