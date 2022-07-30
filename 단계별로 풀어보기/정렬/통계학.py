# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

# 둘째 줄에는 중앙값을 출력한다.

# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

# 넷째 줄에는 범위를 출력한다.

import sys
from collections import Counter
N = int(sys.stdin.readline())

nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))



nums_sum = sum(nums)




print(round(nums_sum / N))

nums.sort()

print(nums[N // 2])
# print(c)
# print(c[0], c[0][1])
c = Counter(nums).most_common()
if len(c) > 1 and c[0][1] == c[1][1]:
    print(c[1][0])
else:
    print(c[0][0])
print(max(nums) - min(nums))