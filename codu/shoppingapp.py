# store managers (SM) and Shoppers (S)
# SHIRT and SHOE with modifiable prices


# syntaxes
# CMD - for any command
# SM/S - for user selection



# ADD:
#   [ITEM NAME] [ITEM QTY] > 0 (whole numbers)
#   returns the quantity added
#   prints -1 on error
class ShoppingApp():
    
    def __init__(self):
        self.inputin()
        self.func = {
                'ADD':self.add,
                'REMOVE':self.remove,
                'GET_QTY':self.get_qty,
                'INCR':self.incr_dcr,
                'DCR':self.incr_dcr,
                'SET_COST':self.set_cost,
                'GET_ORDER_AMOUNT':self.get_order_amount
                }
        self.inventory = {}
        self.cart = {}
        self.opts = {"SM": self.inventory, "S": self.cart}
        self.prices = {'SHOE': 10 , "SHIRT": 10}
        self.process()

    def inputin(self): # to take lines of input
        self.inputs = []
        while True:
            std = input('>')
            if std == 'END':
                break
            self.inputs.append(std) 

    def valid(self): # checks the validity of the item params
            if self.cmd[0] != "CMD":
                return -1 
            if self.cmd[1] != "SM" and self.cmd[1] != "S":
                return -2
            if self.cmd[2] not in self.func:
                return -3
            if self.cmd[2] != "GET_ORDER_AMOUNT":
                if self.cmd[3] != "SHIRT" and self.cmd[3] != "SHOE":
                    return -4
                if self.cmd[2] != "GET_QTY" and self.cmd[2] != "REMOVE":
                    self.cmd[4] = eval(self.cmd[4])
                    if self.cmd[2] == "SET_PRICE":
                        if type(self.cmd) != int or type(self.cmd) != float:
                            return -6
                    else:
                        if type(self.cmd[4])!= int:
                            return -5
            return True

    def add(self,mode):
            item = self.cmd[3]
            val = self.cmd[4]
            if item not in self.opts[mode]:
               self.opts[mode][item] = val
               return val
            else:
                return -1

    def remove(self,mode):
        item = self.cmd[3]
        if item in self.opts[mode]:
            del self.opts[mode][item]
            return 1
        else:
            return -1

    def incr_dcr(self,mode):
        item = self.cmd[3]
        t = {'INCR':+1,"DCR": -1}
        val = self.cmd[4]
        if item in self.opts[mode]:
            self.opts[mode][item] += val * t[self.cmd[2]]
            if self.opts[mode][item] <= 0:
                del self.opts[mode][item]
                return -1
        
            return val
        else:
            return -1

    def get_qty(self,mode):
        item = self.cmd[3]
        if item in self.inventory:
            return self.inventory[item]
        else:
            return 0 

    def set_cost(self,mode):
        val = float(self.cmd[4])
        item = self.cmd[3]
        if mode == 'SM':
             self.prices[self.cmd[3]] = val # item price =new item value
             return '%.1f'%val 
        else:
            return -1

    def get_order_amount(self,mode):
            if mode == 'S':
                SUM = 0.0
                for a,b in self.cart.items():
                    SUM += self.prices[a] * b        
                return '%.2f'%SUM
            else:
                return -1

    def process(self):
        for _input in self.inputs:
            self.cmd = _input.split()
            if self.valid() == True:
                print(self.func[self.cmd[2]](self.cmd[1]))
            else:
                print(self.valid()) 
a = ShoppingApp()

