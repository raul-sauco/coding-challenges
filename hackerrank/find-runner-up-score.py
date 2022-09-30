# Mini Max Sum
# 🟢 Easy
#
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
#
# Tags: Array

n = int(input())
i=0
#takes input, splits it and then convert it into integer
arr = list(map(int, input().split()))  
zes = max(arr)

while(i<n):
    if zes == max(arr):
        arr.remove(max(arr))
    i+=1

print(max(arr))
