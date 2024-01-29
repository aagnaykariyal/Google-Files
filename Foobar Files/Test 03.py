# My solution

def solution(lists):
    if len(lists) == 0:
        return "0"
    if len(lists) == 1:
        return str(lists[0])

    positive_numbers = [x for x in lists if x > 0]
    negative_numbers = [x for x in lists if x < 0]

    if len(negative_numbers) == 1 and len(positive_numbers) == 0:
        return "0"
    elif len(negative_numbers) == 0 and len(positive_numbers) == 0:
        return "0"
    else:

        value = 1
        for num in positive_numbers:
            value = value * num

        if len(negative_numbers) % 2 == 1:
            negative_numbers.remove(max(negative_numbers))

        for num in negative_numbers:
            value = value * num

        return str(value)

