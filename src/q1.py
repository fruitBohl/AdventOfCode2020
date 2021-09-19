from collections import defaultdict


def readData(filename):
    data = []
    with open(filename) as infile:
        for line in infile:
            integer = int(line)
            data.append(integer)
    return data


def q1(nums, target):
    lookup = defaultdict(list)
    for i, num in enumerate(nums):
        needed = target - num
        if needed in lookup:
            return lookup[needed][0] * i
        lookup[num].append(i)

    return None


if __name__ == "__main__":
    data = readData("/Users/harrisonbohl/IdeaProjects/AdventOfCode2020/puzzleInputs/1stPuzzleInput.rtf")
    print(q1(data, 2020))
