

def get_input():
    with open("input") as fp:
        output = [int(i) for i in fp.readlines()]
    return output

previous = None
cnt_inc = 0
a = get_input()
for i in range(len(a)):
    s = a[i:i+3]
    current = sum(s)
    if len(s) == 3:
        if previous == None:
            previous = current
            print(f"{current} (N/A)")
        elif previous == current:
            print(f"{current} (No change)")
        elif previous and previous > current:
            previous = current
            print(f"{current} (decrease)")
        elif previous and previous < current:
            previous = current
            print(f"{current} (increase)")
            cnt_inc += 1
    else:
        print(cnt_inc)
        exit(0)
