a = input()


def is_palindrome(n):
    for i in range (len(n)):
        if n[i] != n[len(n) - 1 - i]:
            return False

    return True

if is_palindrome(a) :
    print("Yes")
else:
    print("No")