class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        max_area = 0
        
        while l < r:
            current_area = (r - l) * min(height[l], height[r])
            if current_area > max_area:
                max_area = current_area
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
