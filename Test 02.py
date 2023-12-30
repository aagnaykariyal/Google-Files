def solution(L):
    L.sort(reverse=True)
    if L == []:
        return 0

    def max_value(n, current_num, ind):
        if ind == len(L):
            if n != 0 and n % 3 == 0:
                return max(n, current_num)
            else:
                return current_num
        else:
            n_new = n
            n_c = int(str(n) + str(L[ind]))
            current_num_val = max_value(n_c, current_num, ind + 1)
            current_num_without_val = max_value(n_new, current_num, ind + 1)
            return max(current_num_val, current_num_without_val)

    return max_value(0, 0, 0)