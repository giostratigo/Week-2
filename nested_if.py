# Ask the user for the book cover type
cover = input("What type of cover does the book have? ").lower()

# Check if the cover is soft
if cover == "soft":
    # Ask if the book is perfect bound
    perfect_bound = input("Is the book perfect-bound? ").lower()

    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

# Check if the cover is hard
elif cover == "hard":
    print("Books with hard covers can be more expensive!")
