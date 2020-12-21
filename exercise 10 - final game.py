__AUTHOR__ = 'Eylon Fayena'

HANGMAN_PHOTOS = {0: """ 
    Let's play Hangman !
      x-------x
    """,
                  1: """      x-------x  
      |
      |
      |
      |
      | """,
                  2: """      x-------x 
      |       |
      |       0
      |
      |
      | """,
                  3: """      x-------x 
      |       |
      |       0
      |       |
      |
      | """,
                  4: """      x-------x 
      |       |
      |       0
      |      /|\\
      |
      | """,
                  5: """      x-------x  
      |       |
      |       0
      |      /|\\
      |      / 
      | """,
                  6: """      x-------x 
      |       |
      |       0
      |      /|\\
      |      / \\
      | """}


def home_screen(MAX_TRIES):
    """
    the start of the game. prints out the headline, and
    the times of trying to guess
    :param: MAX_TRIES: the chosen word from the text file
    :type: MAX_TRIES: str
    :return: print the headline and the ma tries a player has
    :rtype: str
    """
    print("""  
        _    _
       | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
       |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
       | |  | | (_| | | | | (_| | | | | | | (_| | | | |
       |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |
                           |___/

           """, 'the times to make a mistake is', MAX_TRIES, 'times' '\n'
                                                             '            ')


def print_hangman(num_of_tries):
    """this func presents to the player every time, his status
    in the hangman draw, depends on the times he have mistake.
    :param: num_of_tries: goes from 0 to 6. each times the player makes mistake
    num_of_tries +=1
    :param: HANGMAN_PHOTOS: a dictionary of key: nums of tries, val: the stage draw
    :type: num_of_tries: str
    :type: HANGMAN_PHOTOS: dict
    :return: v: returns the value ( stage draw ) of the k - the number of mistakes
    :rtype: v: str
    """
    for k, v in HANGMAN_PHOTOS.items():
        if num_of_tries == k:
            print(v)


def choose_word(file_path, index):
    """
    this func decides what's the guessed word will be
    :param file_path: text file path - from user input
    :param index: int - a random number from player input
    to choose a index word in the text file, that word will
    be the guessed word
    :return: index: the word that the player will be guessing in the following index
    :rtype: index: str
    """
    with open(file_path, 'r') as file_path:
        file = file_path.read().split(' ')
        words = []
        for word in file:
            if word not in words:
                words.append(word)
        if int(index) > len(file):  # an index loop - if a player input index that not exist
            index_i = int(index) - len(file)
            while index_i > len(file):
                index_i -= (int(index) - len(file))
                if index_i < len(file):
                    break
            word_i = file[index_i - 1]
        else:
            word_i = file[int(index) - 1]

        secret_word = word_i
    return secret_word


def show_hidden_word(secret_word, old_letters_guessed):
    """this func presents to the player the chosen word
    that the player will need to guess, but instead of
    letters it presents '_'
    if the player guessed a letter right, it will present the guessed letter.
    :param: secret_word: the chosen word from the text file
            old_letters_guessed: list of all the input letters that have been guessed
    :type: secret_word: str
            old_letters_guessed: list
    :return: res: returns '_' instead of the secret word letters
            old_letters_guessed: no return
    :rtype: secret_word: str
    """
    res = ''
    for letter in secret_word:
        if letter not in old_letters_guessed:
            res += ' _'
        else:
            res += ' ' + letter
    return res


def check_valid_input(letter_guessed, old_letters_guessed):
    """this func decides is the letter that the player input
    is valid. which means is it only 1 letter and isalpha and if the player have not
    guessed the letter in the pass.
    :param: letter_guessed: the input of the player,
            old_letters_guessed: list of all the input letters that have been guessed
    :type: letter_guessed: str
            old_letters_guessed: list
    :return:letter_guessed: if the letter valid or not
            old_letters_guessed: no return
    :rtype:letter_guessed: bool
    """
    return len(letter_guessed.lower()) == 1 and letter_guessed.isalpha() \
        and (letter_guessed.lower()) not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """this func decides is the letter that the player input
    is valid. which means is it only 1 letter and isalpha and if the player have not
    guessed the letter in the pass.
    if the letter is not valid prints X - and the letters that have been guessed already
    :param: letter_guessed: the input of the player,
            old_letters_guessed: list of all the input letters that have been guessed
    :type:letter_guessed: str
            old_letters_guessed: list
    :return: letter_guessed: if the letter valid or not
            old_letters_guessed: no return
    :rtype:letter_guessed: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed) and letter_guessed.lower() not in old_letters_guessed:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    elif not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        if letter_guessed in old_letters_guessed:
            sorted_input = sorted(old_letters_guessed)
            print('-> ', ' -> '.join(sorted_input))
        return False


def while_game_run(num_of_tries, MAX_TRIES, secret_word, old_letters_guessed):
    """this func make a loop so the game can keep running after
    every try. the loop starts at asking a letter from the player and
    check if valid. if the letter gussed was a part of the secret word
    it checks if the player has won or lost and return.
    else the game keep's runing and the number of tries + 1.
    :param: num_of_tries: the number of the mistakes the player has done
            MAX_TRIES: the maximum mistakes a player can make: 6.
            secret_word: the chosen word from the text file
            old_letters_guessed: list of all the input letters that have been guessed
    :type: secret_word: str
            old_letters_guessed: list
            num_of_tries: int
            MAX_TRIES: int
    :return: if the player have won or lost the game prints the secret word with the status.
             if the player keeps playing the func returns the num_of_tries += 1 and print the
             hangman draw according to the num_of_tries.
    :rtype: str
            int + str
    """
    is_won = False
    while num_of_tries < MAX_TRIES and not is_won:
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter_guessed = input('Guess a letter: ').lower()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed in secret_word:
                is_won = check_win(secret_word, old_letters_guessed)
            else:
                print(":(")
                num_of_tries += 1
                print_hangman(num_of_tries)
    if is_won:
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("W I N")
    else:
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("L O S E")


def check_win(secret_word, old_letters_guessed):
    """this func checks if the player has gussed the word
    by checking if the letters are in the letters that have been
    guessed list (-old_letters_guessed)
    :param: secret_word: the chosen word from the text file
            old_letters_guessed: list of all the input letters that have been guessed
    :type: secret_word: str
            old_letters_guessed: list
    :return: bool: if the letters of the secret word are in
            old_letters_guessed. if so, returns True - player wins.
            else: returns False - player lose.
    :rtype: bool
    """
    after_check = ''
    for i in secret_word:
        if i in old_letters_guessed:
            after_check += i
    return secret_word == after_check


def main():
    MAX_TRIES = 6
    num_of_tries = 0
    home_screen(MAX_TRIES)
    file_path = input('Please input a text file path here: ')
    index = input('Please input a random number: ')
    print_hangman(num_of_tries)
    secret_word = choose_word(file_path, index)
    old_letters_guessed = []
    while_game_run(num_of_tries, MAX_TRIES, secret_word, old_letters_guessed)


if __name__ == '__main__':
    main()
