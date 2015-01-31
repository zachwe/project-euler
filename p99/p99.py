import math
max = 0
max_line_number = 0
with open("p099_base_exp.txt", "rb") as f:
    line_number = 0
    for line in f:
        line_number += 1
        base, exp = [int(i) for i in line.strip().split(",")]
        if math.log(base) * exp > max:
            max = math.log(base) * exp
            max_line_number = line_number
print max
print max_line_number
