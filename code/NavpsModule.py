#here lies the blue print for the class description
from datetime import datetime as dt

class Navps:
    """
    Navps object with date and prices of the different unit trust funds for that date
    """

    def __init__(self):
        self.date = 0
        self.bond = 0
        self.balanced = 0
        self.equity = 0
        self.market = 0
        self.gs = 0
        self.dynamic = 0
        self.index = 0
        self.advantage = 0
        self.abundance = 0
        self.wellspring = 0
        self.voyager = 0
        self.starter = 0
        self.a28 = 0
        self.a38 = 0
        self.a48 = 0

    def updateItem(self, attr, val):
        return setattr(self, attr, val)

    def getItem(self, attr):
        return getattr(self, attr)

    def printAttr(self):
        print(f"Date: {self.date}")
        print(f"Bond Fund: {self.bond}")
        print(f"Balanced Fund: {self.balanced}")
        print(f"Philippine Equity Fund: {self.equity}")
        print(f"Money Market Fund: {self.market}")
        print(f"GS Fund: {self.gs}")
        print(f"Dynamic Fund: {self.dynamic}")
        print(f"Index Fund: {self.index}")
        print(f"Dollar Advantage Fund: {self.advantage}")
        print(f"Dollar Abundance Fund: {self.abundance}")
        print(f"Dollar Wellspring Fund: {self.wellspring}")
        print(f"World Voyager Fund: {self.voyager}")
        print(f"Dollar Starter Fund: {self.starter}")
        print(f"* Achiever 2028 Fund: {self.a28}")
        print(f"* Achiever 2038 Fund: {self.a38}")
        print(f"* Achiever 2048 Fund: {self.a48}")

    def add(self, value, list):
        if isinstance(value, dt):
            self.date = value
        elif ":" in value:
            temp = value.split(":")
            if temp[0].casefold().find("bond"):
                self.updateItem("bond", temp[1])
            elif temp[0].casefold().find("balanced"):
                self.updateItem("balanced", temp[1])
            elif temp[0].casefold().find("equity"):
                self.updateItem("equity", temp[1])
            elif temp[0].casefold().find("market"):
                self.updateItem("market", temp[1])
            elif temp[0].casefold().find("gs"):
                self.updateItem("gs", temp[1])
            elif temp[0].casefold().find("dynamic"):
                self.updateItem("dynamic", temp[1])
            elif temp[0].casefold().find("index"):
                self.updateItem("index", temp[1])
            elif temp[0].casefold().find("advantage"):
                self.updateItem("advantage", temp[1])
            elif temp[0].casefold().find("abundance"):
                self.updateItem("abundance", temp[1])
            elif temp[0].casefold().find("wellspring"):
                self.updateItem("wellspring", temp[1])
            elif temp[0].casefold().find("voyager"):
                self.updateItem("voyager", temp[1])
            elif temp[0].casefold().find("starter"):
                self.updateItem("starter", temp[1])
            elif temp[0].casefold().find("2028"):
                self.updateItem("a28", temp[1])
            elif temp[0].casefold().find("2038"):
                self.updateItem("a38", temp[1])
            elif temp[0].casefold().find("2048"):
                self.updateItem("a48", temp[1])
            else:
                pass
        else:
            pass

        list.append(self)