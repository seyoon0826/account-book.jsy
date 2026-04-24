# pip install matplotlib

# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

# 가계부
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='NanumBarunGothic')
total_plus = 0
total_minus = 0
total_money = 0
minus = {}
plus = {}
cates = []
moniy = []
while True:     # 무한루프문
    a = input(
        "가계부 작성 (1: 지출, 2: 입금, 3: 지출총액 확인하기\n"
        "4: 입금총액 확인하기, 5: 총금액 확인하기, q: 종료하기): "    # 옵션 입력받기
    )
    print()

    if a == "1":
        print("지출내용 작성합니다.")
        cate, money = input("카테고리와 지출액을 입력해주세요: ").split()   # 딕셔너리의 키와 벨류값을 입력받기
        print()
        money = int(money)
        if cate not in minus:
            minus[cate] = [money]
        else:
            minus[cate].append(money)    # 키값이 없으면 새로 추가, 있으면 해당 키값의 Value인 리스트에 저장( 키값은 중복X )
        print(minus, "작성완료")
        print()

    elif a == "2":
        print("입금내용 작성합니다.")
        cate, money = input("카테고리와 입금액을 입력해주세요: ").split()
        print()
        money = int(money)
        if cate not in plus:
            plus[cate] = [money]
        else:
            plus[cate].append(money)    # 키값이 없으면 새로 추가, 있으면 해당 키값의 Value의 리스트에 저장
        print(plus, "작성완료")
        print()

    elif a == "3":
        print("지출 총액을 확인합니다.")
        total_minus = sum(sum(v) for v in minus.values())   # 마이너스 딕셔너리의 각Value들(리스트)의 총합의 총합
        print("지출한 총금액:", total_minus)
        print()
        print("카테고리별 지출 총합:")
        for cate, money_list in minus.items():
            print(f"{cate}: {sum(money_list)}")
        print()

    elif a == "4":
        print("입금 총액을 확인합니다.")
        total_plus = sum(sum(v) for v in plus.values())   # 플러스 딕셔너리도 ↑위에것과 마찬가지
        print("입금된 총금액:", total_plus)
        print()
        print("카테고리별 입금 총합:")
        for cate, money_list in plus.items():
          print(f"{cate}: {sum(money_list)}")
        print()

    elif a == "5":
        print("총금액(입금 - 지출)을 확인합니다.")
        total_minus = sum(sum(v) for v in minus.values())   # 모든 카테고리의 지출금액의 총합
        total_plus = sum(sum(v) for v in plus.values())     # 모든 카테고리의 입금금액의 총합
        total_money = total_plus - total_minus
        print("총금액:", total_money)
        print()

    elif a == "q":    # 무한루프를 종료하는 선택지
        print("지출:", minus)
        print("입금:", plus)
        print()
        # 가장 많이 입력된 카테고리
        count_cate = max(minus, key=lambda x: len(minus[x]))

        # 가장 많이 돈 쓴 카테고리
        money_cate = max(minus, key=lambda x: sum(minus[x]))

        print("가장 자주 지출한 카테고리:", count_cate)
        print("가장 많은 돈을 쓴 카테고리:", money_cate)
        print()
        if count_cate == money_cate:
          print(count_cate,"에 쓰는 돈을 줄이면 좋겠습니다.")   #  가장 자주 쓰는 카테고리와 가장 돈을 많이 쓴 카테고리가
        elif count_cate != money_cate:                          #  동일한 경우 하나만 출력
          print(count_cate, "와", money_cate, "에 쓰는 돈을 줄이면 좋겠습니다.")  # 가장 자주 쓰는 카테고리와 가장 돈을 많이 쓴 카테고리를 출력해줌
        else:
          print("아직 지출이 없어요!")
        print()
        total_minus = sum(sum(v) for v in minus.values())
        total_plus = sum(sum(v) for v in plus.values())
        total_money = total_plus - total_minus
        if total_money > (total_plus // 10):  # 입금-지출 이 입금의 총액의 1/10 보다 크면 칭찬해줌
          print(f"돈관리를 잘했습니다. {total_money}원 남았어요.")    # fstring을 이용한 출력

        for cate, money_list in minus.items():  # 여기부터는 그래프코드
          cates.append(cate)
          moniy.append(sum(money_list))
        plt.figure()
        x = np.arange(len(cates))
        plt.bar(x, moniy, color='skyblue')
        plt.xticks(x, cates)
        plt.show()
        print(total_money)
        break

    else:
        print("잘못된 선택지입니다.")
        print()
        p = input("종료하시겠습니까?(Y/N): ")
        if (p == "y" or p == "Y"):
          break