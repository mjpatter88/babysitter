AFTER_MIDNIGHT_RATE = 16
BEFORE_BEDTIME_RATE = 12

def calculate(start_time, bed_time, end_time):
    if start_time < 5:
        start_time += 12
    if end_time <= 4:
        end_time += 12
    if bed_time < 5:
        bed_time += 12
    work_after_midnight = max(12, end_time) - max(12, start_time)
    work_before_bedtime = min(bed_time, 12) - min(start_time, 12)
    return work_after_midnight * AFTER_MIDNIGHT_RATE + work_before_bedtime * BEFORE_BEDTIME_RATE
