def time_of_year(a):
    if a <= 12 and a > 0:
        if a == 12 or a == 1 or a == 2:
            return 'Winter'
        elif a >= 3 and a <= 5:
            return 'Spring'
        elif a >= 6 and a <= 8:
            return 'Summer'
        else:
            return 'Autumn'
    else:
        return 'enter correct number: number of the month'
print(time_of_year(5))