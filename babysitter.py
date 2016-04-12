MIDNIGHT = 12

EARLIEST_STARTING_TIME = 5
EARLIEST_BED_TIME = 5
LATEST_ENDING_TIME = 4

AFTER_MIDNIGHT_RATE = 16
BEFORE_BEDTIME_RATE = 12
BEDTIME_TO_MIDNIGHT_RATE = 8

def calculate(start_time, bed_time, end_time):
    start_time, bed_time, end_time = _make_times_absolute(start_time, bed_time, end_time)

    work_before_bedtime = min(bed_time, MIDNIGHT) - min(start_time, MIDNIGHT)
    work_after_bedtime_before_midnight = min(end_time, MIDNIGHT) - min(bed_time, MIDNIGHT)
    work_after_midnight = end_time - max(MIDNIGHT, start_time) if end_time > MIDNIGHT else 0

    return work_before_bedtime * BEFORE_BEDTIME_RATE + \
                work_after_midnight * AFTER_MIDNIGHT_RATE + \
                work_after_bedtime_before_midnight * BEDTIME_TO_MIDNIGHT_RATE

def _make_times_absolute(start_time, bed_time, end_time):
    if start_time < EARLIEST_STARTING_TIME:
        start_time += MIDNIGHT
    if bed_time < EARLIEST_BED_TIME:
        bed_time += MIDNIGHT
    if end_time <= LATEST_ENDING_TIME:
        end_time += MIDNIGHT
    return start_time, bed_time, end_time
