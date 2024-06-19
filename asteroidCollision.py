def asteroidCollision(asteroids):
    stk = []
    check = True
    while check:
        for asteroid in asteroids:
            if stk:
                if asteroid > 0:
                    if stk[-1] > 0:
                        stk.append(asteroid)
                    else:
                        if abs(stk[-1]) > abs(asteroid):
                            continue
                        elif abs(stk[-1]) == abs(asteroid):
                            stk.pop()
                        else:
                            stk.pop()
                            stk.append(asteroid)
                else:
                    if stk[-1] < 0:
                        stk.append(asteroid)
                    else:
                        if abs(stk[-1]) > abs(asteroid):
                            continue
                        elif abs(stk[-1]) == abs(asteroid):
                            stk.pop()
                        else:
                            stk.pop()
                            stk.append(asteroid)
            else:
                stk.append(asteroid)
            if not min(stk) < 0 < max(stk):
                check = False
    return asteroidCollision(stk)
    
print(asteroidCollision([5, 10, -5])) # [5, 10]
print(asteroidCollision([8, -8])) # []
print(asteroidCollision([10, 2, -5])) # [10]
print(asteroidCollision([-10, -2, -5])) 
print(asteroidCollision([10, 2, 5]))
