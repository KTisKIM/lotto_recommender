#################################################
#                                               #
#               Lotto Recommender               #
#       - Version: 0.2.5.5.20210801             #
#       - Writer: Keuntae Kim                   #
#       - Comment: Generating random nums,      #
#       but it doesn't do anything with         #
#       the data file yet.                      #
#                                               #
#################################################

import random
import csv
import pandas as pd

def read_lotto_history():
    """
    1회차 로또 당첨 번호 데이터부터 현재 로또 당첨 번호 데이터를 읽어들임.
    위쪽에서부터 제일 최신 회차. --> reversed list를 이용해 위쪽을 1회차로 만듬.
    """
    lotto_history_file = open('lotto_history.csv', encoding='utf-8')    # encoding 하지 않으면 error 발생.
    
    # get rid of first 3 lines in the CSV file
    for no_need in range(3):
        lotto_history_file.readline()
    csv_reader = csv.reader(lotto_history_file)
    
    all_lottery_nums = []
    
    # lottery[13]부터 lottery[18]까지 당첨번호, lottery[19]는 보너스번호
    # lottery[1]은 회차 번호.
    for lottery in reversed(list(csv_reader)):
        a = 0
        for lot_nums in lottery[13:20]:     # transfer from string to integer for the lottery numbers.
            lottery[13+a] = int(lot_nums)
            all_lottery_nums.append(lottery[13+a])  # to count the number of all_lottery_nums
            a += 1
        print(f"{lottery[1]}회차: {lottery[13:19]} + {lottery[19]}")    # 회차별 당첨번호 확인(보너스번호 포함)
    
    # 당첨번호별 출현 횟수
    num_lottery_nums = []
    
    for i in range(1,46):
        num_lottery_nums.append(all_lottery_nums.count(i))

def num_games():
    """
    총 5게임이며, 희망하는 게임 수(1-5)만큼 참여 가능.
    """
    num_game = int(input("총 몇 게임을 희망하시나요? (1-5)\n>>>>> "))
    if 0 < num_game < 6:
        print()
        print(f"{num_game}게임을 희망하셨습니다!")
        print()
        return num_game
    else:
        print()
        print(f"{num_game}게임을 희망하셨습니다. 하지만")
        print("5게임 초과, 혹은 1게임 미만은 불가능합니다!")
        print()
        return False

def lotto_recommend(games):
    """
    한 게임당 6개의 숫자를 선정.
    """
    for game in range(games):
        print(f"{game+1}번째 게임")
        lottery_for_user = random.sample(range(1,46), 6)
        lottery_for_user.sort()
        print(lottery_for_user)
    print()
    

def main():
    # read_lotto_history()
    games = num_games()
    lotto_recommend(games)

if __name__ == "__main__":
    main()