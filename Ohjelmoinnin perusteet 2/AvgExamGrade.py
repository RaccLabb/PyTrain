sumOfGrades = 0
numOfExams = 0
while True:
    grade = int(input("Anna tentin arvosana 0-5 tai lopeta syöttämällä negatiivinen luku. "))
    if grade < 0:
        break
    sumOfGrades += grade
    numOfExams += 1
if numOfExams <= 0:
    print("Yhtään koetta ei syötetty.")
else:    
    AvgGrade = sumOfGrades/numOfExams
    print(AvgGrade)

#En tiedä miksi ohjelma näytti ensin virhettä rivillä 1 vaikka kaikki on kyllä oikein. Toimi kyllä kolmannella käynnistyksellä.