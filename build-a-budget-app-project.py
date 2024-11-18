class Category:
    def __init__(self, name):
        self.ledger = []
        self.balance = 0
        self.name = name
        self.percent = 0
        self.spending = 0

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({"amount" : amount, "description" : description})
    
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount) == True:
            self.balance -= amount
            self.spending += amount
            self.ledger.append({"amount" : -amount, "description" : description})
            return True
        return False

                
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, dest):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f'Transfer to {dest.name}')
            self.spending -= amount
            dest.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return self.balance >= amount
    
    def __str__(self):
        title = ''
        title += self.name.center(30, '*')
        res = ''
        res += title + '\n'
        total = 0
        for i in self.ledger:
            d = i["description"][:23]
            if not 'deposit' in res:
                if 'Transfer' in i["description"]:
                    d = i["description"]
            a = f'{i["amount"]:.2f}'
            l = f'{d}' + a.rjust(len(title) - len(d)) + '\n'
            total += i["amount"]
            res += l
        t = f'Total: {total:.2f}'
        res += t
        return res

            
def create_spend_chart(categories):
    line = []
    line.append('Percentage spent by category')

    # Calculate the total spending and percentage spent by each category
    total_spent = sum([category.spending for category in categories])
    percentages = [(category.spending / total_spent) * 100 for category in categories]
    
    # Round down to the nearest 10 for each percentage
    percentages = [int(p // 10) * 10 for p in percentages]

    # Create the chart
    for i in range(100, -1, -10):
        row = f"{str(i).rjust(3)}| "
        for p in percentages:
            if p >= i:
                row += "o  "
            else:
                row += "   "
        line.append(row)

    # Add the horizontal line
    line.append("    -" + "---" * len(categories))

    # Find the longest category name
    max_len = max([len(category.name) for category in categories])

    # Add the category names vertically
    for i in range(max_len):
        row = "     "
        for category in categories:
            if i < len(category.name):
                row += category.name[i] + "  "
            else:
                row += "   "
        line.append(row)

    return "\n".join(line)

    # line = [''] * 13
    # line[0] = 'Percentage spent by category'
    # line[12] = '    -'
    # n = [i.name for i in categories]
    # lth = len(max(n, key = len))
    # line += ['     '] * lth
    # res = ''
    # a = list(range(110, -10, -10))
    # ts = sum([round(i.spending,2) for i in categories])
    # per = []
    # for i in range(1,12):
    #     line[i] += str(a[i]).rjust(3) + '| '
    # for i in categories:
    #     line[12] += '-' * 3
    #     i.name = i.name + ' ' * (lth - len(i.name))
    #     i.per = int(round(i.spending / ts * 100, -1))
    #     per.append(i.per)
    #     for b in range(0,lth):
    #         line[13 + b] += i.name[b] + '  '
    # for x in per: # per = [20, 20, 60]
    #     for i in range(11, 0, -1):
    #         if x >= 0:
    #             line[i] += 'o' + '  '
    #             x -= 10
    #         else: 
    #             line[i] += '   '

    # for lines in line:
    #     lines = lines.rstrip(' ')
    #     res += '\n' + lines

    # res = (res.replace('\n', '', 1))
    # return res
    
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
auto = Category("Auto")
food.transfer(50, clothing)
food.transfer(100, auto)
clothing.withdraw(30.50, 't-shirt')
auto.withdraw(70.30, "engine")

print(food)
print(
    (create_spend_chart([food, clothing, auto])))
