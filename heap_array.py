heap = [7, 6, 5, 8, 3, 5, 9, 1, 6]
heapLength = len(heap)

for i in range(1, heapLength):
    leaf = i

    ##먼저 max heap 구조로 바꾸는 과정
    while leaf != 0:
        root = (leaf-1)//2
        if heap[root] < heap[leaf]:
            temp = heap[root]
            heap[root] = heap[leaf]
            heap[leaf] = temp
        leaf = root

print('first heap is', heap)

##min heap으로 변환
for i in range(heapLength-1, -1, -1):
    temp = heap[i]
    heap[i] = heap[0]
    heap[0] = temp

    root = 0
    leaf = 1
    while leaf < i:
        leaf = root*2 + 1
        #자식중에 더 큰 자식 찾기
        #조건문 작성은 index 조건을 먼저 작성해야 오류발생하지 않는다
        #그 후에 요소조건(value)작성
        if leaf < i-1 and heap[leaf] < heap[leaf+1]:
            leaf = leaf + 1

        #부모노드가 자식노드보다 더 작은 경우 교환
        #조건문을 위 조건문과 따로 봐야한다(elif와 같이 이어지면 안됨)
        if leaf < i and heap[root] < heap[leaf]:
            temp = heap[root]
            heap[root] = heap[leaf]
            heap[leaf] = temp

        root = leaf
        print(heap)

print(heap)