class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} # key - num, value - count
        frequent = []

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        # find k max values
        for i in range(k): #loop to find k frequent elements in group
            most_common = max(seen, key=seen.get)
            frequent.append(most_common)
            del seen[most_common]

        return frequent