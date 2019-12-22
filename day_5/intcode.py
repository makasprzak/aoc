import copy


def intcode(line: str, *cin):
    elements = map(lambda x: x.strip(), line.split(","))
    program = list(map(lambda e: int(e), elements))
    i = 0
    input_idx = 0
    while program[i] != 99:
        opcode = program[i + 0]
        mode_2, mode_1, op = decode_opcode(opcode)
        if op == 3:
            program[program[i+1]] = cin[input_idx]
            i += 2
        elif op == 4:
            print(value(mode_1, i+1, program))
            i += 2
        elif op == 5:
            if value(mode_1, i+1, program) > 0:
                i = value(mode_2, i+2, program)
            else:
                i += 3
        elif op == 6:
            if value(mode_1, i+1, program) == 0:
                i = value(mode_2, i+2, program)
            else:
                i += 3
        elif op == 7:
            if value(mode_1, i+1, program) < value(mode_2, i+2, program):
                program[program[i + 3]] = 1
            else:
                program[program[i + 3]] = 0
            i += 4
        elif op == 8:
            if value(mode_1, i+1, program) == value(mode_2, i+2, program):
                program[program[i + 3]] = 1
            else:
                program[program[i + 3]] = 0
            i += 4
        else:
            func = get_func(op)
            program[program[i + 3]] = func(value(mode_1, i+1, program), value(mode_2, i + 2, program))
            i += 4
    return program

def value(mode, idx, program):
    if mode == 0:
        return program[program[idx]]
    else:
        return program[idx]

def value_for(mode, input, param_value):
    if mode == 0:
        try:
            return input[param_value]
        except:
            raise Exception("requested index " + str(param_value))
    else:
        return param_value


def get_func(input):
    if 1 == input:
        return lambda x, y: x + y
    else:
        return lambda x, y: x * y


def prepare(input):
    reset_program(input, 12, 2)


def reset_program(input, noun, verb):
    input[1] = noun
    input[2] = verb


def run_procedure(input, noun, verb):
    reset_program(input, noun, verb)
    if input[1] != noun:
        raise Exception('PANIC')
    intcode(input)
    return input[0]


def lookup(input):
    for noun in range(0, 100):
        for verb in range(0, 100):
            result = run_procedure(copy.copy(input), noun, verb)
            if result == 19690720:
                return noun * 100 + verb


def decode_opcode(opcode: int):
    return int(opcode / 1000), int(opcode / 100) % 10, opcode % 10
