import os


def part_two():
    with open("input.txt") as ip:
        lines = ip.readlines()
        forward_total, depth_total, down_total, aim = 0, 0, 0, 0
        for line in lines:
            direction, magnitude = [x for x in line.split(" ")]
            if direction == "forward":
                forward_total += int(magnitude)
                depth_total += aim * int(magnitude)
            if direction == "down":
                aim += int(magnitude)
            if direction == "up":
                aim -= int(magnitude)

        ret = forward_total * depth_total
        print(ret)


def solve():
    with open("input.txt") as ip:
        lines = ip.readlines()
        forward_total, depth_total, down_total = 0, 0, 0
        for line in lines:
            direction, magnitude = [x for x in line.split(" ")]
            if direction == "forward":
                forward_total += int(magnitude)

            if direction == "down":
                depth_total += int(magnitude)
            if direction == "up":
                depth_total -= int(magnitude)

        ret = forward_total * depth_total
        print(ret)


if __name__ == "__main__":
    solve()
    part_two()
