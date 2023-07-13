import sys
input = sys.stdin.readline

def dijkstra():


#주어진 값에 따라서 adjaency matrix를 활용하여 네트워크 그리기
#1번부터 다익스트라 알고리즘을 바탕으로 최소 경로 찾으면서 각각 노드를 연결한 값 list에 저장 -> 
#다 찾은 후에 list를 sorting하여 input으로 받은 무료로 제공되는 노선을 기준으로 list의 일부 slice
#그 중에 가장 큰 값만 return