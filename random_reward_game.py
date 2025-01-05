import random

reward_list = ["cake", "chocolate", "ice cream", "tour", "musical", "game", "꽝"]

def solution(reward_list):
    a = random.randint(1, len(reward_list))
    print("오늘의 보상은 무엇일까요?")
    if reward_list[a] == "꽝":
        print("꽝! 아쉽지만 다음 기회에~!")
    else :
        print("오늘의 보상은", "'" + reward_list[a] + "'" + "입니다~!")

solution(reward_list)