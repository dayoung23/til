# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# c = list()
# for i in a:
#     if i in b:
#         c.append(i)

# print(c)    
# -------------다른 방법-------------------
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(list(a & b))

#완전탐색 알고리즘
def gcd_brute_force (a, b):
    t = min(a, b) 
    while t > 0:
        if a % t == 0 and b % t == 0: 
            return t 
        t -= 1 
    return 1 
def main():
    print(gcd_brute_force(32229,15267))

if __name__ == '__main__':
    main()

#유클리드 알고리즘
def gcd_euclidean_iterative (a, b):
    while b != 0:
        temp = a 
        a = b 
        b = temp % b 
    return a
def main():
    print(gcd_euclidean_iterative(32229,15267))

if __name__ == '__main__':
    main()