def asteroidCollision(asteroids):
    stk = []
    for asteroid in asteroids:
        while stk and asteroid < 0 < stk[-1]:
            if stk[-1] < -asteroid:
                stk.pop()
            elif stk[-1] == -asteroid:
                stk.pop()
            break
        else:
            stk.append(asteroid)
    return stk

print(asteroidCollision([10, 2,-5])) # [10]
print(asteroidCollision([5, 10, -5])) # [5, 10]
print(asteroidCollision([8, -8])) # []
print(asteroidCollision([-2, -1,1,2])) # [-2, -1, 1, 2]
print(asteroidCollision([-2, -2,-2,1])) # [-2, -2, -2, 1] 