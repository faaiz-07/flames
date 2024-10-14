import re

def get_data_1(name_1):
    return bool(re.match(r"^[a-zA-Z ]*$", name_1))

def get_data_2(name_2):
    return bool(re.match(r"^[a-zA-Z ]*$", name_2))

def pros_data(name_1, name_2, col_list):
    name_1 = (
        sorted([x for x in name_1]) + ["" * i for i in range(len(name_2) - len(name_1))]
        if len(name_1) < len(name_2)
        else sorted([x for x in name_1])
    )
    name_2 = (
        sorted([y for y in name_2]) + ["" for i in range(len(name_1) - len(name_2))]
        if len(name_2) < len(name_1)
        else sorted([y for y in name_2])
    )
    col_list.append([(i, j) for i, j in zip(name_1, name_2) if i != j])
    return len(
        [
            z
            for z in [
                items for out_list in col_list for tup in out_list for items in tup
            ]
            if z != ""
        ]
    )

def flames(length):
    flames_board = ["F", "L", "A", "M", "E", "S"]
    duplicate_flames_board = ["F", "L", "A", "M", "E", "S"]
    for i in range(len(flames_board) - 1, 0, -1):
        flames_board = (
            (flames_board * (length // 2))[length : length + i]
            if len(flames_board) > length
            else (flames_board * (length // 2 + 1))[length : length + i]
        )
    return duplicate_flames_board.index(flames_board[0])

def formate(value):
    if value in [0, 1, 4, 5]:
        return "are"

    elif value == 2:
        return "is"

    else:
        return "will"

def result(value):
    result_word = [
        "Friends",
        "Lovers",
        "Only Affection",
        "Marriage",
        "Enimies",
        "Brother and Sister",
    ]
    return result_word[value]