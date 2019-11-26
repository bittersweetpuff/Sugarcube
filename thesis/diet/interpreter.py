def DoasageParser(dose):
    if (dose*10)%1 < 0.3:
        dosage = ((dose*10)//1)/10
    elif (dose*10)%1 < 0.8 and (dose*10)%1 >= 0.3:
        dosage = ((dose*10)//1 + 0.5)/10
    elif (dose*10)%1 >= 0.8:
        dosage = ((dose*10)//1 + 1)/10
    return dosage


def CalculateInsulinDose(WW, T, B, Wraz, Przel, Sugar):
    kcal = WW + T + B
    result = dict()
    if Sugar >= 220:
        initial_dose = ((Sugar - 100)/100)*Wraz
        result["warning"] = f"Przed jedzeniem przyjmij {DoasageParser(initial_dose)} jednostek insuliny aby obniżyć poziom cukru"
    elif Sugar <= 60:
        result["warning"] = "Jedz odrazu po podaniu insuliny"
    else:
        result["warning"] = " "
    ratio = WW/kcal
    if Sugar < 220:
        control_dose = ((Sugar - 100)/100)*Wraz
    else:
        control_dose = 0
    meal_dose = ((kcal/100)*Przel)
    if ratio >= 0.8:
        result["insulin_dose"] = str(DoasageParser((meal_dose*1.3)+control_dose))
        result["bolus"] = "100:0"
    elif ratio < 0.8 and ratio > 0.5:
        result["insulin_dose"] = str(DoasageParser((meal_dose*1.2)+control_dose))
        result["bolus"] = "80:20"
    elif ratio == 0.5:
        result["insulin_dose"] = str(DoasageParser(meal_dose+control_dose))
        result["bolus"] = "70:30"
    elif ratio < 0.5 and ratio >= 0.15:
        result["insulin_dose"] = str(DoasageParser(meal_dose+control_dose))
        result["bolus"] = "50:50"
    elif ratio < 0.15:
        result["insulin_dose"] = str(DoasageParser(meal_dose+control_dose))
        result["bolus"] = "0:100"

    if ratio < 0.8:
        if kcal > 250 and kcal <= 350:
            result["bolus"] = result["bolus"] + " przedłużony na 2 h"
        elif kcal > 350 and kcal <= 450:
            result["bolus"] = result["bolus"] + " przedłużony na 3 h"
        elif kcal > 450:
            result["bolus"] = result["bolus"] + " przedłużony na 4 h"

    return result
