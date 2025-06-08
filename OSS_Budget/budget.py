import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def daily_summary(self):
        today = datetime.date.today().isoformat()
        today_expenses = [e for e in self.expenses if e.date == today]

        if not today_expenses:
            print("\n오늘은 지출이 없습니다. 알뜰하게 보내셨네요!\n")
            return

        total = sum(e.amount for e in today_expenses)

        # 카테고리별 합산
        category_totals = {}
        for e in today_expenses:
            category_totals[e.category] = category_totals.get(e.category, 0) + e.amount
            
        top_category = max(category_totals, key=category_totals.get)

        advice = {
            "식비": "오늘은 배가 고프셨나봐요. 간식은 적당히!",
            "교통": "움직임이 많았던 하루였네요. 이동도 소비입니다!",
            "문화": "문화생활로 마음의 양식을 채우셨군요!",
            "쇼핑": "지름신 강림! 충동구매는 없었나요?"
        }
        tip = advice.get(top_category, "오늘도 좋은 소비 하셨네요!")

        print("\n오늘의 소비 요약")
        print(f"총 지출: {total}원")
        print(f"가장 많이 쓴 항목: {top_category}")
        print(f"조언: {tip}\n")
    def reset_expenses(self):
        self.expenses = []
        print("모든 지출 내역이 초기화되었습니다.\n")
