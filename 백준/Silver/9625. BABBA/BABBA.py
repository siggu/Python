'''
1 : 0, 1(B)
2 : 1, 1(AB)
3 : 1, 2(BBA)
4 : 2, 3(BABAB)
5 : 3, 5(BABBABBA)
6 : 5, 8(BABBABABBABAB)
'''
import sys
read = sys.stdin.readline

k = int(read())
dp_A = [0, 0, 1, 1] + [0] * 42
dp_B = [0, 1, 1, 2] + [0] * 42

for i in range(3, 46):
    dp_A[i] = dp_A[i-1] + dp_A[i-2]
    dp_B[i] = dp_B[i-1] + dp_B[i-2]

print(dp_A[k], dp_B[k])