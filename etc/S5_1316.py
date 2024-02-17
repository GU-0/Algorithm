import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    res = N
    for i in range(N):
        tmp = []
        bool_search = True
        for j in arr[i]:
            if bool_search:
                if j not in tmp:
                    tmp.append(j)
                elif j != tmp[-1]:
                    res -= 1
                    bool_search = False
    print(res)


if __name__ == "__main__":
    N = int(input().strip())
    arr = [list(input().strip()) for _ in range(N)]
    main()
