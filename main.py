import time

print("Welcome to the Stretching Timer! Choose how long you want to stretch in each position, and how much time you "
      "need to switch between positions. Lastly, choose how many total stretching positions that you will complete. \n")

i_one = int(input("How many seconds do you want each stretch to be? "))
i_two = int(input("How many seconds do you need to switch positions? "))
positions = int(input("How many total stretching positions will you be doing today? "))
reps = positions * 2

while reps > 0:
    print("\nStart stretching!")
    time.sleep(i_one)
    print("Time to switch!")
    time.sleep(i_two)
    reps = reps - 1

print("\nYou're done!")
