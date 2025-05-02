def grade(score):
    if score>=90 and score<=100:
        return("A")
    elif score>=80 and score<=89:
        return("B")
    elif score>=70 and score<=79:
        return("C")
    elif score>=60 and score<=69:
        return("D")
    elif score>=0 and score<=59:
        return("F")
print(grade(92))
print(grade(58)) 