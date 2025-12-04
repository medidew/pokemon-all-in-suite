import keyboard
import csv
import time

onix_game_cost: int = 25
start_button: str = "l"
end_button: str = "space"
start_time = time.time()

def startGame(event):
    keyboard.unhook_all()
    global start_time
    start_time = time.time()
    keyboard.on_press_key(key=end_button, callback=endGame)

def endGame(event):
    keyboard.unhook_all()
    game_duration = time.time() - start_time
    winnings = int(input("Enter number of coins won:"))
    profit = winnings - onix_game_cost
    earn_rate = profit / game_duration
    
    with open("onix.csv", mode="a", encoding="utf-8", newline='\n') as onix_csv:
        csv_writer = csv.writer(onix_csv)
        csv_writer.writerow([f"{game_duration:.3f}", str(winnings), f"{earn_rate:.3f}"])
    
    keyboard.on_press_key(key=start_button, callback=startGame)

keyboard.on_press_key(key=start_button, callback=startGame)
keyboard.wait()