with open("input.txt") as f:
    text = f.read().strip()

top, _bottom = text.split("\n\n")  # ignoring IDs 

ranges = []
for token in top.split():
    lo, hi = map(int, token.split("-"))
    ranges.append((lo, hi))

# sort by start
ranges.sort(key=lambda x: x[0])

merged = []
cur_start, cur_end = ranges[0]

for s, e in ranges[1:]:
    if s > cur_end + 1:
        merged.append((cur_start, cur_end))
        cur_start, cur_end = s, e
    else:
        if e > cur_end:
            cur_end = e

merged.append((cur_start, cur_end))

ans = 0
for s, e in merged:
    ans += e - s + 1

print(ans)
