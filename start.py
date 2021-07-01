import json
import os


class VendingMachine:
    def __init__(self, filePath):
        self.config = json.load(open(filePath))
        self.data = self.config["machine"]["total_items_quantity"]  #Intialising input data
        
    def getDrinks(self):
        # This function will give drinks
        try:
            noofOutlet = self.config["machine"]["outlets"]["count_n"]

            beverageList = list(self.config["machine"]["beverages"].keys())
            beveragesData = self.config["machine"]["beverages"]

            for i in range(noofOutlet):
                bevName = beverageList[i % len(beverageList)]
                bevIngr = beveragesData[bevName]
                result, msg = self.checkIngrPresent(bevIngr)
                if result:
                    self.updateStock(bevIngr, "remove")
                    print(bevName + " is prepared.")
                else:
                    print(bevName + " cannot be prepared because " + msg)

            return
        except e:
            print(e)
            return


    def checkIngrPresent(self, bevIngr):
        # This function will give whethere ingredients for beverage are present in vending machine.

        for key, value in bevIngr.items():
            if key in self.data:
                if  self.data[key] < value:
                    return False, key + " is not sufficient"
            else:
                return False, key + " is not available"

        return True, ""


    def updateStock(self, updateData, operation):
        # This function will update stock as per operation. Add or remove

        if operation == "add":
            for key, value in (updateData.items()):
                    self.data[key] = value + self.data[key]

        elif operation == "remove":
            for key, value in (self.data.items()):
                self.data[key] = value - updateData[key]
        return

    def getStatus(self):
        # This function will give current status of ingredients in vending machine.
        print(self.data)


currPath = os.getcwd() + "/input.json"
machine = VendingMachine(currPath)


while True:
    print("\nPlease select one option:")
    print("1. Beverages   2. Refeil Machine   3. Status   4. Exit")
    num = input()
    if num == "1":
        machine.getDrinks()
    elif num == "2":
        bevList = ["hot_water", "hot_milk", "ginger_syrup", "sugar_syrup", "tea_leaves_syrup", 
         "green_mixture"]
        print("Select which you want to refeil :")
        print("1. Hot Water 2.Hot Milk 3.Ginger syrup 4.Sugar syrup 5.Tea leaaves syrup 6. Green mixture")
        selNo = input()
        print("Enter value for refeil :")
        quantity = input()
        key = bevList[int(selNo) - 1]
        value = int(quantity)

        machine.updateStock({key: value}, "add")
    elif num == "3":
        machine.getStatus()
    elif num == "4":
        break
        