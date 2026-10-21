import time

def combi (n,k):
    if k == 0 or n == k:
        return 1
    else:
        return combi(n-1,k)+combi (n-1,k-1)

n=100
k=20

start = time.time()
print(combi (n,k))
end = time.time()

print(f"{end-start :.5f}초 걸림")