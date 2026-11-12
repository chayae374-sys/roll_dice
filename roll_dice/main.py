from menu import get_number
import all_function as a
from fs import load_game_history,save_game

def main():
    player = None
    while player != 4:
        player = get_number()
        if player == 1:
            game = a.start_game()
        elif player == 2:
            history = load_game_history()
            a.display_game_history(history)
        elif player == 3:
            history = load_game_history()
            a.display_statistics(history)
        elif player == 4:
            print("goodbye")
    
    
            
if __name__ == "__main__":
    main()
    
    