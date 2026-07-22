import random

best_score = None

while True:

    print("\n===== NUMBER GUESSING GAME =====")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    level = input("Choose difficulty: ")

    if level == "1":
        limit = 10
    elif level == "2":
        limit = 50
    else:
        limit = 100

    secret = random.randint(1, limit)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {limit}: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        attempts += 1

        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print("Correct!")
            print("Attempts:", attempts)

            if best_score is None or attempts < best_score:
                best_score = attempts

            print("Best Score:", best_score)
            break

    again = input("Play Again? (y/n): ")

    if again.lower() != "y":
        print("Goodbye!")
        break
