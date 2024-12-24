import pyfiglet

def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

def main():
    while True:
        text = input("Enter the text you want to convert to ASCII art: ")
        ascii_art = generate_ascii_art(text)

        print("\nHere is your ASCII art:\n")
        print(ascii_art)

        continue_choice = input("Do you want to continue? (yes/no): ").lower()

        if continue_choice != "yes":
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()