#!/usr/bin/env python3


def main(payload):
    """ Main logic to read the payload information
    and then identify the longest switched on bulb streak
    and corrdinates for the k flips to take place.
    """
    lines = payload.split('\n')
    iterations = int(lines[0])

    for i in range(iterations):
        bulbs_total = int(lines[i*3 + 1])
        bulbs_to_switch_on = int(lines[i*3 + 2])
        bulbs_states = lines[i*3 + 3].split(' ')

        # We will scan through the array bulb_states
        # and try to create a maximum window having states
        # of switched off bulbs <= the ones which we can switch
        # on.

        # left and right are the pointers to the
        # endpoints of the window which needs to be
        # created for scanning.
        left = 0
        right = 1
        current_streak = 0

        best_coordinates = []
        longest_streak = 0

        while (left < right and right <= bulbs_total):

            # print(f"left: {left}, right: {right}, can_be_switched_on: {bulbs_to_switch_on}")
            count = switched_off_count(bulbs_states[left:right])
            # print(f"switched_off_count: {count}")

            if count <= bulbs_to_switch_on:
                current_streak += 1

                if current_streak > longest_streak:
                    longest_streak = current_streak
                    best_coordinates = get_switched_off_coordinates(
                        left,
                        bulbs_states[left:right])
                    # print(best_coordinates)

                # Before continuing, expand the window on the right
                # side to be able to increase our streak
                right += 1

            else:
                # Shrink the streak now
                # and also contract the window by moving
                # the left pointer
                current_streak -= 1
                left += 1

        print(longest_streak)
        print(*best_coordinates)


def switched_off_count(states_array):
    """Simply count the switched off bulbs in
    the states array.
    input  = ["1", "0", "1"]
    output = 1
    """
    resp = 0
    for i in states_array:
        if i == '0':
            resp += 1

    return resp


def get_switched_off_coordinates(offset, states_array):
    """ Construct a list of coordinates or idxs
    of the positions where the value is "0".

    offset: This is required to calculate the position
    of the coordinates in the final array as we only get
    a subset of the window array.

    states_array: Subset of the window for which we
    need to identify the coordinates.
    """
    coordinates = []
    for i in range(len(states_array)):
        if states_array[i] == "0":
            coordinates.append(i + offset)

    return coordinates


if __name__ == "__main__":
    with open('input.txt') as f:
        main(f.read())
