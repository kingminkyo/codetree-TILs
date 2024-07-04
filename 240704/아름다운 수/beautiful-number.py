n = int(input())

ans = []

cnt = 0

def print_answer():
    global cnt
    for a in ans:
        print(a, end="")
    print(f" {cnt}" ,end="")
    print()



def check_beautiful():
    global cnt 
    check = []

    for a in ans:
        check.append(a)
        if len(check) > 0:
            for c in check:
                if a != c:
                    return 0
            
            if check[0] == len(check):
                for _ in range(len(check)):
                    check.pop()
        # print(check)
    if len(check) == 0:
        cnt += 1 
    


def choose(curr_num):

    if curr_num == n+1:
        # print_answer()
        check_beautiful()
        return
    
    for i in range(1, 5):
        ans.append(i)
        choose(curr_num + 1)
        ans.pop()


choose(1)

print(cnt)