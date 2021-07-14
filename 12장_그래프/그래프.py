def 셋():
    a,b,c,d,e,f = range(6) # 6개 노드 0 1 2 3 4 5
    N= [{b,c,d,f}, {a,d,f}, {a,b,d,e}, {a,e}, {a,b,c}, {b,c,d,e}]

    print(N)
    print(b in N[a]) # 멤버십 테스트
    print(b in N[b])
    print(len(N[f]))


def 리스트():
    a, b, c, d, e, f = range(6)  # 6개 노드 0 1 2 3 4 5
    N = [[b,c,d,f], [a,d,f], [a,b,d,e], [a,e], [a,b,c], [b,c,d,e]]

def 딕셔너리():
    a, b, c, d, e, f = range(6)
    N= [{b:2, c:1, d:4, f:1}, {a:4, d:1, f:4}, {a:1, b:1, d:2, e:4}, {a:3, e:2},
        {a:3, b:4, c:1}, {b:1, c:2, d:4, e:3}]

if __name__ == "__main__":
    셋()