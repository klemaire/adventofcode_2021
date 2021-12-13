

def get_input():
    def get_fields(s):
        a = s.split()
        return a[0], int(a[1])
    with open("input") as fp:
        output = [get_fields(i) for i in fp.readlines()]
    return output

distance = 0
depth = 0
for action, dist in get_input():
    if action == "forward":
        distance += dist
    elif action == "down":
        depth += dist
    elif action == "up":
        depth -= dist
    else:
        raise ValueError("Bad action")
print(f"distance {distance}\ndepth {depth}")
print(distance * depth)
