def setComparison(course1, course2):
    sameAttendants = course1.intersection(course2)
    return sameAttendants

if __name__=="__main__":
    kurssi_a = {"Jussi", "Marjo", "Timo", "Anna"}
    kurssi_b = {"Timo", "Anna", "Paavo", "Kati"}
    print(setComparison(kurssi_a, kurssi_b))