class Budget:

    def __init__(self, category, amt):
        self.category = category
        self.amt = amt

    def deposit_funds(self, amount, reason):
        self.amount = amount
        self.reason = reason
        return ("You have deposited %s" % amount)

    def calc_balance(self):
        totalAmount = 0
        for item in self.category:
            totalAmount += item["amount"]
            return ("Your current balance is %s" %totalAmount)
    
    def withdraw_fund(self, amount, reason):
        return "This is a  method to withdraw funds for a category"

    def transfer_funds(self, amount, category):
        if(self.calc_balance(amount)):
            self.withdraw_fund(amount, "Transfer to" + category.name)
            category.deposit_funds(amount, "Transfer from" + self.category)
            return True
        return False
    
Clothing = Budget("Clothing", 1000)
Food = Budget("Food", 1000)
Entertainment = Budget("Entertainment", 1000)

Food.deposit_funds(1000, "Salary")
Food.withdraw_fund(200, "Party")
Food.calc_balance()

print(Clothing.deposit_funds(20000, "salary"))
print(Clothing.calc_balance())
print(Clothing.withdraw_fund(300, "Party"))
print(Clothing.transfer_funds(100, "more money"))