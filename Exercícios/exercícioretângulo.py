position = [(5, 2)]
rec_position = [(6, 7), (6, 8), (7, 7), (7, 8)]


def check_position(pos, rec_pos):
    length = rec_pos.count(pos[0])
    if length != 0:
        return True
    else:
        return False


colision = check_position(position, rec_position)

print(colision)
