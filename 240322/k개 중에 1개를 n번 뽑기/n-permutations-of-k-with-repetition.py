k , n = tuple(map(int, input().split()))
selected_nums = []

def print_sn():
    for n in selected_nums:
        print(f"{n}" , end=" ")

    print()


def find_sn(cnt):
    if cnt == n:
        print_sn()
        return
    
    for i in range(1, k+1):
        selected_nums.append(i)
        find_sn(cnt + 1)
        selected_nums.pop()

find_sn(0)