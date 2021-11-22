from data import piece_of_data
import art
import random
import os


def get_random_data():
    pick = random.choice(piece_of_data)
    return pick


def format_dict(data):
    name = data['name']
    follower_count = data['follower_count']
    description = data['description']
    country = data['country']
    return f"{name}, a {description} from {country}"


def game():
    print(art.logo)
    person_a = get_random_data()
    print(f"Compare A: {format_dict(person_a)}")
    print(art.vs)
    person_b = get_random_data()
    print(f"Against B: {format_dict(person_b)}")
    return person_a, person_b


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    score = 0
    game_keep_going = True
    person_a = get_random_data()
    person_b = get_random_data()
    print(art.logo)

    while game_keep_going:
        person_a = person_b
        person_b = get_random_data()

        while person_a == person_b:
            person_b = get_random_data()

        print(f"Compare A: {format_dict(person_a)}")
        print(art.vs)
        print(f"Against B: {format_dict(person_b)}")
        guess = input("Which has more followers? Press 'A' or 'B'").lower()
        a_followers_count = person_a['follower_count']
        b_followers_count = person_b['follower_count']
        is_correct = check_answer(guess, a_followers_count, b_followers_count)

        clean = lambda: os.system('cls')
        clean()

        print(art.logo)
        if is_correct:
            score += 1
            print(f"You are right! Your current score: {score}")
        else:
            game_keep_going = False
            print(f"Sorry, that's wrong.Final score: {score}")
            if input("Would you like to play again? Press 'y' or 'n': ").lower() == 'y':
                game()

game()




