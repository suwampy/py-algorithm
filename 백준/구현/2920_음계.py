from collections import deque

if __name__ == "__main__":
    a = list(map(int,input().split()))

    asc = True
    des = True

    for i in range(1,8):
        if a[i] > a[i-1]:
            des=False
        elif a[i] < a[i-1]:
            asc =False

    if asc:
        print("ascending")
    elif des:
        print("descending")
    else:
        print("mixed")