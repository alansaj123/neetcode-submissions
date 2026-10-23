class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        max_area = 0

        while left < right: #needs to change
            current_window_size = right - left
            current_area = min(heights[right], heights[left]) * current_window_size

            max_area = max(max_area, current_area)

            if heights[right] > heights[left]:
                left +=1
            else:
                right -=1

        return max_area
                