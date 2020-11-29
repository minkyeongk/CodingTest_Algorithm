
n = int(input())
army = list(map(int, input().split()))

def func(front, back):
    print(front, back)
    global army
    if back > len(army)-1:
        return 0
    if army[front] > army[back]:
        front, back = front+1, back+1
        func(front, back)
    else:
        when_front = func(front, back+1) + 1
        pick_front = 0
        for x in army[:back]:
            pick_front = pick_front + 1 if x <= army[back] else pick_front
        when_back = pick_front + func(back, back+1)
        return min(when_front, when_back)

print(func(0, 1))


