def problem_1(readings):
    frequencies = frequencies_by_pos(readings)

    gamma = frequencies_to_string(frequencies, most_common_bit)
    epsilon = frequencies_to_string(frequencies, least_common_bit)

    return bits_to_int(gamma) * bits_to_int(epsilon)

def problem_2(readings):
    oxygen = filter_readings(readings, most_common_bit)
    co2 = filter_readings(readings, least_common_bit)

    return bits_to_int(oxygen) * bits_to_int(co2)

def filter_readings(readings, string_func):
    filtered = readings

    for i in range(len(readings[0])):
        frequencies = frequencies_by_pos(filtered)
        bit = string_func(*frequencies[i])
        filtered =  [reading for reading in filtered if reading[i] == bit]
        
        if len(filtered) == 1: return filtered[0]

def frequencies_by_pos(readings):
    positions = [[0, 0] for _ in range(len(readings[0]))]

    for reading in readings:
        for i in range(len(reading)):
            positions[i][int(reading[i])] += 1

    return positions

def bits_to_int(bits):
    return int(bits, 2)

def most_common_bit(x, y):
    return "1" if x <= y else "0"

def least_common_bit(x, y):
    return "0" if x <= y else "1"

def frequencies_to_string(frequencies, string_func):
    return "".join([string_func(x, y) for x, y in frequencies])
