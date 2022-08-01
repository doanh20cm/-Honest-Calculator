h = int(input())
for t in range(1, h + 1):
    print(" " * (h - t) + "#" * (2 * t - 1) + " " * (h - t))
