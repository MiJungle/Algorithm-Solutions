import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()


def zero():
    ans =[]
    min = 2e9
    left =0
    right = len(liquid) -1
    while left < right:

        if liquid[left] + liquid[right] == 0:
            ans = [liquid[left], liquid[right]]
            return ans
        elif abs(liquid[left] + liquid[right]) < min:
            min = abs(liquid[left] + liquid[right]) 
            ans = [liquid[left], liquid[right]]
        elif liquid[left] + liquid[right] > 0:
            right -=1 
        elif liquid[left] + liquid[right] <0:
            left +=1   
    return ans

print(*zero(),end='')             
