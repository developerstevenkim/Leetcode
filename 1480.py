def runningSum(nums: list[int]) -> list[int]:
    result = [nums[0]]
    for i in range(len(nums)):
        if i == 0:
            continue
        result.append(result[i-1] + nums[i])
    return result


def main():
    # sample inputs
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 1, 1, 1, 1]
    nums3 = [3, 1, 2, 10, 1]

    print(runningSum(nums1))
    print(runningSum(nums2))
    print(runningSum(nums3))


if __name__ == '__main__':
    main()
