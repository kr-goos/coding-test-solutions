
def solution(clothes):
    clothes_dict = {}
    for name, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1  
        else:
            clothes_dict[kind] = 1   
    
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)  

    return answer - 1  

# defaultdict 를 이용한 방법 
def solution2(clothes):
    from collections import defaultdict

    clothes_dict = defaultdict(int)
    for _, kind in clothes:
        clothes_dict[kind] += 1
    
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)

    return answer -1


clothes = [
    [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
    [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]],
]

for c in clothes:
    print('clothes : ', c)
    print('result : ', solution(c))
