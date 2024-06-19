def minFlips(a: int, b: int, c: int) -> int:
    flip = 0
    while a > 0 or b > 0 or c > 0:
        if c & 1 == 0:
            flip += (a & 1) + (b & 1)
        else:
            if a & 1 == 0 and b & 1 == 0:
                flip += 1

        a >>= 1
        b >>= 1
        c >>= 1
    return flip


print(minFlips(2, 6, 5)) # 3