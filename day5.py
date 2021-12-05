def problem_1(points):
    lines = [extrapolate_line(*p) for p in points if is_straight(*p)]
    return len(find_overlaps(lines))


def problem_2(points):
    lines = [extrapolate_line(*p) for p in points]
    return len(find_overlaps(lines))


def find_overlaps(lines):
    intersections = set()
    seen = set()

    for line in lines:
        intersections = intersections.union(seen.intersection(line))
        seen = seen.union(line)

    return intersections


def extrapolate_line(start, end):
    if not is_straight(start, end):
        return set(zip(inclusive_range(start[0], end[0]), inclusive_range(start[1], end[1])))
    elif is_vertical(start, end):
        return set([(start[0], y) for y in inclusive_range(start[1], end[1])])
    else:
        return set([(x, start[1]) for x in inclusive_range(start[0], end[0])])


def is_vertical(start, end):
    return start[0] == end[0]


def is_straight(start, end):
    return start[0] == end[0] or start[1] == end[1]


def inclusive_range(x, y):
    if x < y:
        return range(x, y + 1)
    else:
        return range(x, y - 1, -1)