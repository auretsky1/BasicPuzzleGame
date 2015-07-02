""" This module can be called to generate a trigger list for any sized puzzle map. It stores the trigger list
    as a one-dimensional list of tuples where each tuple stores the cubes which that valued cube lights up. """
import random


def generate_trigger_list(size=3):
    # Seed the random number generator
    random.seed(None)

    trigger_list = []
    for x in range(size**2):
        trigger_element_list = [x+1]
        trigger_list.append(trigger_element_list)

    # Randomly select a series of numbers within the bounds of the puzzle board
    # to act as the 'correct' series of triggers to solve the puzzle

    # Get the maximum number that is possible for this grid size
    n_max = size**2

    # Select randomly the number of the moves to perform (max = n_max / 2)
    n_moves = random.randint((n_max // 2), n_max - 2)

    # A list which holds the numbers already used
    trigger_sequence_numbers = []

    # Randomly pick numbers from the board equal to n_moves
    for x in range(0, n_moves):
        while True:
            n_current = random.randint(1, n_max)
            if n_current not in trigger_sequence_numbers:
                break
        trigger_sequence_numbers.append(n_current)

    # A list which holds the possible values for each cubes trigger
    possible_triggers = [[] for y in range(0, n_max)]

    # A list which holds the number of times each value appears (1 through n_max)
    value_totals = [0 for y in range(0, n_max)]

    # Go to each cube in the series selected and randomly select number it will
    # light up based off of it's available options.
    for x in range(n_max):
        if x % size != 0:  # Cube is on far left of board
            possible_triggers[x].append(x - 1)
        if x % size != size - 1:  # Cube is on far right of board
            possible_triggers[x].append(x + 1)
        if x // size != 0:  # Cube is on the top of board
            possible_triggers[x].append(x - size)
        if x // size != size - 1:  # Cube is on the bottom of board
            possible_triggers[x].append(x + size)

        # Select the number of values that will be used for this specific cube
        number_of_triggers = random.randint(0, len(possible_triggers[x]))

        # Assign a number of possible triggers equal to the random number selected for number_of_triggers
        for y in range(0, number_of_triggers):
            while True:
                n_random_trigger = random.randint(0, len(possible_triggers[x]) - 1)  # Location in possible triggers to access
                n_trigger_selection = possible_triggers[x][n_random_trigger] + 1  # The cube we are going to trigger
                if n_trigger_selection not in trigger_list[x]:
                    break
            trigger_list[x].append(n_trigger_selection)  # Add the selected cube to this cube's trigger list

            # Update the totals for the cube added to the trigger list
            if (x + 1) in trigger_sequence_numbers:
                value_totals[n_trigger_selection - 1] += 1

        # Update the total for the chosen cube by 1 since all cubes light turn themselves on
        if (x + 1) in trigger_sequence_numbers:
            value_totals[x] += 1

    # Check the totals for each number and adjust at specific points accordingly.
    for x in range(len(value_totals)):
        if value_totals[x] % 2 == 0:
            set_flag = False  # Has the number that appeared an even number of times been corrected?
            while not set_flag:
                for y in possible_triggers[x]:
                    if y + 1 in trigger_sequence_numbers and x + 1 not in trigger_list[y]:
                        if random.randint(0, 1) == 0:
                            trigger_list[y].append(x + 1)
                            set_flag = True
                            break
                    elif y + 1 in trigger_sequence_numbers and x + 1 in trigger_list[y]:
                        if random.randint(0, 1) == 0:
                            trigger_list[y].remove(x + 1)
                            set_flag = True
                            break
                if x + 1 not in trigger_sequence_numbers and not set_flag:
                    trigger_list[x] = [x+1]
                    set_flag = True

    return trigger_list