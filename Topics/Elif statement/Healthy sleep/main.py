a = int(input())
b = int(input())
h = int(input())
if a <= h <= b:
    print("Normal")
if h < a:
    print("Deficiency")
if h > b:
    print("Excess")