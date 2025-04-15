def fence(n, k):
    for i in range(n):
        if (i + 1) % (k + 1) == 0:
            print(".", end="")
        else:
            print("#", end="")
    print()

fence(27, 4)
fence(13, 2)
fence(17, 1)
fence(54, 6)