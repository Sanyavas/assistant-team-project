from information import start_info_games
from games.magic_layer import main as mg_main
from games.hangman import main as hm_main
from logger import get_logger


logger = get_logger(__name__)


def main():

    logger.info('Start Games')
    while True:
        print(start_info_games())
        user_input = input(f"\nEnter command {chr(10151) * 3} ")
        if user_input == "1":
            mg_main()
        elif user_input == "2":
            hm_main()
        elif user_input == "0":
            print(f"\n{chr(128075)} Good bay!")
            break
        else:
            print(f"\n{chr(129400)}I don't understand you!")


if __name__ == '__main__':
    main()
