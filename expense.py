class Expense:
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self) -> str:
        return "<fExpense: {self.name}, {self.category}, Rs {self.amount: .2f}>"

