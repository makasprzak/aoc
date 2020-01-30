from line_reader import read_lines
from coords import Coords, Direction
from day_18.crawler import Crawler
from day_18.collect import collect, Collector


def load_world_map(path='./input.data'):
    lines = read_lines(path)
    world_map = dict()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] not in '.\n':
                world_map[Coords(x, y)] = lines[y][x]
    return world_map, len(lines[0]), len(lines)


def find_entry(world_map):
    for k, v in world_map.items():
        if v == '@':
            return k


def main():
    world_map, max_x, max_y = load_world_map(path='./test_file.data')
    crawler = Crawler(find_entry(world_map), Direction.right(), world_map, max_x, max_y)
    crawler.crawl()
    crawler.print()
    result = collect(crawler.root, Collector(0, dict()))
    print(result.last_distance, result.steps, result.last_key_at, result.keys, result.completed, result.closed)
    print("Answer:", result.last_key_at * 2 - result.last_distance)


if __name__ == '__main__':
    main()
    exit()

