class Student:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def work(self):
        # Логіка заробітку студента
        # Наприклад, можна використати рандомний генератор для визначення заробітку
        self.money += random.randint(10, 100)

    def spend_money(self, amount):
        # Логіка витрати грошей студента

        if self.money >= amount:
            self.money -= amount
        else:
            # Якщо недостатньо грошей, студент може піти на роботу
            self.work()

    def study(self):
        # Логіка навчання студента
        # Наприклад, можна викликати методи для вивчення різних предметів
        pass

    def solve_problems(self):
        # Логіка вирішення проблем студента
        # Наприклад, можна викликати методи для розв'язання різних завдань
        pass

    def live_one_year(self):
        # Логіка проживання студента протягом року
        for _ in range(365):
            self.study()
            self.solve_problems()
            self.spend_money(10)  # Припустимо, що студент витрачає по 10 одиниць грошей щодня

