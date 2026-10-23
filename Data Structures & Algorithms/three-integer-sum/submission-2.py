class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array = sorted(nums)
        result = []

        for i in range(len(sorted_array)):
            if i > 0 and sorted_array[i] == sorted_array[i - 1]:
                continue

            left = i + 1
            right = len(sorted_array) -1

            while left < right:
                total = sorted_array[left] + sorted_array[right] + sorted_array[i]
                
                if total == 0:
                    result.append([sorted_array[left],sorted_array[right],sorted_array[i]])
                    right -=1
                    left +=1

                    while left < right and sorted_array[left] == sorted_array[left - 1]:
                        left += 1
                    while left < right and sorted_array[right] == sorted_array[right + 1]:
                        right -= 1

                elif total >0:
                    right -=1
                else:
                    left +=1

        return result

            


        