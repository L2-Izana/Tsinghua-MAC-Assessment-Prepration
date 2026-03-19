import sys

def solve():
    input = sys.stdin.read().strip().split()
    k, s = input[0], input[1]
    for i in range(int(k)):    
        pretty = s[0]
        pretties = []
        for c in s[1:]:
            if c == pretty[-1]:
                pretty+=c
            else:
                pretties.append(pretty)
                pretty = c
        pretties.append(pretty)
        s = ''.join([str(len(pretty))+pretty[0] for pretty in pretties])
    print(s)
if __name__ == "__main__":
    solve()