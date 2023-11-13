# Yuqi Cheng
# Nov 2
# Homework 2

# The heart beat per year for human, blue whale and rabbit
Human_beat = 80*60*24*365
Bluewhale_beat = 33*60*24*365
Rabbit_beat = 160*60*24*365

# Which year a new president came to office (1980 onward)
Presidents = ["JIMMY CARTER", "RONALD REAGAN", "GEORGE BUSH", "WILLIAM J. CLINTON", "GEORGE W. BUSH", "BARACK OBAMA", "DONALD J. TRUMP", "JOSEPH R. BIDEN"]
Time = [1977, 1981, 1989, 1993, 2001, 2009, 2017, 2021]
# 1: Democrat; 0: Republican
Democrat = [1, 0, 0, 1, 0, 1, 0 ,1]

My_age = 22

print("How old are you?")
User_age = int(input())
Born_year = 2023 - User_age
if User_age < 0:
    print("I know you are not comming from the future. How old are you?")
    User_age = int(input())

# A simple way to do print. Multiple commas.
print("You are", User_age, "years old.")
# A similar way, but remember to change the number into string.
print("In that time, your heart has beaten "+str(User_age * Human_beat)+" times.")
# f-string with {}. It's straight forward to put the variable into {}.
print(f"In that time, a blue whale's heart has beaten {User_age * Bluewhale_beat} times.")
if User_age * Rabbit_beat < 1000000000 :
    # not f-string, but .format
    print("In that time, a rabbit's heart has beaten {} times.".format(User_age * Rabbit_beat))
else:
    print(f"In that time, a rabbit's heart has beaten {round(User_age * Rabbit_beat / 1000000000, 2)} billion times.")

Age_diff = User_age - My_age
if Age_diff > 0:
    print(f"You are {Age_diff} years older than me.")
elif Age_diff < 0:
    print(f"You are {-Age_diff} years younger than me.")
else:
    print("Your age is the same with me.")

if Born_year % 2 == 0:
    print(f"You were born in {Born_year}, which is an even year.")
else:
    print(f"You were born in {Born_year}, which is an odd year.")

n = 0
for year in Time:
    n += 1
    if n == len(Time):
        print(f"After 1980, there were {sum(Democrat[:n])} Democratic presidents since you were born.")
        print(f"President {Presidents[n-1]} was in office when you were born.")
    # find the president, which means Born_year < the year of next president came into office
    elif Born_year >= 1980 and Born_year < Time[n]:
        print(f"After 1980, there were {sum(Democrat[:n])} Democratic presidents since you were born.")
        print(f"President {Presidents[n-1]} was in office when you were born.")
        break


