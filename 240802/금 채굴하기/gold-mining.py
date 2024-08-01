n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

#채굴에 드는 비용 
def get_cost(k):
    return k * k + (k+1) * (k+1)



# k에 따른 금 포획 

def get_gold(x, y, k):
    gold = 0

    # 2, 2   //   1 1, 1 2 1 3 , 2 1, 2 2, 2, 3 3 1 , 3 2 , 3 3  
    for i in range(n): 
        for j in range(n):
            if abs(x-i) + abs(y-j) <= k:
                gold += arr[i][j]

    return gold

max_gold = 0 


for i in range(n):
    for j in range(n):
        for k in range(n+1):
            num_of_gold = get_gold(i, j, k)

            if num_of_gold * m >= get_cost(k):
                
                max_gold= max(max_gold, num_of_gold )

print(max_gold)