# 💰 가계부 & 지출 시각화 프로젝트 (Personal Household Ledger)

나의 첫 번째 파이썬 프로젝트인 **가계부 프로그램**입니다. 
지출과 수입을 단순히 기록하는 것을 넘어, 데이터를 분석하고 시각화하여 사용자의 소비 습관을 관리해줍니다.

---

## 📽️ 발표 자료 (Links)
이 프로젝트의 기획과 결과에 대한 상세 내용은 아래 발표 자료에서 확인하실 수 있습니다.

* [📍 계획 발표 자료 보러가기](https://www.canva.com/design/DAG-dgw33Hw/we0_LhDW3ievCcx6Nsoe9w/edit)
* [🏁 최종 발표 자료 보러가기](https://www.canva.com/design/DAG-h0eGEFs/OP8Nr-_-HgaLlVNJFRs3UQ/edit)

---

## ✨ 주요 기능 (Key Features)

1. **지출 및 입금 기록**: 카테고리별로 금액을 입력하며, 동일 카테고리는 자동으로 누적 합산됩니다.
2. **실시간 통계**: 현재까지의 지출 총액, 입금 총액, 그리고 현재 잔액을 바로 확인할 수 있습니다.
3. **소비 패턴 분석**:
    * **빈도 분석**: 가장 자주 지출한 카테고리를 찾아냅니다.
    * **금액 분석**: 가장 많은 돈을 쓴 카테고리를 찾아냅니다.
    * **맞춤형 피드백**: 분석 결과를 바탕으로 절약이 필요한 항목을 조언해줍니다.
4. **재정 건전성 체크**: 총 수입의 10% 이상을 저축했을 경우 칭찬 메시지를 출력하여 동기를 부여합니다.
5. **데이터 시각화**: `matplotlib`을 사용하여 지출 내역을 막대그래프로 시각화합니다.

---

## 🛠️ 기술 스택 (Tech Stack)

* **Language**: Python 3
* **Libraries**: `matplotlib`, `numpy`
* **Environment**: Colab 및 Linux 환경 지원 (나눔바른고딕 한글 폰트 적용)

---

## 💻 설치 및 실행 방법 (Installation)

1. **필수 라이브러리 설치** <br>
```pip install matplotlib numpy```
2. **한글 폰트 설치 (Colab/Linux 사용 시)**<br>
```sudo apt-get install -y fonts-nanum```<br>
```!sudo fc-cache -fv```<br>
```!rm ~/.cache/matplotlib -rf```<br>
