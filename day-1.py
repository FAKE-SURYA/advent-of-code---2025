def count_zero_hits(rotations: list[str]) -> int:
    pos = 50
    count = 0

    for line in rotations:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        steps = int(line[1:])

        if direction == 'L':
            pos = (pos - steps) % 100
        elif direction == 'R':
            pos = (pos + steps) % 100
        else:
            raise ValueError(f"Unknown direction: {direction}")

        if pos == 0:
            count += 1

    return count
def read_input(path: str) -> list[str]:
    with open(path, 'r') as f:
        return f.readlines()


if __name__ == "__main__":
    rotations = read_input("input.txt")
    ans = count_zero_hits(rotations)
    print(ans)
