def points_per_90(points, minutes):

    if minutes == 0:
        return 0

    return points / minutes * 90

def goals_per_90(goals, minutes):

    if minutes == 0:
        return 0

    return goals / minutes * 90

def assists_per_90(assists, minutes):

    if minutes == 0:
        return 0

    return assists / minutes * 90