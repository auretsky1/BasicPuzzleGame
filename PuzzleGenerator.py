""" This module can be called to generate a trigger list for any sized puzzle map. It stores the trigger list
    as a one-dimensional list of tuples where each tuple stores the cubes which that valued cube lights up. """


def generate_trigger_list(size=3):
    # todo: replace this function with the proper generation algorithm
    trigger_list = []
    for x in range(size**2):
        trigger_element_list = []
        trigger_element_list.append(x+1)
        trigger_list.append(trigger_element_list)
    return trigger_list