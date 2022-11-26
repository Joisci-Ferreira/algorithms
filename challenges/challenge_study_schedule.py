def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    users_online = 0

    try:
        for entry_time, exit_time in permanence_period:
            if (entry_time <= target_time <= exit_time):
                users_online += 1
    except TypeError:
        return None

    return users_online
