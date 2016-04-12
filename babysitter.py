MIDNIGHT = 12

AFTER_MIDNIGHT_RATE = 16
BEFORE_BEDTIME_RATE = 12

def calculate(start_time, bed_time, end_time):
    if start_time < 5:
        start_time += MIDNIGHT
    if end_time <= 4:
        end_time += MIDNIGHT
    if bed_time < 5:
        bed_time += MIDNIGHT
    work_after_midnight = end_time - max(MIDNIGHT, start_time) if end_time > MIDNIGHT else 0
    work_before_bedtime = min(bed_time, MIDNIGHT) - min(start_time, MIDNIGHT)
    return work_after_midnight * AFTER_MIDNIGHT_RATE + work_before_bedtime * BEFORE_BEDTIME_RATE
