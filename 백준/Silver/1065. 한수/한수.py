N = int(input())
print(len(list(filter(lambda a : a < 100 or 2 * int(str(a)[1]) == int(str(a)[0]) + int(str(a)[2]), [i for i in range(1, N+1)]))))
