import random
import time
import datetime

# 랜덤 보상 목록 정의하기
reward_list = ["cake", "chocolate", "ice cream", "tour", "musical", "game", "꽝"]
empty_list = []


# 랜덤으로 보상 반환하기
def get_random_reward(reward_list):
    """
    보상 목록에서 무작위로 하나의 보상을 선택하여 반환합니다.

    Args:
        reward_list (list): 보상 항목들이 담긴 리스트

    Returns:
        str: 선택된 보상 항목

    Raises:
        ValueError: 보상 목록이 비어있는 경우
    """
    if not reward_list:
        raise ValueError("보상 목록이 비어있습니다. 보상 목록을 채워주세요!")

    return random.choice(reward_list)


# 반환된 보상에 따라 메시지 출력하기
def play_reward_game(reward_list):
    """
    랜덤 보상 게임을 실행합니다.
    get_random_reward 함수에서 반환된 보상으로 다음 조건문을 실행합니다.

    Args:
        reward_list (list): 보상 항목들이 담긴 리스트
    """
    try:
        current = datetime.datetime.now()
        print("오늘은", current.strftime("%Y년 %m월 %d일"), "입니다.")
        print("오늘의 보상은 무엇일까요?")
        print("두구두구🥁...")
        time.sleep(2)
        reward = get_random_reward(reward_list)

        if reward == "꽝":
            print("꽝💨 아쉽지만 다음 기회에~!")
        else:
            print(f"축하합니다🎉 오늘의 보상은 '{reward}' 입니다~!")

    except ValueError as e:
        print(f"오류 발생: {e}")


# 게임 실행하기
play_reward_game(reward_list)
# play_reward_game(empty_list)
