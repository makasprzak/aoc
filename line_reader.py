def process_lines(path, func):
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            func(line)


def read_lines(path):
    res = []
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            res.append(line)
            line = f.readline()
    return res


def process_lines_as_arrays(path, func):
    process_lines(path, lambda line: func(parse_array(line)))


def parse_array(line):
    elements = line.split(",")
    elements = map(lambda x: x.strip(), elements)
    return elements