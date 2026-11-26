class student:
    def __init__(self, name, num):
        self.name = name
        self.studentNum = num
        self.__credits = 0

    @property
    def credits(self):
        return self.__credits
 
    @credits.setter
    def credits(self, amount):
        if amount > 0 and amount < 7:
            self.__credits += amount
        else:
            print("Virheellinen luku!")
        print(f"{self.name} opintopistemäärä on: {self.credits}")



def main():
    student1 = student("Petteri Rintamäki", "k2603034")
    student2 = student("Matti Meikäläinen", "k2089497")
    student1.credits = 5
    student2.credits = 6

if __name__=="__main__":
    main()