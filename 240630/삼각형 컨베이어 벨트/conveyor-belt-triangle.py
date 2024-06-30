n, t = map(int, input().split())
u = list(map(int, input().split()))
m = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):

    temp_u = u[n-1]
    temp_m = m[n-1]

    for i in range(n-1, 0, -1):
        u[i] = u[i-1]
    u[0] = d[n-1]

    for i in range(n-1, 0, -1):
        m[i] = m[i-1]
    m[0] = temp_u

    for i in range(n-1, 0, -1):
        d[i] = d[i-1]
    d[0] = temp_m


for a in u :
    print(a, end=" ")
print()
for a in m :
    print(a, end=" ")
print()
for a in d :
    print(a, end=" ")
print()