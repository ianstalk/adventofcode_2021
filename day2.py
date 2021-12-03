def command_value(direction, count):
    if direction == "forward":
        return int(count), 0
    elif direction == "down":
        return 0, int(count)
    elif direction == "up":
        return 0, -int(count)
    else:
        return 0, 0

def problem_1(commands):
    horizontal, depth = 0, 0
    for command in commands:
        delta_h, delta_d = command_value(*command.split(" "))
        
        horizontal += delta_h
        depth += delta_d

    return horizontal * depth

def problem_2(commands):
    horizontal, depth, aim = 0, 0, 0
    for command in commands:
        delta_h, delta_a = command_value(*command.split(" "))

        horizontal += delta_h
        aim += delta_a
        depth +=  aim * delta_h if delta_h else 0

    return horizontal * depth