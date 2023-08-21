import sys

testData = int(sys.stdin.readline().strip())

for test in range(len(testData)):
    n = int(sys.stdin.readline().strip())
    data = map(int, sys.stdin.readline().strip().split())
    dp = [[0 for _ in range(len(n))] for _ in range(len(n))]
    