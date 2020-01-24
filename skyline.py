# Given an iterable of buildings represented as triples (left, right,
# height), generate the co-ordinates of the skyline.

class BuildingPoint(object):
    def __init__(self, point, is_start, height):
        self.point = point
        self.is_start = is_start
        self.height = height


def get_skyline(buildings):
    building_points = []

    # Iterate through tuples to make points
    for left, right, height in buildings:
        building_points.append(BuildingPoint(left, True, height))
        building_points.append(BuildingPoint(right, False, height))

    building_points = sorted(building_points)

    queue = {}
    queue[0] = 1
    prev_max_height = 0
    result = []

    for point in building_points:
        if point.is_start:
            if point.height in queue:
                queue[point.height] += 1
            else:
                queue[point.height] = 1

        else:
            if queue[point.height] == 1:
                del queue[point.height]
            else:
                queue[point.height] -= 1

        current_max_height = max(queue.keys())

        if prev_max_height != current_max_height:
            result.append([point.point, current_max_height])
            prev_max_height = current_max_height

    return result



buildings = [(1,9,3), (1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25), (19,18,22), (23,13,29), (24,4,28)]