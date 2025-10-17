COLOR_CODES = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUA": "#00ffff", "BEIGE": "#f5f5dc",
               "CORAL": "#ff7f50", "DARKGREEN": "#006400", "GOLD": "#ffd700", "HOTPINK": "#ff69b4", "INDIGO": "#4b0082",
               "LAVENDER": "#e6e6fa"}

color_name = input("Enter color name: ").strip().upper()
while color_name != "":
    try:
        print(color_name, "is", COLOR_CODES[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").strip().upper()

for name, code in COLOR_CODES.items():
    print(f"{name:<12} is {code}")
