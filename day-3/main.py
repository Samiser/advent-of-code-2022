priority = lambda letter : ord(letter) - 96 if ord(letter) >= 97 else ord(letter) - 38
priority_bag = lambda items : list(map(priority, items))

def part1(items):
    pocket_pairs = map(lambda bag : [bag[:len(bag) // 2], bag[len(bag) // 2:]], map(priority_bag, items))
    print(sum(map(lambda pair : set(pair[0]).intersection(set(pair[1])).pop(), pocket_pairs)))

def part2(items):
    groups = zip(*[iter(map(priority_bag, items))] * 3)
    print(sum(map(lambda group : set(group[0]).intersection(group[1], group[2]).pop(), groups)))

if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.read().splitlines()
        part1(lines)
        part2(lines)
