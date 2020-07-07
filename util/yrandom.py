# coding=utf-8
import random
import string

import ylog


def create_random_list(choice_list, str_length):
    return random.sample(choice_list, str_length)


def create_random_string(choice_list, str_length):
    return "".join(create_random_list(choice_list, str_length))


# create letters(with 'a-zA-Z'): count <str_size>, letter length <str_length>
def create_random_letter_list(str_length, str_size):
    _list = []
    for i in range(str_size):
        _text = create_random_string(string.letters, str_length)
        _list.append(_text)

        ylog.print_progress(i, str_size, "Create texts")
    return _list
