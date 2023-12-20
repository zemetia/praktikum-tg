import copy

N = 8

papan = [[-1 for _ in range(N)] for _ in range(N)]
STEPS = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

ketemu = False
counter = 0

def is_safe(loc, visited):
    x = loc[0]
    y = loc[1]

    return x >= 0 and x < N and y >= 0 and y < N and visited[x][y] == -1

def search(visited: list, pos = 0, curr = (0, 0)):
    global STEPS
    global N
    global counter

    # Lokasi bebas
    counter += 1
    print(str(counter) + '.', pos, curr)
    if pos == N ** 2: # and curr == (0, 0)
        return True

    for step in STEPS:
        next_step = (curr[0] + step[0], curr[1] + step[1])
        # print(is_safe(next_step, visited))
        if is_safe(next_step, visited):
            visited[next_step[0]][next_step[1]] = pos
            if(search(visited, pos+1, next_step)):
                return True
            
            visited[next_step[0]][next_step[1]] = -1

    return False


print(search(papan))
print(papan)