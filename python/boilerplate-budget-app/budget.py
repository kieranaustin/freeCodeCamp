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
    print("not yet implemented")
