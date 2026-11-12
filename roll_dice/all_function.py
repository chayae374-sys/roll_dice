import random
from fs import *
from fs import load_game_history,save_game

def get_name_and_round():
    valid_input = False 
    while not valid_input:
        user = input("please enter your name: ")
        if not user:
            print("you must enter a name")
        else:
            valid_input = True
    input_round = False
    while not input_round:
        try:
            rounds = int(input("choose how many games do you want? "))
            if 1 < rounds > 10:
                print("just bwteen 1-10")
            else:
                input_round = True
        except ValueError:
            print("just a number")
    return user,rounds



def roll_dice():
    return random.randint(1, 6)
    


def play_round(round_count):
    player = roll_dice()
    computer = roll_dice()
    winner = None
    if player > computer:
        winner = "player"
    elif computer > player:
        winner = "computer"
    else:
        winner = "draw"
    result = {"round": round_count,
            "player_dice":player ,
            "computer_dice": computer,
            "winner": winner
            }
    return result
    
    
def start_game():
    final_result = []
    user_score = 0
    computer_score = 0
    user,rounds = get_name_and_round()
    Show_start_of_game(user,rounds)
    for i in range(rounds):
        result = play_round(i + 1)
        final_result.append(result)
        if result["winner"] == "player":
            result["winner"] = user
            user_score += 1
        elif result["winner"] == "computer":
            computer_score += 1
        Displaying_game_results(user,i+1,result)
    if computer_score > user_score:
        winner = "computer"   
    elif  user_score > computer_score:
        winner = user
    else:
        winner = "draw" 
    Displaying_final_result(user,user_score,computer_score,winner)
    game = {"player_name": user,
                        "rounds": rounds,
                        "player_score":user_score,
                        "computer_score": computer_score,
                        "winner": winner,
                        "results":final_result
                        }
    save_game(game)
    return game


def Show_start_of_game(user,rounds):
    print(f"""
            ================================
                    NEW GAME
            ================================

            Player name: {user}
            Number of rounds: {rounds}
        """)
              
              
def Displaying_game_results(user,rounds,result):
    print(f"""        

---------- ROUND {rounds} ----------

{user}:    🎲 {result["player_dice"]}
Computer: 🎲 {result["computer_dice"]}

{result["winner"]} wins this round!

""")

def Displaying_final_result(user,user_score,computer_score,winner):
    print(f"""
          ================================
                    GAME OVER
          ================================

            {user}:    {user_score} points
            Computer:  {computer_score} points

            WINNER: {winner}!

            Game saved successfully!

          """)



#quastion 2

def display_game_history(history):
    for i in history:
        print(f"""
        ================================
                    GAME
        ================================

        Result!
        Player name:{i["player_name"]}
        Number of rounds: {i["rounds"]}
        Player score: {i["player_score"]}
        Computer: {i["computer_score"]}
        Winner: {i["winner"]}
        """
        )
    
# quastion 3

def Total_number_of_games(history):
    len_history =  len(history)
    return f"the total games until now: {len_history}"
    
def Total_numbers_of_player_wins(history):
    count = 0
    for game in history:
        if not game["winner"] in ["computer","draw"]:
            count += 1
    return count

def Total_numbers_of_computer_wins(history):
    count = 0
    for game in history:
        if game["winner"] =="computer":
            count += 1
    return f"the total winner computer is: {count}" 

def Total_numbers_of_player_name_wins(history):
    names = {}
    for game in history:
        if not game["winner"] in ["computer","draw"]:
            if not game["player_name"] in names:
                names[game["player_name"]] = 0
            names[game["player_name"]] += 1
    return f"the nanes and their wins are : {names}"      

def calculate_avg(history,total_player_wins):
    if len(history) > 0:
        return f"this is the ratio of the % of player winning :{total_player_wins/len(history)*100}"
    else:
        print("there is no games")
    
    

    
def display_statistics(history):  
    total_games = Total_number_of_games(history)
    total_player_wins = Total_numbers_of_player_wins(history)
    total_computer_wins = Total_numbers_of_computer_wins(history)
    total_players_and_wins = Total_numbers_of_player_name_wins(history)
    avg_of_total_winning_player = calculate_avg(history,total_player_wins)
    print(total_games)
    print(f"the total winner player is: {total_player_wins}")
    print(total_computer_wins)
    print(total_players_and_wins)
    print(avg_of_total_winning_player)



    
    


        


    

