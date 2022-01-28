ROTATION_DICTIONARY = {
    'j': ['y', 1, 90, False], 'f': ['y', 1, -90, False],        # U and U'
    'i': ['x', 1, 90, False], 'k': ['x', 1, -90, False],        # R and R'
    'h': ['z', -1, 90, False], 'g': ['z', -1, -90, False],      # F and F'
    's': ['y', -1, -90, False], 'l': ['y', -1, 90, False],      # D and D'
    'd': ['x', -1, -90, False], 'e': ['x', -1, 90, False],      # L and L'
    'w': ['z', 1, -90, False], 'o': ['z', 1, 90, False],        # B and B'

    'y': ['x', 1, 90, True], 'n': ['x', 1, -90, True],          # //
    't': ['x', 1, 90, True], 'b': ['x', 1, -90, True],          # x and x'
    'a': ['y', 1, 90, True], ';': ['y', 1, -90, True],          # y and y'
    'p': ['z', 1, 90, True], 'q': ['z', 1, -90, True], }        # z and z'
