# coding: utf-8

# 顺序查找 O(n)
def sequential_search(list_, item):
    for x in list_:
        if x == item:
            return True
    return False


list_ = [3, 6, 1, 2, 5, 11, 0]
print(sequential_search(list_, 4))
print(sequential_search(list_, 11))


# 二分查找 O(log^n)
def binary_search(list_, item):
    first = 0
    end = len(list_) - 1

    while first <= end:
        mid = (first + end) // 2
        if list_[mid] == item:
            return True
        elif list_[mid] < item:
            first = mid + 1
        else:
            end = mid - 1
    return False


list_ = sorted(list_)

print(binary_search(list_, 4))
print(binary_search(list_, 11))
