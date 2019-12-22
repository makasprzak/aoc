import copy


# def intcode(line: str, *cin):
#     elements = map(lambda x: x.strip(), line.split(","))
#     program = list(map(lambda e: int(e), elements))
#     return intcode_program(program, cin)

class StatefulIntcode:
    def __init__(self, program, cin):
        self.i = 0
        self.program = program
        self.cin = cin
        self.input_idx = 0
        self.relative_base = 0
        for _ in range(0, 1000):
            self.program.append(0)

    def intcode_program(self):
        output = []
        while self.program[self.i] != 99:
            opcode = self.program[self.i + 0]
            mode_3, mode_2, mode_1, op = decode_opcode(opcode)
            if op == 3:
                if self.input_idx >= len(self.cin):
                    return output, False
                if mode_1 == 2:
                    self.program[self.relative_base + self.program[self.i + 1]] = self.cin[self.input_idx]
                else:
                    self.program[self.program[self.i + 1]] = self.cin[self.input_idx]
                self.input_idx += 1
                self.i += 2
            elif op == 4:
                output_value = self.value(mode_1, self.i + 1)
                # print(output_value)
                output.append(output_value)
                self.i += 2
            elif op == 5:
                if self.value(mode_1, self.i + 1) > 0:
                    self.i = self.value(mode_2, self.i + 2)
                else:
                    self.i += 3
            elif op == 6:
                if self.value(mode_1, self.i + 1) == 0:
                    self.i = self.value(mode_2, self.i + 2)
                else:
                    self.i += 3
            elif op == 7:
                if self.value(mode_1, self.i + 1) < self.value(mode_2, self.i + 2):
                    self.set_value(mode_3, self.i + 3, 1)
                else:
                    self.set_value(mode_3, self.i + 3, 0)
                self.i += 4
            elif op == 8:
                if self.value(mode_1, self.i + 1) == self.value(mode_2, self.i + 2):
                    self.set_value(mode_3, self.i + 3, 1)
                else:
                    self.set_value(mode_3, self.i + 3, 0)
                self.i += 4
            elif op == 9:
                self.relative_base += self.value(mode_1, self.i + 1)
                self.i += 2
            else:
                func = get_func(op)
                value = func(self.value(mode_1, self.i + 1), self.value(mode_2, self.i + 2))
                self.set_value(mode_3, self.i + 3, value)
                self.i += 4
        return output, True

    def set_value(self, mode, idx, value):
        if mode == 2:
            self.program[self.relative_base + self.program[idx]] = value
        else:
            self.program[self.program[idx]] = value

    def value(self, mode, idx):
        if mode == 0:
            return self.program[self.program[idx]]
        elif mode == 2:
            return self.program[self.relative_base + self.program[idx]]
        else:
            return self.program[idx]

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


# def run_procedure(input, noun, verb):
#     reset_program(input, noun, verb)
#     if input[1] != noun:
#         raise Exception('PANIC')
#     intcode(input)
#     return input[0]
#
#
# def lookup(input):
#     for noun in range(0, 100):
#         for verb in range(0, 100):
#             result = run_procedure(copy.copy(input), noun, verb)
#             if result == 19690720:
#                 return noun * 100 + verb


def decode_opcode(opcode: int):
    return int(opcode / 10000), int(opcode / 1000) % 10, int(opcode / 100) % 10, opcode % 10
