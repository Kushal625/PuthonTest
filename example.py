class Bonus:
    def __init__(self,name,base_salary, bonus_per):
        self.name = name
        self.base_salary = base_salary
        self.bonus_per = bonus_per

    def Annual(self):
        self.Annu = (self.base_salary *self.bonus_per )/ 100
        print(self.Annu)

new = Bonus('kuk',40000,10)
new.Annual()
'''name = input("Enter employee's name")
    base_salary = int(input("Enter base annual salary"))
    bonus_per = int(input("Enter bonus percentage"))'''


