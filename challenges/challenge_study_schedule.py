def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count_online_period = 0

    for start, end in permanence_period:
        if (
            not isinstance(start, int)
            or not isinstance(end, int)
            or start > end
        ):
            return None

        if start <= target_time <= end:
            count_online_period += 1

    return count_online_period
