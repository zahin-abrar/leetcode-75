def productExceptSelf(nums: list[int]) -> list[int]:
    left_current_product = 1
    right_current_product = 1
    left_product = []
    right_product = [0] * len(nums)

    answer = []

    for i in range(len(nums)):
        left_product.append(left_current_product)
        left_current_product *= nums[i]

    for i in range(len(nums)-1, -1, -1):
        right_product[i] = right_current_product
        right_current_product *= nums[i]

    for i in range(len(nums)):
        answer.append(left_product[i] * right_product[i])

    return answer

print(productExceptSelf([1,2,3,4]))