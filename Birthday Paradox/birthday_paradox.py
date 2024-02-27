"""
Birthday Paradox Simulation
Explore the surprising probabilities of the "Birthday Paradox"
Tags: Short, math, simulation
"""

import datetime
import random

def get_birthdays(num_bday):
    start = datetime.date(2001,1,1)
    birthdays = []
    for i in range(num_bday):
        birthday = start + datetime.timedelta(days=random.randint(0,364))
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    
    # If all the birthdays are unique 
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for i in range(len(birthdays)):
        # print(f"i is {i}")
        for j in range(i+1,len(birthdays)):
            # print(f"j is {j}")
            if birthdays[i] == birthdays[j]:
                # print(i,j)
                return birthdays[i]



def main():
    print("""Birthday Paradox Problem Simulation
The birthday paradox problem is about finding the probability
of two people having the same birthday in a group of N people.
This simulation is a Monte Carlo simulation to test the same 
with repeated random trials.
          
One would believe that we need many people in the group like half 
of 365 to be certain if group will have 2 common birthdays and here
lies the paradox as we only need a group of 23 people to have 50% 
probablity that in the group there will be a common birthday.

Here lies the paradox and the power of combinations.
""")

    MONTH_NAME = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec')

    while True:
        number_of_birthdays = input('How many birthdays shall I generate? (Max 100): ')
        if ( (number_of_birthdays.isdecimal()) and (0 < int(number_of_birthdays) <= 100)):
            number_of_birthdays = int(number_of_birthdays)
            break
        print('Invalid input.')
    
    print()

    print(f"Here are the {number_of_birthdays} birthdays: ")
    birthdays = get_birthdays(number_of_birthdays)

    for i in range(number_of_birthdays):
        if i != 0:
            print(', ',end='')
        print(f"{MONTH_NAME[birthdays[i].month-1]} {birthdays[i].day}",end="")
    print()
    print()

    if f_match := get_match(birthdays):
        print(f"In this simulation, multiple people have a birthday on {MONTH_NAME[f_match.month - 1]} {f_match.day}")
    else:
        print("In this simulation, there are no matching bithdays")
    

    print(f"Generating {number_of_birthdays} random birthday simulations 100,000 times")
    
    sim_match_count = 0
    for i in range(100000):
        if i % 10000 == 0:
            print(f"{i} simulation runs executed...")
        birthdays = get_birthdays(number_of_birthdays)
        if get_match(birthdays):
            sim_match_count += 1
    print("Executed 100000 simulation runs")

    prob = round(sim_match_count * 100/100000,2)
    print(f"""Out of the 100,000 simulation of {number_of_birthdays} people, there was a
matching birthdays in the group {sim_match_count} times. This means that that {number_of_birthdays}
people have a {prob}% chance of having a matching birthday in their group.
""")



if __name__ == '__main__':
    main()