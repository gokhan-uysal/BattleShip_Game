import datetime as dt
def Greetings(name):
    if 00 <= int(dt.datetime.now().hour) < 10:
        print(f"Good morning {name.capitalize()} ")
    elif 10 <= int(dt.datetime.now().hour) <= 16:
        print(f"Good evening {name.capitalize()} ")
    elif 16 < int(dt.datetime.now().hour) < 24:
        print(f"Good night {name.capitalize()} ")
    pass

def CurrentFullDate():
    month, day, year = dt.datetime.now().month, dt.datetime.now().day, dt.datetime.now().year
    return f"{month}/{day}/{year}"
    pass