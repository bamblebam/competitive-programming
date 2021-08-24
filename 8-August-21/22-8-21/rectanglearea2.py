from sortedcontainers import SortedSet


class Solution:
    def rectangleArea(self, rectangles) -> int:
        n = len(rectangles)
        mod = 10**9+7
        rows, cols = SortedSet(), SortedSet()
        row_map, col_map = dict(), dict()
        events = list()

        # adding elements to the row and col sets and adding the points where a specific x starts and ends by denoting them with 1 and -1.

        for x1, y1, x2, y2 in rectangles:
            rows.add(x1)
            rows.add(x2)
            cols.add(y1)
            cols.add(y2)
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))

        events.sort()
        # creating maps for finding the idx of the row or col
        for i, r in enumerate(rows):
            row_map[r] = i
        for i, c in enumerate(cols):
            col_map[c] = i

        # sections that the different y's split the grid into
        sections = [0]*len(cols)
        area = 0
        prev_x = events[0][0]

        # iterate over events and then iterate over the different sections and check if it is part of rectangle by checking the count at that position then update the area and update the section count.

        for x, delta, y1, y2 in events:
            dx = x-prev_x
            filled = 0
            for y in range(1, len(sections)):
                if sections[y-1] > 0:
                    filled += cols[y]-cols[y-1]
            area += dx*filled
            for y in range(col_map[y1], col_map[y2]):
                sections[y] += delta
            prev_x = x

        return area % mod
