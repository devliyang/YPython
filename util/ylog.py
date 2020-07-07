# coding=utf-8
import sys


def print_in_line(text):
    sys.stdout.write('\r{}'.format(text))
    sys.stdout.flush()


def print_progress(index, total, hint):
    print_in_line('{}, total {}'.format(hint, index + 1))
    if index == total - 1:
        print ': Success!'
