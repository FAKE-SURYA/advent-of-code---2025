def is_fresh(x, ranges):
    for lo, hi in ranges:
        if lo <= x <= hi:
            return True
    return False

with open("input.txt") as f:
    text = f.read().strip()

top, bottom = text.split("\n\n")  # ranges block, ids block
ranges = []
for token in top.split():
    lo, hi = map(int, token.split("-"))
    ranges.append((lo, hi))

ids = list(map(int, bottom.split()))

count = 0
for x in ids:
    if is_fresh(x, ranges):
        count += 1

print(count)
