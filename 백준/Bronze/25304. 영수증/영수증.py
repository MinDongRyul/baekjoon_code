def func(tot_price : int) -> str:
    for _ in range(int(input())):
        price, num = map(int, input().split())
        tot_price -= price * num
    return 'Yes' if tot_price == 0 else 'No'

tot_price = int(input())
print(func(tot_price))