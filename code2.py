try:
    weight =float(input("Enter your weight\t"))
    unit =input("kilograms or pounds? (K/L)\t")
    if unit =="K" or unit =="k":
        weight =weight  *2.205
        unit ="lbs."
        print(f"Your weight is: {round(weight, 1)} {unit}")
    elif unit =="L" or unit =="l":
        weight =weight/2.205
        unit ="kgs."
        print(f"Your weight is: {round(weight, 1)} {unit}")    
    else:
        print(f"{unit} is not valid")
    

except Exception:
    print("Invalid Entry")
