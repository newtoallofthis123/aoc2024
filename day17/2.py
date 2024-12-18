with open(0) as file:
    content = file.read().strip().split("\n\n")

register = {}
for line in content[0].splitlines():
    line = line.strip("Register ")
    letter, num = line.split(": ")
    register[letter] = int(num)

line = content[1].strip("Program: ")
program = list(map(int, line.split(",")))

def rev_combo(op) -> int:
    if op in [0, 1, 2, 3]:
        return op
    if op == register["A"]:
        return 4
    if op == register["B"]:
        return 5
    if op == register["C"]:
        return 6

    print("Invalid opcode:", op)
    return -1


global detect_jump, ins_incr, ins_pointer
ins_pointer = 0
ins_incr = 2

output = []


def operate(opcode, ins):
    global ins_incr, ins_pointer
    if opcode == 0:
        res = int(register["A"] / (1 << combo(ins)))
        register["A"] = res
    elif opcode == 1:
        res = register["B"] ^ ins
        register["B"] = res
    elif opcode == 2:
        res = combo(ins) % 8
        register["B"] = res
    elif opcode == 3:
        if register["A"] == 0:
            pass
        else:
            ins_pointer = ins
            print("Jump detected to", ins)
            if ins_pointer == 3:
                ins_incr = 0
    elif opcode == 4:
        register["B"] = register["B"] ^ register["C"]
    elif opcode == 5:
        output.append(combo(ins) % 8)
    elif opcode == 6:
        res = int(register["A"] / (1 << combo(ins)))
        register["B"] = res
    elif opcode == 7:
        res = int(register["A"] / (1 << combo(ins)))
        register["C"] = res
    else:
        print("Invalid opcode:", opcode)


print(register, program)

while ins_pointer < len(program):
    opcode = program[ins_pointer]
    ins = program[ins_pointer + 1]

    ins_pointer += ins_incr

    print("Opcode:", opcode, "Instruction:", ins)
    operate(opcode, ins)

print(register, output)
print(','.join(map(str, output)))
