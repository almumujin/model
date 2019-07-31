import matplotlib.pyplot as plt
import matplotlib.patches as mpathes
import numpy as np
import random


# 初始位置的生成
def initial_room():
    coordinates = []
    for i in range(N):
        generated_data = [random.randint(1,row), random.randint(1,column)]
        if not generated_data in coordinates:
            coordinates.append(generated_data)
    for i in range(len(coordinates)):
        room[coordinates[i][0]][coordinates[i][1]] = 1
    for i in range(len(room)):
        for j in range(len(room)):
            if i == 0 or i==len(room)-1 or j==0 or j==len(room)-1:
                room[i][j] = 9
    for i in range(len(export)):
        room[export[i][0]][export[i][1]] = 8
    print(room)
    return


def create_flat():
    plt.xticks(np.arange(0,column+3,1.0))
    plt.yticks(np.arange(0,row+3, 1.0))
    plt.grid(linestyle='-')
    wall_bottom = mpathes.Rectangle((0, 0), column+2, 1, color='grey')
    wall_left = mpathes.Rectangle((0, 0), 1,  row+2, color='grey')
    wall_top = mpathes.Rectangle((0, row+1), column+2, 1, color='grey')
    wall_right = mpathes.Rectangle((column+1, 0), 1, row+2, color='grey')
    ax.add_patch(wall_bottom)
    ax.add_patch(wall_left)
    ax.add_patch(wall_right)
    ax.add_patch(wall_top)
    for i in range(len(export)):
        ax.add_patch(mpathes.Rectangle((export[i][1], export[i][0]), 1, 1, color='green'))


def visualization():
    for i in range(1, len(room)-1):
        for j in range(1, len(room)-1):
            if room[i][j] == 1.0:
                rect = mpathes.Rectangle((j, i), 1, 1, color='black')
                ax.add_patch(rect)
    plt.show()


def update_state():
    for i in range(1, len(room)-1):
        for j in range(1, len(room)-1):
            if room[i][j] == 1:
                if check_out(i, j):
                    room[i][j] = 0
                else:
                    move(i, j)
            else:
                pass


def move(i, j):
    if i > export[0][0]:
        if room[i-1][j-1] == 0:
            room[i][j] = 0
            room[i-1][j-1] = 1
        elif room[i-1][j] == 0:
            room[i][j] = 0
            room[i-1][j] = 1
        elif room[i][j-1] == 0:
            room[i][j] = 0
            room[i][j-1] = 1
        else:
            pass

    elif i < export[0][0]:
        if room[i+1][j+1] == 0:
            room[i][j] = 0
            room[i+1][j+1] = 0
        elif room[i+1][j] == 0:
            room[i][j] = 0
            room[i+1][j] = 1
        elif room[i][j+1] == 0:
            room[i][j] = 0
            room[i][j+1] = 1
        else:
            pass
    else:
        room[i][j] = 0
        room[i][j-1] = 1


def check_out(i, j):
    if i == export[0][0] and j == export[0][1]+1:
        return True
    elif i == export[0][0]+1 and j == export[0][1]:
        return True
    elif i == export[0][0]-1 and j == export[0][1]:
        return True
    else:
        return False


def main():
    create_flat()
    update_state()
    visualization()


if __name__ == '__main__':
    N, row, column = 5, 20, 20
    room = np.zeros((row+2, column+2))
    export = [(11, 0, 'E')]
    initial_room()
    #
    # fig, ax = plt.subplots()
    # create_flat()
    # visualization()
    while 1 in room:
        fig, ax = plt.subplots()
        main()