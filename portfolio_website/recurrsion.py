# import sys
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n==0:
#         return 1
#     return f(n-1)*n
# # print(f(1000))
import sys
sys.setrecursionlimit(10**50)
def f(n):
    if n==0:
        return 1
    return f(n-1)*n
print(f(100000))