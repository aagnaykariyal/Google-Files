from itertools import combinations


def solution(lists):
    positive_numbers = [x for x in lists if x > 0]
    negative_numbers = [x for x in lists if x < 0]

    if len(lists) == 0 or lists == None:
        return "0"

    if len(positive_numbers) == 0 and len(negative_numbers) <= 1 and 0 in lists:
        return str(0)
    elif len(positive_numbers) == 0 and len(negative_numbers) == 1:
        return str(max(negative_numbers))

    if len(negative_numbers) % 2 != 0:
        negative_numbers.remove(max(negative_numbers))

    combined_numbers = positive_numbers + negative_numbers
    values = []
    for r in range(1, len(combined_numbers)+1):
        combs = combinations(combined_numbers, r)
        for comb in combs:
            result = 1
            for num in comb:
                result  = result * num
            values.append(result)
    return str(max(values))

print(solution([-2, 0]))