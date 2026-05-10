from core.logic_selector import RandomSelector

def main():
    print("🎯 Welcome to the RandomPick Console Tester")
    selector = RandomSelector()

    # Get User Input
    raw_input = input("Enter options separated by commas: ")
    selector.add_options(raw_input)

    try:
        num_to_pick = int(input("How many items should I pick? "))
        
        # Action
        results = selector.select_items(num_to_pick)

        # Output
        print("\n✨ Selection Results:")
        for i, item in enumerate(results, 1):
            print(f"{i}. {item}")

    except ValueError:
        print("❌ Error: Please enter a valid number for the selection count.")

if __name__ == "__main__":
    while True:
        main()