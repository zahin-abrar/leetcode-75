from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candies = max(candies)

        for c in candies:
            if c + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result

if __name__ == "__main__":
    sol = Solution()

    print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))
    print(sol.kidsWithCandies([4, 2, 1, 1, 2], 1))
    print(sol.kidsWithCandies([12, 1, 12], 10))
