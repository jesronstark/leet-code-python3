
s



s















class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                          bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Calculate the area of the first rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)
        # Calculate the area of the second rectangle
        area2 = (bx2 - bx1) * (by2 - by1)

        # Compute the overlapping rectangle's coordinates
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        # Calculate the area of the overlapping region
        overlap_area = overlap_width * overlap_height

        # Total area is sum of individual areas minus the overlapping area
        return area1 + area2 - overlap_area
