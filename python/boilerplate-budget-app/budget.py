class Category:
    def __init__(self, name: str):
        self.name: str = name
        self.funds: float = 0
        self.ledger: list = []

    def __repr__(self):
        return "<Category name:%s>" % self.name

    def getTitleLine(self, lineLength=30) -> str:
        outString = ""
        starLength = (lineLength - len(self.name))//2
        for x in range(0, starLength):
            outString += "*"
        outString += self.name
        for x in range(0, starLength):
            outString += "*"
        if len(self.name)%2!=0:
            outString += "*"
        return outString

    def getItemLine(self, item: dict, maxLineLength=30, maxDescLength=23) -> str:
        descStr = item["description"][:maxDescLength]
        descLen = len(descStr)
        amountStr = str("%.2f" % item["amount"])
        amountLen = len(amountStr)
        fillLen = maxLineLength - amountLen - descLen
        fillStr = ""
        for x in range(0, fillLen):
            fillStr += " "
        return descStr + fillStr + amountStr


    def __str__(self):
        outString = ""
        # print title line
        outString += self.getTitleLine()
        outString += "\n"

        # print item lines
        for item in self.ledger:
            outString += self.getItemLine(item)
            outString += "\n"

        # print total line
        outString += "Total: " + str(self.funds)

        return outString

    def item(self, amount: float, description: str) -> dict:
        return {"amount": amount, "description": description}

    def deposit(self, amount: float, description: str=""):
        if amount >= 0.0:
            self.ledger.append(self.item(amount, description))
            self.funds += amount

    def withdraw(self, amount: float, description: str="") -> bool:
        if amount > 0.0 and self.check_funds(amount):
            self.ledger.append(self.item(-amount, description))
            self.funds -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.funds

    def check_funds(self, amount) -> bool:
        if amount <= self.funds:
            return True
        else:
            return False

    def transfer(self, amount: float, other: 'Category') -> bool:
        if amount > 0.0 and self.check_funds(amount):
            toDesc = "Transfer to " + other.name
            fromDesc = "Transfer from " + self.name
            self.withdraw(amount, toDesc)
            other.deposit(amount, fromDesc)
            return True
        else:
            return False


def create_spend_chart(categories):
    # calculate percentage spent
    percentages = []
    totalSpent = 0
    catSpent = []
    # get the amounts each category has spent
    for i in range(0, len(categories)):
        catSpent.append(0)
        for item in categories[i].ledger:
            if item["amount"] < 0.0:
                catSpent[i] += item["amount"]
        totalSpent += catSpent[i]
    # calculate percentage of what all categories have spent in total
    for p in range(0, len(catSpent)):
        percentage = 100*catSpent[p]/totalSpent
        percentage -= percentage%10
        percentages.append(percentage)

    # print everything
    outStr = ""
    # print diagram title
    outStr += "Percentage spent by category\n"

    # print diagram
    for x in range(100, -10, -10):
        outStr += "%3i| " % x
        for i in range(0, len(categories)):
            if percentages[i] >= x:
                outStr += "o  "
            else:
                outStr += "   "
        outStr += "\n"

    # print seperator line
    outStr += "    -"
    for i in range(0, len(categories)):
        outStr += "---"

    # print labels
    # get longest string of category.name
    nameLength = 0
    for category in categories:
        if nameLength < len(category.name):
            nameLength = len(category.name)
    # print each line of labels
    for i in range(0, nameLength):
        outStr += "\n"
        outStr += "     "
        for category in categories:
            if i < len(category.name):
                outStr += category.name[i] + "  "
            else:
                outStr += "   "

    return outStr
