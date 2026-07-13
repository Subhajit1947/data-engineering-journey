class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplet = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate anchors
            if nums[i] > 0:
                break  # sorted + positive anchor means no triplet can sum to 0

            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    triplet.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1  # skip duplicate j's
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1  # skip duplicate k's
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return triplet