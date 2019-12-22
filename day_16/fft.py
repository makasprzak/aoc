import numpy as np
from day_16.fft2 import create_digit_calculator, DigitCalculator


def int_phase(int_signal: [], times=1, offset=0, pg=1) -> []:
    int_out = []
    calculator = create_digit_calculator(int_signal)
    for i in range(len(int_signal)):
        digit = calculator.calculate_digit(i, offset=offset)
        int_out.append(digit)
    return int_out


def calculate_digit(sum_cache, i, int_signal, times=1):
    window_length = ((i + 1) * 4)
    reminder = len(int_signal) % window_length
    if reminder == 0:
        fft = signle_cycle_fft(sum_cache, i, int_signal, window_length)
        return (fft * times) % 10
    else:
        cycle = np.lcm(reminder, window_length) / reminder
        remaining_times = times % cycle
        effective_signal = int_signal * int(remaining_times)
        return signle_cycle_fft(sum_cache, i, effective_signal, window_length)


def signle_cycle_fft(sum_cache, i, int_signal, window_length):
    positives = 0
    negatives = 0
    for f in range(0, len(int_signal), window_length):
        sum1 = sum(int_signal[f:f + int(window_length / 4)])
        positives += sum1
        negatives += sum(int_signal[f+int(window_length/2):f+int(3*window_length/4)])
    fft = abs(positives - negatives) % 10
    return fft


def prepare_pattern(i, pattern):
    prepared_pattern = []
    for p in pattern:
        for _ in range(i + 1):
            prepared_pattern.append(p)
    return prepared_pattern


def do_calculate_digit(int_signal, prepared_pattern):
    digit = 0
    for j in range(len(int_signal)):
        digit += int_signal[j] * prepared_pattern[(j + 1) % len(prepared_pattern)]
    digit = abs(digit) % 10
    return digit


def to_str(int_signal: []):
    return ''.join(map(str, int_signal[:8]))


def decode(int_signal, offset, repeat, phases):
    print("Offset:", offset)
    original_len = len(int_signal)
    total = original_len * repeat
    print("TotalL:", total)
    print("Diff  :", original_len * repeat - offset)
    pgOffset = offset % original_len
    print("PgOff :", pgOffset)
    print("PgNumb:", int(offset / repeat))
    pgsLeft = int((total - offset) / original_len)
    print("PgsLft:", pgsLeft)
    # offset = offset % len(signal)
    int_signal = int_signal[pgOffset:] + (int_signal * pgsLeft)
    print(to_str(int_signal))
    for i in range(phases):
        int_signal = int_phase(int_signal, offset=offset)
        print("Phase", i + 1, ":", to_str(int_signal))
    return int_signal


if __name__ == '__main__':
    signal = "59766832516471105169175836985633322599038555617788874561522148661927081324685821180654682056538815716097295567894852186929107230155154324411726945819817338647442140954601202408433492208282774032110720183977662097053534778395687521636381457489415906710702497357756337246719713103659349031567298436163261681422438462663511427616685223080744010014937551976673341714897682634253850270219462445161703240957568807600494579282412972591613629025720312652350445062631757413159623885481128914333982571503540357043736821931054029305931122179293220911720263006705242490442826574028623201238659548887822088996956559517179003476743001815465428992906356931239533104"
    # signal = "12345678"
    offset = int(signal[:7])
    int_signal = list(map(int, signal))
    repeat = 10000
    decode(int_signal, offset, repeat, 100)
    exit()

