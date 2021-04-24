class Budget:

    def __init__(self, category, amt):
        self.category = category
        self.amt = amt

    def deposit_funds(self, amount, reason):
        self.amount = amount
        self.reason = reason
        return "This is a deposit method"

    def calc_balance(self, amount, reason):
        return "This is a method to calculate the current balance of the category"
    
    def withdraw_fund(self, amount, reason):
        return "This is a  method to withdraw funds for a category"

    def transfer_funds(self, amount, reason):
        return "This is a method to tranfer funds between categories"

Clothing = Budget("Clothing", 1000)
Food = Budget("Food", 1000)
Entertainment = Budget("Entertainment", 1000)

Food.deposit_funds(1000, "Salary")
Food.withdraw_fund(200)

print(Clothing.deposit_funds())
print(Clothing.calc_balance())
print(Clothing.withdraw_fund())
print(Clothing.transfer_funds())