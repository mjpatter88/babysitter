AFTER_MIDNIGHT_RATE = 16

def calculate(start_time, end_time):
    if end_time <= 4:
        end_time += 12
    work_after_midnight = end_time - 12
    return work_after_midnight * AFTER_MIDNIGHT_RATE
