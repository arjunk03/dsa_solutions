def partition(s):
    lst_indx = {val: indx for indx, val in enumerate(s)}

    start = 0
    end = 0
    res = []
    for i, j in enumerate(s):
        end = max(end, lst_indx[j])

        if i == end:
            res.append(i - start + 1)
            end = 0
            start = i + 1

    return res


s = "ababcbacadefegdehijhklij"
print(partition(s))
