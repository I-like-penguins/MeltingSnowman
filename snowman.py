import game_logic as gl

if __name__ == "__main__":
    is_playing = True
    while is_playing:
        gl.play_game()
        usr_input = input("Play again? (y/n): ").lower()
        if usr_input == "n":
            is_playing = False

    print("Game finished")