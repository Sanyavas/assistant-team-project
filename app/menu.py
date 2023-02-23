"""C H A T B O T    M E N U"""

from .addressbook import main as ab_main
from .notes import main as nb_main
from .sort import main as sr_main
from .information import start_info_menu
from .games_menu import main as games_main
from .logger import get_logger


logger = get_logger(__name__)


def main():
    """Main function"""

    while True:
        print(start_info_menu())
        user_input = input(f"\nEnter command {chr(10151)*3} ")
        if user_input == "1":
            ab_main()
        elif user_input == "2":
            nb_main()
        elif user_input == "3":
            sr_main()
        elif user_input == "4":
            games_main()
        elif user_input == "0":
            print(f"\n{chr(128075)} Good bay!")
            break
        else:
            print(f"\n{chr(129400)}I don't understand you!")


if __name__ == "__main__":
    logger.info('Start program')
    main()
