from power_ca import PowerAgent, PowerBoard
import random


if __name__ == '__main__':
    n = 13
    empty_board = {}
    for i in range(n):
        for j in range(n):
            r1 = random.randint(0,100)
            if r1 < 60:
                r2 = (random.random() * 4)
                r3 = (random.random() * 4)
                empty_board[i,j] = PowerAgent((i,j), board_width=n, power=r2, desired_power=r3)
    b = PowerBoard(n, n, empty_board)
    print (len(b))

    for _ in range(1000):
        b.move_someone()
    print len(b)



