def problem_1(readings):
    increases = 0
    previous = 0
    
    for reading in readings:
        increases += int(previous and reading > previous)
        previous = reading

    return increases


def problem_2(readings):
    increases = 0
    previous = 0

    for i in range(len(readings)):
        reading = sum(readings[i : min(len(readings), i+3)])
        increases += int(previous and reading > previous)
        previous = reading

    return increases