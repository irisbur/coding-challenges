from ctypes import c_uint16 as unsigned_int16


def calculate_gate_a():
    with (open('input.txt') as f):
        lines = f.readlines()
        wires = {}

        while 'a' not in wires:
            for line in lines:
                line = line.split()

                if len(line) == 3:
                    if line[0].isnumeric():
                        wires[line[2]] = unsigned_int16(int(line[0]))
                    elif line[0] in wires:
                        wires[line[2]] = unsigned_int16(wires[line[0]].value)

                elif len(line) == 4:
                    if line[1] in wires:
                        wires[line[3]] = unsigned_int16(~wires[line[1]].value & 0xFFFF)

                elif len(line) == 5:
                    val1, val2 = line[0], line[2]
                    if not (is_valid(val1, wires) and is_valid(val2, wires)):
                        continue

                    if val1 in wires:
                        val1 = wires[val1].value
                    else:
                        val1 = int(val1)

                    if val2 in wires:
                        val2 = wires[val2].value
                    else:
                        val2 = int(val2)

                    res = None

                    if line[1] == "AND":
                        res = val1 & val2
                    elif line[1] == "OR":
                        res = val1 | val2
                    elif line[1] == "LSHIFT":
                        shifts = int(line[2])
                        res = val1 << shifts
                    elif line[1] == "RSHIFT":
                        shifts = int(line[2])
                        res = val1 >> shifts

                    wires[line[-1]] = unsigned_int16(res & 0xFFFF)

        print(wires)
        return wires['a'].value


def is_valid(val, wires):
    return val in wires or val.isnumeric()


print(calculate_gate_a())
