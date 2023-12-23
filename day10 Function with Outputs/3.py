year=int(input("year "))
month=int(input("month "))

def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def days_in_month(year, month):
    month_days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month==2:
        return 29
    else:
        return month_days[month-1] 
should_end = False
days=days_in_month(year,month)
print(days)
            
while not should_end:
    a=input("want to continue again?")
    if a=="no":
        should_end=True
        print("good bye") 
    else:
        year=int(input("year "))
        month=int(input("month "))

        def is_leap(year):
            if year%4==0:
                if year%100==0:
                    if year%400==0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        def days_in_month(year, month):
            month_days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if is_leap(year) and month==2:
                return 29
            else:
                return month_days[month-1] 
        should_end = False
        days=days_in_month(year,month)
        print(days)
            
            
       