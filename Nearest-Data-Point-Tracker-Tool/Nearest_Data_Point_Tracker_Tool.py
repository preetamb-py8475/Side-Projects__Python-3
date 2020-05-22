
def list__data_pt():
    length = input("\nEnter the Number of Data Point(s) :\t")
    try:
        if not length.isnumeric() or int(length) <= 0:
            raise Exception
    except Exception:
        print()
        print(length)
        print("ERROR !!!")
        print("Enter a Natural Number Greater than 0 !!!")
        exit(1)
    print("\nEnter your Numerical Data Point(s) :")
    a = []
    for _ in range(int(length)):
        i = input()
        try:
            if not i.isnumeric() and not isinstance(float(i), float):
                raise Exception
        except Exception:
            print()
            print(i)
            print("ERROR !!!")
            print("Enter 0 or any Positive or Negative Integer/Decimal !!!")
            exit(1)
        i = float(i)
        a.append(i)
    print("\nList of Your Data Point(s) :")

    return a


def nearest__data_pt():
    """
                    My Python Script : Nearest Data Point Tracker Tool
                    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """

    data = list__data_pt()
    print(data)
    x = input(f"\nEnter a Numerical Value :\t")
    try:
        if not x.isnumeric() and not isinstance(float(x), float):
            raise Exception
    except Exception:
        print()
        print(x)
        print("ERROR !!!")
        print("Enter 0 or any Positive or Negative Integer/Decimal !!!")
        exit(1)
    x = float(x)
    c = []
    for _ in data:
        b = x - _
        b = abs(b)
        c.append(b)
    d = min(c[0:len(c)])
    print("\n")
    data_single = []
    data_multiple = []
    i = 0
    for c[i] in c:
        if c.count(c[i]) > 1 and d == c[i]:
            data_multiple.append(data[i])
        elif c.count(c[i]) == 1 and d == c[i]:
            data_single.append(data[i])
        i += 1
    print()
    if data_single != []:
        return f"From your List, Nearest Data Point to your Numerical Value --- '{x}' :\t'''{data_single}'''"
    elif data_multiple != []:
        return f"From your List, Nearest Data Point to your Numerical Value --- '{x}' :\t'''{data_multiple}'''"


# print(nearest__data_pt())
