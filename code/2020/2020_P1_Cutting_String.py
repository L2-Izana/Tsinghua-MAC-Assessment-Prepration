import sys

def solve():
    input = sys.stdin.read().strip()
    pretty = input[0]
    pretties = []
    for c in input[1:]:
        if c == pretty[-1]:
            pretty+=c
        else:
            pretties.append(pretty)
            pretty = c
    pretties.append(pretty)
    print(len(pretties))
    for pretty in pretties:
        print(pretty)
if __name__ == "__main__":
    solve()