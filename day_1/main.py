
import os

def part_two():
    with open("input_2.txt") as ip:
        lines = ip.readlines()
        k = 3
        start, end, increased = 0,3,0
        running_sum = sum([int(lines[x]) for x in range(3)])
        while start >=0 and end <= len(lines):
            inner_sum = 0
            for i in range(start, end, 1):
                depth = int(lines[i])
                inner_sum += depth
            if inner_sum > running_sum:
                increased += 1
            running_sum = inner_sum
            
            start += 1
            end += 1
        print(increased)

def solve():
    with open("input.txt") as ip:
        lines = ip.readlines()
        first = int(lines[0])
        increased = 0
        for line in lines:
            depth = int(line)
            if depth > first:
                increased += 1
                first = depth
            else:
                first = depth
        print(increased)
if __name__ == "__main__":
    solve()
    part_two()