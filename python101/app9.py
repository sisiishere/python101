weight = int(input("Weight: "))
unit = input("kgs or lbs: ")
if unit == "kgs":
    converted = weight / 0.45
    print("weight in lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("weight in kgs: " + str(converted))
