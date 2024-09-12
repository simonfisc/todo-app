date = input("Enter a date in YYYY-MM-DD format: ")
mood = input("Enter a mood of the day: ")
thoughts = input("Let your thought flow: ")
with open(f"../journal/{date}.txt", "w") as file:
    file.write(f"Mood: {mood}, journal: {thoughts}")


