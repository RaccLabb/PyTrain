class student:
    def __init__(self, name, num):
        self.name = name
        self.studentNum = num
        self.credits = 0

    def addCredits(self, amount):
        self.credits += amount
        print(f"{self.name} opintopistemäärä on: {self.credits}")

def main():
    student1 = student("Petteri Rintamäki", "k2603034")
    student2 = student("Matti Meikäläinen", "k2089497")
    student1.addCredits(5)
    student2.addCredits(15)

if __name__=="__main__":
    main()