import sys
import copy
read = sys.stdin.readline

def anagram(s1, s2):
    c1 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1
    
    arr = copy.deepcopy(c1)

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(arr)):
        arr[i] *= 2

    if arr == c1:
        return True
    else:
        return False

T = int(read())

for _ in range(T):
    A, B = map(str, read().rstrip().split())

    if anagram(A, B):
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')