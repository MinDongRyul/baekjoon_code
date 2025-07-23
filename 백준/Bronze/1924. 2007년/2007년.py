months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 'SUN, MON, TUE, WED, THU, FRI, SAT, SUN'.split(', ')
x, y = map(int, input().split())

print(days[(sum(months[:x-1]) + y) % 7])