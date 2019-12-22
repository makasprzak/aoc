from day_7.sequence_combinator import get_combinations
from day_7.stateful_intcode import StatefulIntcode


def run_amps(program: []):
    combinations = get_combinations({5, 6, 7, 8, 9})
    max_out = -1000
    max_comb = []
    for combination in combinations:
        o = check_combination(program, combination)
        if o > max_out:
            max_out = o
            max_comb = combination
    print("Maximum output: ", max_out, "comb:", max_comb)


def check_combination(program: [], combination: []):
    try:
        print("checking combination " + str(combination))
        # programs = list(map(lambda c: set_program(program, c), combination))
        signals = []
        programs = []
        for i in range(0, 5):
            programs.append(StatefulIntcode(program.copy(), []))
            signals.append([combination[i]])
        i = 0
        signals[0].append(0)
        while True:
            inp = signals[i]
            prog = programs[i % 5]
            prog.cin += inp
            o, done = prog.intcode_program()
            i += 1
            if len(o) > 0:
                if len(signals) == i:
                    signals.append([o[0]])
                else:
                    signals[i].append(o[0])
            if i % 5 == 0 and done:
                break
        print("output = ", str(signals))
        return signals[-1][0]
    except Exception as e:
        print('error', e)
        return -1000







