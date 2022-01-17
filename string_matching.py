def findString(parent, pattern):
    parentSize = len(parent)
    patternSize = len(pattern)

    for i in range(parentSize-patternSize):
        finded = True
        for j in range(patternSize):
            if parent[i + j] != pattern[j]:
                finded = False
                #break는 가장 가까운 반복문을 탈출한다
                break
        # 2차 순회(탐색)이 완료된 후에 인덱스 출력
        if finded:
            return i
        # 2차 순회에 대해 break 후 다시 반복문을 수행하도록 하기 위해
        # continue를 작성하여 1차 순회를 다시 실행하도록
        continueㅌ   

        return -1

parent = "Hello World"
pattern = "llo W"



print(findString(parent, pattern))