final = []
for line in open("C:\\Users\\peque\\OneDrive\\Documents\\GitHub\\python-scripts\\AdventOfCode3.txt", "r"):
    size = int(len(line) / 2)
    half1 = []
    for i in range(0, int(size), 1):
        half1.append(line[i])
        print(half1)
    half2 = []
    for i in range(0, int(size), 1):
        half2.append(line[i+size])
    for i in range(0, size):
        if half1[i] in half2:
            print(half1[i])
            final.append(half1[i])
            break
print("".join(final))