def image():
    layers = []
    layer_id = 0
    row_id = 0
    col_id = 0
    row = []
    layer = []
    with open('./input.txt', 'r') as f:
        c = f.read(1)
        i = 0

        while c:
            if col_id % 25 == 0:
                row = []
                if row_id % 6 == 0:
                    layer = []
                    layers.append(layer)
                    layer_id += 1
                layer.append(row)
                row_id += 1
            row.append(c)
            col_id += 1

            i += 1
            c = f.read(1)
        print(len(layers))

    least_0 = min(layers, key=lambda l: count('0', l))
    print("Answer 1: ", str(count('1', least_0) * count('2', least_0)))
    for y in range(0, 6):
        for x in range(0, 25):
            for l in range(0, 100):
                c = layers[l][y][x]
                if c != '2':
                    print('*' if c == '1' else ' ', end='')
                    break
        print()

def count(c, layer):
    i = 0;
    for row in layer:
        for col in row:
            if col == c:
                i += 1
    return i

if __name__ == '__main__':
    image()
