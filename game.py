import webbrowser

def find_game_link(ftext):
    games = {
        "chess": "https://poki.com/en/g/master-chess",
        "bubble": "https://poki.com/en/g/bubble-shooter-lak",
        "brain": "https://poki.com/en/g/brain-test-tricky-puzzles",
        "subway": "https://poki.com/en/g/subway-surfers",
        "sort": "https://poki.com/en/g/water-color-sort",
        "hangman": "https://poki.com/en/g/hangman",
        "tic": "https://poki.com/en/g/tictactoe",
        "row": "https://poki.com/en/g/four-in-a-row",
        "mine": "https://poki.com/en/g/mine-sweeper-3",
        "f1": "https://poki.com/en/g/super-star-car",
        "smash": "https://poki.com/en/g/smash-karts",
        "google": "https://poki.com/en/g/google-feud",
        "red": "https://poki.com/en/g/red-ball-4"
    }   
    ftext = ftext.lower()   
    for word in ftext.split():
        if word in games:
            sentence = "Playing " + word + " game."
            webbrowser.open(games[word])
            return sentence           
    
    sentence = "No such game found."
    return sentence