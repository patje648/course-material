import random
import grid


def shift_row_left(tiles):
    destination = 0
    current = 1
    has_changed = False

    while current < len(tiles):
        if tiles[destination] is None:
            if tiles[current] is not None:
                tiles[destination] = tiles[current]
                tiles[current] = None
                has_changed = True
            current += 1
        elif tiles[current] is None:
            current += 1
        elif tiles[destination] == tiles[current]:
            tiles[destination] *= 2
            tiles[current] = None
            destination += 1
            current += 1
            has_changed = True
        else:
            destination += 1
            current = max(current, destination + 1)

    return has_changed


def shift_grid_left(tiles):
    result = grid.copy(tiles)
    has_changed = any([shift_row_left(row) for row in result])
    return result, has_changed


def shift_grid_up(tiles):
    result = grid.rotate_ccw(tiles)
    result, has_changed = shift_grid_left(result)
    return grid.rotate_cw(result), has_changed


def shift_grid_right(tiles):
    result = grid.rotate_cw(grid.rotate_cw(tiles))
    result, has_changed = shift_grid_left(result)
    return grid.rotate_cw(grid.rotate_cw(result)), has_changed


def shift_grid_down(tiles):
    result = grid.rotate_cw(tiles)
    result, has_changed = shift_grid_left(result)
    return grid.rotate_ccw(result), has_changed


def is_filled(tiles):
    return all(all(x is not None for x in row) for row in tiles)


def add_random_tile(tiles):
    positions = [
        (x, y)
        for x in range(grid.width(tiles))
        for y in range(grid.height(tiles))
        if tiles[y][x] is None
    ]
    x, y = random.choice(positions)
    tiles[y][x] = random.choice([2, 4])


def print_grid(tiles):
    def format_tile(tile):
        if tile is not None:
            return str(tile).center(5, ' ')
        else:
            return '.'.center(5, ' ')

    for row in tiles:
        print("".join(format_tile(tile) for tile in row))


def input_direction():
    while (result := input()) not in "asdw":
        pass
    return result


def play():
    tiles = [[None] * 4 for _ in range(4)]
    add_random_tile(tiles)
    has_changed = True

    while not is_filled(tiles):
        if has_changed:
            add_random_tile(tiles)
        print_grid(tiles)
        match input_direction():
            case 'a':
                tiles, has_changed = shift_grid_left(tiles)
            case 's':
                tiles, has_changed = shift_grid_down(tiles)
            case 'd':
                tiles, has_changed = shift_grid_right(tiles)
            case 'w':
                tiles, has_changed = shift_grid_up(tiles)


if __name__ == '__main__':
    play()