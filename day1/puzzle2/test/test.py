
a = [1,2,3,4,5,6]

for i in range(len(a)):
    s = a[i:i+3]
    if len(s) == 3:
      print(f"{i} : {s} = {sum(s)}")
    else:
        print("the end ...")
        exit(0)

