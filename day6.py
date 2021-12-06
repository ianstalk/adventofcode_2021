from collections import deque

def problem_1(input):
    return run_simulation(input, 80)

def problem_2(input):
    return run_simulation(input, 256)

def run_simulation(input, num_days):
    timers = deque([0 for _ in range(9)])

    for i in input:
        timers[i] += 1

    for _ in range(num_days):
        zeroes = timers.popleft()
        timers.append(zeroes) # all the zeroes spawn as 8
        timers[6] += zeroes # add new sixes

    return sum(timers)

