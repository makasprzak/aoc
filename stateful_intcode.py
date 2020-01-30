import numpy as np


# def intcode(line: str, *cin):
#     elements = map(lambda x: x.strip(), line.split(","))
#     program = list(map(lambda e: int(e), elements))
#     return intcode_program(program, cin)

class StatefulIntcode:
    def __init__(self, program, cin, debug=False):
        self.i = 0
        self.program = program
        self.cin = cin
        self.input_idx = 0
        self.relative_base = 0
        self.debug = debug
        for _ in range(0, 1000):
            self.program.append(0)

    def enter_input(self, *cin):
        self.cin += cin
        return self.run()

    def log(self, str):
        if self.debug:
            print(str)

    def reset(self):
        self.i = 0
        self.relative_base = 0

    def run(self):
        output = []
        while self.program[self.i] != 99:
            opcode = self.program[self.i + 0]
            mode_3, mode_2, mode_1, op = decode_opcode(opcode)
            if op == 3:
                if self.input_idx >= len(self.cin):
                    self.log("Waiting for input")
                    return output, False
                if mode_1 == 2:
                    self.log("storing value {0} at address {1} with offset {2}".format(self.cin[self.input_idx], self.program[self.i + 1], self.relative_base))
                    self.program[self.relative_base + self.program[self.i + 1]] = self.cin[self.input_idx]
                else:
                    self.log("storing value {0} at address {1}".format(self.cin[self.input_idx], self.program[self.i + 1]))
                    self.program[self.program[self.i + 1]] = self.cin[self.input_idx]
                self.input_idx += 1
                self.i += 2
            elif op == 4:
                output_value = self.value(mode_1, self.i + 1)
                self.log("Output:" + str(output_value))
                # print(output_value)
                output.append(output_value)
                self.i += 2
            elif op == 5:
                self.log("if f({0}) > 0 jump to f({1}) [arg1: {2}, arg2: {3}]".format(self.i + 1, self.i + 2, self.value(mode_1, self.i + 1), self.value(mode_2, self.i + 2)))
                if self.value(mode_1, self.i + 1) > 0:
                    self.i = self.value(mode_2, self.i + 2)
                else:
                    self.i += 3
            elif op == 6:
                self.log("if f({0}) == 0 jump to f({1}) [arg1: {2}, arg2: {3}]".format(self.i + 1, self.i + 2, self.value(mode_1, self.i + 1), self.value(mode_2, self.i + 2)))
                if self.value(mode_1, self.i + 1) == 0:
                    self.i = self.value(mode_2, self.i + 2)
                else:
                    self.i += 3
            elif op == 7:
                self.log("if f({0}) < f({1}) jump to f({2}) [arg1: {3}, arg2: {4}, arg3: {5}]".format(self.i + 1, self.i + 2, self.i + 3, self.value(mode_1, self.i + 1), self.value(mode_2, self.i + 2), self.value(mode_2, self.i + 3)))
                if self.value(mode_1, self.i + 1) < self.value(mode_2, self.i + 2):
                    self.set_value(mode_3, self.i + 3, 1)
                else:
                    self.set_value(mode_3, self.i + 3, 0)
                self.i += 4
            elif op == 8:
                self.log("if f({0}) == f({1}) jump to f({2}) [arg1: {3}, arg2: {4}, arg3: {5}]".format(self.i + 1, self.i + 2, self.i + 3, self.value(mode_1, self.i + 1), self.value(mode_2, self.i + 2), self.value(mode_2, self.i + 3)))
                if self.value(mode_1, self.i + 1) == self.value(mode_2, self.i + 2):
                    self.set_value(mode_3, self.i + 3, 1)
                else:
                    self.set_value(mode_3, self.i + 3, 0)
                self.i += 4
            elif op == 9:
                self.log("set offset to f({0})".format(self.i + 1))
                self.relative_base += self.value(mode_1, self.i + 1)
                self.i += 2
            else:
                self.log("f({0}) = f({1}) {2} f({3}) [arg1: {4}, arg2: {5}]".format(self.i + 3, self.i + 1, '+' if op == 1 else '*', self.i + 2, self.value(mode_1, self.i + 1), self.value(mode_2, self.i + 2)))
                func = get_func(op)
                value = func(self.value(mode_1, self.i + 1), self.value(mode_2, self.i + 2))
                self.set_value(mode_3, self.i + 3, value)
                self.i += 4
        return output, True

    def run_and_print(self):
        out, done = self.run()
        for i in out[:-1]:
            print(chr(i), end='', flush=True)
        print(str(out[-1]))
        return done

    def set_value(self, mode, idx, value):
        if mode == 2:
            set_at_index = self.relative_base + self.program[idx]
        else:
            set_at_index = self.program[idx]
        if set_at_index >= len(self.program):
            self.program = self.program + list(np.zeros(1 + set_at_index - len(self.program), dtype=int))
        self.program[set_at_index] = value

    def value(self, mode, idx):
        if mode == 0:
            self.log("reading value at index: " + str(self.program[idx]))
            return self.program[self.program[idx]]
        elif mode == 2:
            self.log("reading value at index: " + str(self.relative_base + self.program[idx]))
            return self.program[self.relative_base + self.program[idx]] if len(self.program) > self.relative_base + self.program[idx] else 0
        else:
            self.log("reading value at index: " + str(self.relative_base + self.program[idx]))
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


def decode_opcode(opcode: int):
    return int(opcode / 10000), int(opcode / 1000) % 10, int(opcode / 100) % 10, opcode % 10
