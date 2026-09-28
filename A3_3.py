gender = input("Please enter your gender: ")
hemoglobin = float(input("Please enter your hemoglobin: "))
if gender == "male":
    if(hemoglobin < 134):
        print("Your hemoglobin is low")
    elif (hemoglobin > 167):
        print("Your hemoglobin is high")
    else:
        print("Your hemoglobin is normal")
elif gender == "female":
    if(hemoglobin < 117):
        print("Your hemoglobin is low")
    elif (hemoglobin > 155):
        print("Your hemoglobin is high")
    else:
        print("Your hemoglobin is normal")