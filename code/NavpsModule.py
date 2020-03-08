#here lies the blue print for the class description
class Navps:
    """
    Navps object with date and prices of the different unit trust funds for that date
    """

    def __init__(self, date, bond, balanced, equity, market, gs, dynamic, index,
                 advantage, abundance, wellspring, voyager, starter,
                 a28=None, a38=None, a48=None):
        self.date = date
        self.bond = bond
        self.balanced = balanced
        self.equity = equity
        self.market = market
        self.gs = gs
        self.dynamic = dynamic
        self.index = index
        self.advantage = advantage
        self.abundance = abundance
        self.wellspring = wellspring
        self.voyager = voyager
        self.starter = starter
        self.a28 = a28 if a28 is not None else 0
        self.a38 = a38 if a38 is not None else 0
        self.a48 = a48 if a48 is not None else 0

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