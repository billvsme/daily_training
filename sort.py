# coding: utf-8

# 冒泡排序、块排、桶排序

# 冒泡排序
# 最好时间复杂度O(n), 最差时间复杂度O(n^2), 平均时间复杂度O(n^2), 空间复杂度O(1)
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


# 直接选择排序
# 相对于冒泡排序交换次数减少,最好时间复杂度O(n), 最差时间复杂度O(n^2), 平均时间复杂度O(n^2), 空间复杂度O(1)
def select_sort(list_):
    count = len(list_)
    for i in range(count):
        min_index = i
        for j in range(min_index+1, count):
            if list_[j] < list_[min_index]:
                min_index = j

        list_[i], list_[min_index] = list_[min_index], list_[i]

    return list_


# 插入排序
# 最好时间复杂度O(n), 最差时间复杂度O(n^2), 平均时间复杂度O(n^2), 空间复杂度O(1)
def insert_sort(list_):
    count = len(list_)

    for i in range(count):
        j = i
        value = list_[i]

        while j > 0 and list_[j-1] > value:
            list_[j] = list_[j-1]
            j -= 1

        list_[j] = value

    return list_


# 希尔排序
# 是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本 最好时间复杂度O(n), 最差时间复杂度O(n^2), 平均时间复杂度O(n^1.3), 空间复杂度O(1)
def gap_insert_sort(list_, start, gap):
    for i in range(start+gap, len(list_), gap):
        j = i
        value = list_[i]
        while j >= gap and list_[j-gap] > value:
            list_[j] = list_[j-gap]
            j -= gap

        list_[j] = value

    return list_


def shell_sort(list_):
    sub_list_count = len(list_) // 2
    while sub_list_count > 0:
        for start in range(sub_list_count):
            gap_insert_sort(list_, start, sub_list_count)

        sub_list_count = sub_list_count // 2

    return list_


# 归并排序
# 时间复杂度最好最差都是O(n*log2n), 空间复杂度O(n), 稳定
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def merge_sort(list_):
    if len(list_) <= 1:
        return list_

    mid = len(list_) // 2

    left = merge_sort(list_[:mid])
    right = merge_sort(list_[mid:])

    return merge(left, right)


# 快排
# 最好时间复杂度O(n*log2n), 最差时间复杂度O(n^2), 平均时间复杂度O(n*log2n), 空间复杂度O(log2n)~O(n) 不稳定
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


import math

def bucket_sort(list_):
    min_num = min(list_)
    max_num = max(list_)

    bucket_range = math.ceil((max_num - min_num) / len(list_))
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
