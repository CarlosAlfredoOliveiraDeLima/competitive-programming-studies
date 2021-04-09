N = int(input())

for i in range(N):
    n2, n3, n5 = map(float, input().split())
    weightedAverages = (n2 * 2 + n3 * 3 + n5 * 5) / 10
    print('%.1f' % weightedAverages)
