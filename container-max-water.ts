
function maxArea(height: number[]): number {
    let l: number = 0;
    let r: number = height.length - 1;
    
    let max_area: number = 0;
    let current_area: number;
    
    while (l < r) {
       current_area = (r - l) * Math.min(height[l], height[r]);
       if (current_area > max_area) {
           max_area = current_area;
       };
       if (height[l] < height[r]) {
           l++;
       } else {
           r--;
       };
    };
    return max_area;
};
