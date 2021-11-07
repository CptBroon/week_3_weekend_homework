class Game():
    def __init__(self):
        self.win_rules = {
            "rock" : "scissors",
            "scissors" : "paper",
            "paper" : "rock"
            }
        
    def play(self, player1, player2):
        player_1_choice = player1.choice
        player_2_choice = player2.choice
        
        if player_2_choice == self.win_rules[player_1_choice]:
            winner = player1
        elif player_1_choice == self.win_rules[player_2_choice]:
            winner = player2
        else:
            return f'Nobody won the match, both players selected the same option, which was {player1.choice}!'
            
        return f'{winner.name} was the winner, by playing {winner.choice}!'