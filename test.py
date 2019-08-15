from generator import generate

width = 40
height = 40

map = generate(width, height, 40)

for y in range(height):
    for x in range(width):
        if map[x][y] == 1:
            print('#', end = ' ')
        else:
            print(' ', end = ' ')
    print()
