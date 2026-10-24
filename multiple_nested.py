
# Ask the user where to look for the phone
location = input("Where should I look? ").lower().strip()

# Check if the phone is in the bedroom
if location == "in the bedroom":
    place = input("Where in the bedroom should I look? ").lower().strip()

    if place == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")

# Check if the phone is in the bathroom
elif location == "in the bathroom":
    place = input("Where in the bathroom should I look? ").lower().strip()

    if place == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")

# Check if the phone is in the living room
elif location == "in the living room":
    place = input("Where in the living room should I look? ").lower().strip()

    if place == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")

# Handle any other location
else:
    print("I do not know where that is but I will keep looking.")
