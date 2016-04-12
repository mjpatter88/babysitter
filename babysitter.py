AFTER_MIDNIGHT_RATE = 16

def calculate(start_time, end_time):
    if start_time < 5:
        start_time += 12
    if end_time <= 4:
        end_time += 12
    time_worked = end_time - start_time
    work_after_midnight = end_time - max(12, start_time)
    return work_after_midnight * AFTER_MIDNIGHT_RATE
