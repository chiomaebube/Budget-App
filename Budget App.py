class Budget:

    def __init__(self, category, amt):
        self.category = category
        self.amt = amt

    def deposit_funds(self):
        return "This is a deposit method"

    def calc_balance(self):
        return "This is a method to calculate the current balance of the category"
    
    def withdraw_fund(self):
        return "This is a  method to withdraw funds for a category"

    def transfer_funds(self):
        return "This is a method to tranfer funds between categories"

Clothing = Budget("Clothing", 1000)
Food = Budget("Food", 1000)
Entertainment = Budget("Entertainment", 1000)


print(Clothing.deposit_funds())
print(Clothing.calc_balance())
print(Clothing.withdraw_fund())
print(Clothing.transfer_funds())