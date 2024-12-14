from datetime import datetime

# Display advice options
def display_advice():
    print("\n--- Advice Categories ---")
    print("1. Crop Rotation")
    print("2. Pest Control")
    print("3. Soil Health")
    print("4. Irrigation Management")
    print("5. Fertilizer Use")

# Provide advice based on choice
def provide_advice(choice):
    if choice == 1:
        return "Rotate crops annually to maintain soil nutrients."
    elif choice == 2:
        return "Use organic pest control to protect crops naturally."
    elif choice == 3:
        return "Test soil regularly and add compost for fertility."
    elif choice == 4:
        return "Use drip irrigation to conserve water."
    elif choice == 5:
        return "Apply balanced fertilizers based on soil test results."
    else:
        return "Invalid choice."

# Schedule a consultation
def request_consultation():
    print("\n--- Schedule Consultation ---")
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    address = input("Enter your address: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM AM/PM): ")

    display_advice()
    try:
        choice = int(input("Choose an advice number (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    advice = provide_advice(choice)
    if "Invalid" in advice:
        print(advice)
        return

    print("\n--- Consultation Summary ---")
    print(f"Name: {name}")
    print(f"Contact: {contact}")
    print(f"Address: {address}")
    print(f"Date: {date}")
    print(f"Time: {time}")
    print(f"Advice: {advice}")

    save_request(name, contact, address, date, time, advice)

# Save consultation request to a file
def save_request(name, contact, address, date, time, advice):
    with open("requests.txt", "a") as file:
        file.write(f"{name},{contact},{address},{date},{time},{advice}\n")
    print("Consultation request saved.")

# View saved requests
def view_requests():
    print("\n--- Consultation Requests ---")
    try:
        with open("requests.txt", "r") as file:
            requests = file.readlines()
            if not requests:
                print("No requests found.")
                return
            for request in requests:
                details = request.strip().split(",")
                print(f"Name: {details[0]}, Contact: {details[1]}, Address: {details[2]}, "
                      f"Date: {details[3]}, Time: {details[4]}, Advice: {details[5]}")
    except FileNotFoundError:
        print("No requests file found.")

# Main menu
def main():
    while True:
        print("\n--- AgriAssist:Municipal Appointment Advice System Menu ---")
        print("1. View Advice")
        print("2. Schedule Consultation")
        print("3. View Requests")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_advice()
        elif choice == "2":
            request_consultation()
        elif choice == "3":
            view_requests()
        elif choice == "4":
            print("Thank you for trusting us :) !")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
