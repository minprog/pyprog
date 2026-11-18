# De originele versie van de bioscoop. PAS DIT BESTAND NIET AAN.
#
# De knop compare draait dit programma en jouw cinema.py met dezelfde
# antwoorden, en vergelijkt wat ze printen. Verander je dit bestand, dan
# valt er niets meer te vergelijken.

def cinema() -> None:
    print("WELCOME TO THE CINEMA")

    # Prompt and re-prompt for the day
    day = input("Which day? (monday-sunday)\n").lower()
    while day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
                      "sunday"):
        day = input("Invalid day! Please enter monday-sunday.\n").lower()

    # Prompt and re-prompt for the hour
    hour = int(input("At what hour does the movie start? (0-23)\n"))
    while hour < 0 or hour > 23:
        hour = int(input("Invalid hour! Please enter a number between 0 and 23.\n"))

    # Prompt for 3D
    is_3d = input("3D movie? (y/n)\n")
    while is_3d != "y" and is_3d != "n":
        is_3d = input("Please answer y or n.\n")

    # Prompt and re-prompt for number of tickets
    tickets = int(input("How many tickets?\n"))
    while tickets < 1 or tickets > 10:
        tickets = int(input("Invalid amount! Please enter a number between 1 and 10.\n"))

    total = 0
    for number in range(1, tickets + 1):
        # Prompt and re-prompt for age
        age = int(input(f"Age of visitor {number}?\n"))
        while age < 0 or age > 120:
            age = int(input("Invalid age! Please enter a number between 0 and 120.\n"))

        # Base price per age group
        if age < 3:
            price = 0
            group = "infant"
        elif age < 12:
            price = 600
            group = "child"
        elif age < 65:
            price = 1000
            group = "adult"
        else:
            price = 750
            group = "senior"

        # Adults can have a student discount
        if group == "adult":
            student = input("Student card? (y/n)\n")
            while student != "y" and student != "n":
                student = input("Please answer y or n.\n")
            if student == "y":
                price -= 150
                group = "student"

        # Infants always get in for free, others pay surcharges and discounts
        if price > 0:
            if day == "saturday" or day == "sunday":
                price += 100
            elif day == "tuesday":
                price -= 200

            if hour < 12:
                price -= 100
            elif hour >= 18:
                price += 150

            if is_3d == "y":
                price += 200

        print(f"Ticket {number}: {group} {price // 100}.{price % 100:02d}")
        total += price

    # Groups of 4 or more get 10% off
    if tickets >= 4:
        discount = total // 10
        total -= discount
        print(f"Group discount: -{discount // 100}.{discount % 100:02d}")

    if total == 0:
        print("Total: free")
    else:
        print(f"Total: {total // 100}.{total % 100:02d}")


if __name__ == '__main__':
    cinema()
