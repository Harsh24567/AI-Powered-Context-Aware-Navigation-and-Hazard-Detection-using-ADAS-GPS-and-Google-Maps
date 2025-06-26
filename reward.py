def calculate_reward(hazard_type: int, action: int) -> int:
    """
    Computes reward based on current hazard and agent action.

    :param hazard_type: 0 = clear, 1 = red light, 2 = roadblock, 3 = accident
    :param action: 0 = STOP, 1 = SLOW, 2 = GO, 3 = REROUTE
    :return: Reward (int)
    """
    if hazard_type == 0 and action == 2:  # GO on clear
        return 1
    elif hazard_type == 1 and action == 0:  # STOP at red light
        return 1
    elif hazard_type == 2 and action == 3:  # REROUTE at block
        return 1
    elif hazard_type == 3 and action in [0, 3]:  # STOP or REROUTE at accident
        return 1
    else:
        return -1          # Wrong action
