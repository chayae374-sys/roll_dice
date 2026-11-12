def get_menu():
    print("""
        ================================
                    ROLL DICE
        ================================

            1. Start New Game
            2. View Game History
            3. View Statistics
            4. Exit

            Choose an option:

          """)
    
def get_number():
    found =  False
    while not found:
        try:
            get_menu()
            user_choise = int(input("please enter your choise: "))
            if 1 < user_choise > 4:
                print("just between 1-4")
            else:
                found =True
        except ValueError:
            print("just a number")
    return user_choise

            