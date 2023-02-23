from random import choice
from rich.console import Console

console = Console()

answers = ['Безперечно', 'Вирішено', 'Жодних сумнівів', 'Хороші перспективи', 'Краще не розповідати',
           'За моїми даними - ні', 'Мені здається - так', 'Поки неясно, спробуй знову', 'Навіть не думай',
           'Найімовірніше', 'Запитай пізніше', 'Моя відповідь - ні', 'Безперечно так', 'Знаки кажуть - так',
           'Зараз не можна передбачити', 'Перспективи не дуже хороші',
           'Можеш бути впевнений у цьому', 'Так', 'Сконцентруйся і запитай знову', 'Дуже сумнівно']


def magic_layer():
    while True:
        input(f"\nЯ уважно слухаю {chr(10151) * 3} ")
        console.print(f"{chr(127744)} [green]{choice(answers)}[/green] {chr(127744)}")

        while True:
            print(f'\nу тебе є ще питання? (так/ні, yes/no)')
            user_input = input(f"{chr(10151) * 3} ")
            if user_input in ('ні', 'no'):
                print(f'Все буде Україна! {chr(9996)}\n')
                return False
            elif user_input in ('так', 'yes'):
                return magic_layer()
            else:
                continue


def main():
    console.print(f"\n{chr(129535)} [yellow]M A G I C   L A Y E R[/yellow] {chr(129535)}")
    print(f'\nЯк до тебе звертатися?')
    name = input(f"{chr(10151) * 3} ")
    print(f'Привіт {name.title()}! Я магічна куля, яке у тебе питання?.')

    magic_layer()


if __name__ == '__main__':
    main()
