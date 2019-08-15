import random

def generate(width, height, percentage):
    map = [[1 for i in range(height)] for j in range(width)]

    min_x = 1
    max_x = width - 2

    min_y = 1
    max_y = height - 2

    x = random.randint(min_x, max_x)
    y = random.randint(min_y, max_y)

    map_cells = width * height
    filled_cells = 0
    filled_percentage = 0

    previous_delta_x = 0
    previous_delta_y = 0

    while filled_percentage <= percentage:
        if map[x][y] == 1:
            map[x][y] = 0
            filled_cells += 1
            filled_percentage = filled_cells / map_cells * 100

        if random.choice([True, False]):
            delta_x = random.choice([1, -1, previous_delta_x])
            if x + delta_x < min_x or x + delta_x > max_x:
                x = x - delta_x
                previous_delta_x = -delta_x
            else:
                x = x + delta_x
                previous_delta_x = delta_x
        else:
            delta_y = random.choice([1, -1, previous_delta_y])
            if y + delta_y < min_y or y + delta_y > max_y:
                y = y - delta_y
                previous_delta_y = -delta_y
            else:
                y = y + delta_y
                previous_delta_y = delta_y

    return map
