def GenerateTrend(previous, now, timeDiff):
    hours = timeDiff/3600
    change_per_hour = (now - previous)/hours
    if change_per_hour < -100:
        return "Gwałtowny spadek"
    elif change_per_hour < -20 and change_per_hour >= -100:
        return "Spadek"
    elif change_per_hour < 20 and change_per_hour >= -20:
        return "Stabilny"
    elif change_per_hour < 100 and change_per_hour >= 20:
        return "Wzrost"
    elif change_per_hour >= 100:
        return "Gwałtowny wzrost"


def GenerateWarning(sugarlevel, trend):
    low_sugar = 60
    high_sugar = 180
    warning = ""
    if sugarlevel > high_sugar:
        warning = warning + "Wysoki cukier! \n"
        if trend == "Wzrost" or trend == "Gwałtowny wzrost":
            warning = warning + "Ryzyko Hiperglikemi! \n"
    if sugarlevel < low_sugar:
        warning = warning + "Niski cukier! \n"
        if trend == "Spadek" or trend == "Gwałtowny spadek":
            warning = warning + "Ryzyko Hipoglikemi! \n"
    if sugarlevel > 90 and sugarlevel < 120:
        if trend == "Gwałtowny spadek":
            warning = warning + "Ryzyko Hipoglikemi! \n"
        if trend == "Gwałtowny wzrost":
            warning = warning + "Ryzyko Hiperglikemi! \n"
    if trend == "Stabilny":
        if sugarlevel > 200 or sugarlevel < low_sugar:
            warning = warning + "Ryzyko wystąpienia ciał ketonowych \n"
    return warning
