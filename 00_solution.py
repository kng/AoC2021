# --- Day xx ---
# https://adventofcode.com/2021/day/xx

import time
simple = True
verbose = 1

if simple:
    # data = '123\n456\n789'.splitlines()  # multi line
    data = '1, 2, 3, 4'.split(', ')  # single line
else:
    file = open('00_input.txt', 'r')
    # data = file.read().splitlines()  # multi line
    data = file.read().strip().split(', ')  # single line


def main():
    start_time = time.time()

    if verbose > 0:
        print('data:\n{}'.format(data))

    # part 1
    for row in data:
        if verbose > 1:
            print('row {}'.format(row))
        # the actual calculations here

    middle_time = time.time()
    print("part 1 time elapsed: {} seconds".format(middle_time - start_time))

    # part 2

    end_time = time.time()
    print("part 2 time elapsed: {} seconds".format(end_time - middle_time))


if __name__ == '__main__':
    main()
