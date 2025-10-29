def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

# Test cases
test_cases = [
    0,                # no 1-bits
    1,                # single 1-bit
    2147483647,       # 0x7FFFFFFF -> all 1s except sign bit (31 ones)
    4294967295,       # 0xFFFFFFFF -> all 1s (32 ones)
    2147483648        # 0x80000000 -> only the sign bit is 1
]

for n in test_cases:
    print(f"hammingWeight({n}) = {hammingWeight(n)}")
