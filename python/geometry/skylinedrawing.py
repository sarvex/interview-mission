# https://leetcode.com/problems/the-skyline-problem/

class BuildingPoint(object):

    def __init__(self, point, is_start, height):
        self.point = point;
        self.is_start = is_start
        self.height = height
        
    def __lt__(self, other):
        if self.point != other.point:
            return self.point < other.point
        h1 = -self.height if self.is_start else self.height
        h2 = -other.height if other.is_start else other.height
        return h1 < h2
    
def get_skyline(buildings):

    building_points = []
    for building in buildings:
        building_points.extend(
            (
                BuildingPoint(building[0], True, building[2]),
                BuildingPoint(building[1], False, building[2]),
            )
        )
    building_points = sorted(building_points)

    queue = {0: 1}
    prev_max_height = 0
    result = []
    for building_point in building_points:
        if building_point.is_start:
            queue[building_point.height] = (
                queue[building_point.height] + 1
                if building_point.height in queue
                else 1
            )
        elif queue[building_point.height] == 1:
            del queue[building_point.height]
        else:
            queue[building_point.height] = queue[building_point.height] - 1

        current_max_height = max(queue.keys())

        if prev_max_height != current_max_height:
            result.append([building_point.point, current_max_height])
            prev_max_height = current_max_height
    return result

if __name__ == '__main__':
    buildings = [[1, 3, 4], [3, 4, 4], [2, 6, 2], [8, 11, 4], [7, 9, 3], [10, 11, 2]]
    print(get_skyline(buildings))
    
