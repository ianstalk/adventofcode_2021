def problem_1(input):
    sorted_input = sorted(input)
    median = sorted_input[len(sorted_input) // 2]
    ans = 0
    for i in sorted_input:
        ans += abs(median - i)
    return ans


def problem_2(input):
    mean1 = sum(input) // len(input)
    mean2 = mean1 + 1
    ans1 = 0
    ans2 = 0
    for i in input:
        ans1 += triangle(abs(i - mean1))
        ans2 += triangle(abs(i - mean2))
    return min(ans1, ans2)


def triangle(v):
    return v * (v + 1) // 2