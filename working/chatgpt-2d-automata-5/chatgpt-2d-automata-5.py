def next_state(rule, current_state):
    # Pad the current state to allow the calculation of the next state
    padded_state = [0] + current_state + [0]
    next_row = [0] * len(current_state)
    for i in range(len(current_state)):
        # Get the neighborhood of the current cell
        neighbors = padded_state[i:i+3]
        if len(neighbors) == 3:
            # Convert the binary neighborhood to an integer index
            index = int("".join(str(n) for n in neighbors), 2)
            # Use the rule to determine the state of the next cell
            next_row[i] = (rule >> index) & 1
    return next_row


def cellular_automata(rule, num_rows):
    # Initialize the first row with a single live cell in the middle
    state = [[0] * 31]
    state[0][15] = 1
    for i in range(num_rows):
        # Calculate the next row based on the current state
        next_row = next_state(rule, state[-1])
        # Add the next row to the state
        state.append(next_row)
    # Print the state
    for row in state:
        print("".join(["#" if x else " " for x in row]))


# Prompt the user for the rule and the number of rows to generate
rule = int(input("Enter the rule as a decimal value (0-255): "))
num_rows = int(input("Enter the number of rows to generate: "))

# Generate and print the cellular automaton
cellular_automata(rule, num_rows)
