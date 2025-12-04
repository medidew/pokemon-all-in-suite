import csv

pinball_game_cost: int = 25
pinball_game_duration: float = 60

with open("pinball.csv", mode="a", encoding="utf-8", newline='\n') as pinball_csv:
    while True:
        winnings = int(input("Enter number of coins won:"))
        profit = winnings - pinball_game_cost
        earn_rate = profit / pinball_game_duration
        
        csv_writer = csv.writer(pinball_csv)
        csv_writer.writerow([str(winnings), f"{earn_rate:.3f}"])