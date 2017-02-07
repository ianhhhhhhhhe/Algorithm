def ls(s, k):
    print(s)
    for c in set(s):
        print(c)
        if s.count(c) < k:
            temp = s.split(c)
            return max(ls(t, k) for t in temp)
    return len(s)

if __name__ == '__main__':
    print(ls('abababaaasdf', 2))
