import babysitter

start_time = input("Please input the start time: ")
bedtime = input("Please input the bed time: ")
end_time = input("Please input the end time: ")

wages = babysitter.calculate(int(start_time), int(bedtime), int(end_time))

print("You earned {} dollars!".format(wages))

