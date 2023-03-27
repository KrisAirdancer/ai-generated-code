def next_state(rule, current_state):
    next_row = [0] * len(current_state[0])
    for i in range(1, len(current_state[0])-1):
        neighbors = [current_state[j][i-1:i+2] for j in range(len(current_state))]
        index = int("".join(str(n) for n in neighbors[1]), 2)
        next_row[i] = int(rule >> (7-index) & 1)
    return next_row

def cellular_automata(rule, num_rows):
    state = [[0] * 101]
    state[0][50] = 1
    for i in range(num_rows-1):
        next_row = next_state(rule, state[-1:])
        state.append(next_row)
    for row in state:
        print("".join(str(i) for i in row))

rule = int(input("Enter the rule as a decimal value (0-255): "))
num_rows = int(input("Enter the number of rows to generate: "))
cellular_automata(rule, num_rows)
