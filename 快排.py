a = [1, 3, 5, 6, 3, 5, 7, 2, 3, 64, 34]


def quick_sort(a):
    if len(a) <= 1:
        return a

    mid_num = a[int(len(a) // 2)]

    left_list = []
    mid_list = []
    right_list = []

    for i in range(len(a)):
        if a[i] < mid_num:
            left_list.append(a[i])
        if a[i] == mid_num:
            mid_list.append(a[i])
        if a[i] > mid_num:
            right_list.append(a[i])
    left_list = quick_sort(left_list)
    right_list = quick_sort(right_list)

    return left_list + mid_list + right_list


b = quick_sort(a)
print(b)
