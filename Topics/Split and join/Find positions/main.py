ds, find = input().split(), input()
indices = [i for i, x in enumerate(ds) if x == find]
print(" ".join(str(m) for m in indices) if indices else "not found")