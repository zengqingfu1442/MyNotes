#  Q: Given an array nums of n unique integers, are there elements a, b, c in nums such that a + b + c = 0? Find all
#  unique triplets in the array which gives the sum of zero.
# Example:
#
# Given array nums = [-2, -1, 0, 1, 3, -4],
#
# [
# [-2, -1, 3]
# [-1, 0, 1]
# [-2, 1, -1]
# ]


def func(lst: list) -> list:
    rslt = []
    if min(lst) >= 0 or max(lst) <= 0:
        print('no such triplets')
        return
    lst1 = [x for x in lst if x < 0]
    lst2 = [x for x in lst if x >= 0]
    for x in lst1:
        for y in lst2:
            z = x + y
            if -z in lst2 and -z != y:
                # print(x, y, -z)
                if sorted([x, y, -z]) not in rslt:
                    rslt.append(sorted([x, y, -z]))
    for x in lst2:
        for y in lst1:
            z = x + y
            if -z in lst1 and -z != y:
                # print(x, y, -z)
                if sorted([x, y, -z]) not in rslt:
                    rslt.append(sorted([x, y, -z]))
    # print(rslt)
    print(len(rslt))
    for _ in rslt:
        print(_)
    return rslt


if __name__ == '__main__':
    nums = [-2, -1, 0, 1, 3, -4]
    nums2 = [-11, -29, -67, -2, -3, -4, -1, 0, 1, 2, 3, 4, 5, 67, 23, 11, 28, 7, 10, 11]
    func(nums2)
