# coding: utf-8

# 冒泡排序、块排、桶排序
def bubble_sort(list_):
    count = len(list_)
    for i in range(count):
        finished = True
        for j in range(count-i-1):
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
                finished = False

        if finished:
            break

    return list_

def quick_sort(list_, left, right):
    if left >= right:
        return list_

    low = left
    high = right
    value = list_[left]

    while left < right:
        while left < right and value <= list_[right]:
            right -= 1
        list_[left] = list_[right]
        while left < right and value >= list_[left]:
            left += 1
        list_[right] = list_[left]

    list_[left] = value

    quick_sort(list_, low, left - 1)
    quick_sort(list_, left + 1, high)

    return list_

def bucket_sort(list_):
    min_num = min(list_)
    max_num = max(list_)

    bucket_range = int((max_num - min_num) / len(list_))
    bucket = [[] for _ in range(len(list_) + 1)]

    for num in list_:
        bucket[(num - min_num) // bucket_range].append(num)

    rest = []
    for bucket_item in bucket:
        for num in sorted(bucket_item):
            rest.append(num)

    return rest


def sort_code():
    list_ = [1, 6, 2, 9, 9, 10, 3, 2, 1]
    print(bubble_sort(list_))
    print(quick_sort(list_, 0, len(list_) - 1))
    print(bucket_sort(list_))


if __name__ == '__main__':
    sort_code()
