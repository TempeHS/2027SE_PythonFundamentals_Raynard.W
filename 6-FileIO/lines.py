import sys


def main():
    if len(sys.argv) < 2:
        sys.exit
    if len(sys.argv) > 2:
        sys.exit


filename = sys.argv[1]
if not filename.endswith(".py"):
    sys.exit("Not valid file")

count = 0
for line in lines:
    strip = line.lstrip()
    if strip == "":
        continue
else:
    count += 1

print(count)
