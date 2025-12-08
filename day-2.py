def is_invalid_part1(num):
    
    s = str(num)
    length = len(s)
    
    # Must be even length to split in half
    if length % 2 != 0:
        return False
    
    mid = length // 2
    return s[:mid] == s[mid:]

def is_invalid_part2(num):
   
    s = str(num)
    length = len(s)
    
    # Try all possible pattern lengths (from 1 to half the string)
    for pattern_len in range(1, length // 2 + 1):
        # Check if length is divisible by pattern length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            # Check if entire string is this pattern repeated
            if pattern * (length // pattern_len) == s:
                return True
    
    return False

def solve(input_ranges, part=1):
   
    total = 0
    check_func = is_invalid_part1 if part == 1 else is_invalid_part2
    
    # Parse ranges
    ranges = input_ranges.split(',')
    
    for r in ranges:
        start, end = map(int, r.split('-'))
        
        # Check each number in range
        for num in range(start, end + 1):
            if check_func(num):
                total += num
    
    return total


    
input_data = "1-14,46452718-46482242,16-35,92506028-92574540,1515128146-1515174322,56453-79759,74-94,798-971,49-66,601-752,3428-4981,511505-565011,421819-510058,877942-901121,39978-50500,9494916094-9494978970,7432846301-7432888696,204-252,908772-990423,21425-25165,1030-1285,7685-9644,419-568,474396757-474518094,5252506279-5252546898,4399342-4505058,311262290-311393585,1895-2772,110695-150992,567521-773338,277531-375437,284-364,217936-270837,3365257-3426031,29828-36350"
print(f"Part 1: {solve(input_data, part=1)}")
print(f"Part 2: {solve(input_data, part=2)}")
    