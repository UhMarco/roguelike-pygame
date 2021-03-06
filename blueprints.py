# 1: wall / 10: player spawn / 11: enemy spawn / 12: key spawn / 13: potion spawn
# 15: enemy / 16: key / 17: potion
# 30: door / 31: exit

exit_blueprint = [
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 11, 1, 1, 1, 13, 0, 1,
    1, 0, 1, 31, 1, 1, 0, 1,
    1, 0, 1, 30, 30, 30, 0, 1,
    1, 0, 1, 1, 1, 1, 0, 1,
    1, 12, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1
]

blueprints = [
    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 12, 0, 1,
    1, 0, 13, 0, 0, 0, 0, 1,
    1, 0, 0, 10, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 11, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 0, 0, 1, 1, 1,
    1, 1, 0, 0, 0, 0, 1, 1,
    1, 0, 0, 12, 1, 0, 0, 1,
    1, 0, 0, 1, 0, 11, 0, 1,
    1, 1, 10, 0, 0, 13, 1, 1,
    1, 1, 1, 0, 0, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 1, 0, 1, 1, 0, 1,
    1, 0, 1, 0, 12, 1, 0, 1,
    1, 0, 13, 0, 11, 10, 0, 1,
    1, 0, 1, 1, 0, 1, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 12, 0, 0, 0, 0, 1,
    1, 0, 1, 1, 1, 1, 0, 1,
    1, 0, 1, 1, 1, 1, 10, 1,
    1, 0, 1, 1, 1, 1, 11, 1,
    1, 0, 1, 1, 1, 1, 0, 1,
    1, 0, 0, 13, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 1, 0, 0, 0, 0, 1,
    1, 0, 1, 12, 11, 1, 0, 1,
    1, 0, 1, 0, 10, 1, 0, 1,
    1, 0, 13, 0, 0, 1, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 1, 1, 1, 1, 0, 1,
    1, 0, 0, 10, 0, 0, 0, 1,
    1, 0, 11, 0, 12, 0, 0, 1,
    1, 0, 1, 1, 1, 1, 0, 1,
    1, 0, 13, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 13, 1,
    1, 0, 11, 0, 1, 1, 0, 1,
    1, 0, 0, 0, 1, 1, 0, 1,
    1, 0, 1, 12, 10, 0, 0, 1,
    1, 0, 1, 1, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 1, 1, 0, 11, 0, 1,
    1, 0, 1, 10, 0, 0, 0, 1,
    1, 0, 0, 0, 1, 1, 0, 1,
    1, 0, 12, 0, 1, 13, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 1, 0, 0, 1, 0, 1,
    1, 0, 0, 10, 0, 0, 0, 1,
    1, 0, 11, 0, 0, 0, 0, 1,
    1, 0, 1, 0, 0, 1, 12, 1,
    1, 13, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 1, 1, 11, 1, 13, 1,
    1, 0, 1, 1, 0, 1, 0, 1,
    1, 0, 12, 0, 10, 1, 0, 1,
    1, 0, 1, 1, 1, 1, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 12, 0, 1,
    1, 0, 0, 1, 1, 0, 0, 1,
    1, 0, 13, 1, 1, 0, 0, 1,
    1, 0, 0, 0, 11, 10, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 0, 0, 1, 1, 1,
    1, 1, 1, 0, 11, 1, 1, 1,
    1, 0, 13, 0, 12, 0, 0, 1,
    1, 0, 0, 10, 0, 0, 0, 1,
    1, 1, 1, 0, 0, 1, 1, 1,
    1, 1, 1, 0, 0, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1]
]