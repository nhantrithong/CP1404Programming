COLOR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "faebd7", "antiquewhite 1": "ffefdb", "antiquewhite 2": "eedfcc", "antiquewhite 3": "cdc0b0",
               "antiquewhite4": "8b8378", "aquamarine1": "7fffd4", "aquamarine2": "76eec6", "aquamarine4": "458b74", "azure1": "#f0ffff"}

color = input("Enter the color you want the code for:").lower()
while color != "":
    if color in COLOR_CODES:
        print(color,"is",COLOR_CODES[color])
    else:
        print("Invalid!, please re-input appropriate color")
    color = input("Enter the color you want the code for:").lower()