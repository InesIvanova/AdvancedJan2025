from shutil import which
def create(n):
    seq = [0, 1]

    for _ in range(n-2):
        prev  = seq[-1]
        prev2 = seq[-2]
        current = prev + prev2
        seq.append(current)
    return seq


def start(command):
    while command != "stop":
        data = command.split()
        if data[0] == "Create":
            n = int(data[-1])
            seq = create(n)
            print(*seq)
        elif data[0] == "Locate":
            num = int(data[-1])
            try:
                print(f"The number - {num} is at index {seq.index(num)}")
            except ValueError:
                print(f"The number {num} is not in the sequence")
            except NameError:
                print("Please first create a sequence")
        command = input()