#거스름돈을 가장 적은 화폐로 거슬러준다고 할 때

def greedy(value):

    result = 0

    result = result + value//500
    value = value % 500

    result = result + value//100
    value = value % 100

    result = result + value//50
    value = value % 50

    result = result + value//10

    return result


print(greedy(1260))
