def is_number_nagative_in_array(nums):
    if (
        nums is None
        or len(nums) < 2
    ):
        return False

    for num in nums:
        if (
            not isinstance(num, int)
            or num < 0
        ):
            return True

    return False


def find_duplicate(nums):
    if (
        nums is None
        or len(nums) < 2
        or is_number_nagative_in_array(nums)
    ):
        return False

    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
