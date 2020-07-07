# coding=utf-8
import os

import ylog


def save_str_to_file(text, path):
    make_dir_if_not_exist(path)
    _file = open(path, 'w+')
    _file.write(text)
    _file.close()
    print 'Save to "{}" success!'.format(path)


def make_dir_if_not_exist(path):
    __dirs = os.path.dirname(path)
    if os.path.exists(__dirs):
        return
    try:
        os.makedirs(__dirs)
    except OSError:
        print 'dir "{}" is exist'.format(__dirs)
    else:
        print 'create dir "{}"'.format(__dirs)


def rename_images_in_dir(name_list, dir_path):
    if os.path.exists(dir_path):
        _dirs = os.listdir(dir_path)

        _name_size = len(name_list)
        _file_size = len(_dirs)

        print 'Ready to rename. Name size: {}, file size: {}'.format(_name_size, _file_size)

        for i in range(_file_size):
            _old_file_or_dir_name = os.path.join(dir_path, _dirs[i])
            _new_file_name = os.path.join(dir_path, name_list[i] + '.jpg')
            os.rename(_old_file_or_dir_name, _new_file_name)

            ylog.print_progress(i, _file_size, 'Rename images')
    else:
        print 'Rename images error: path: "{}" does not exist!'.format(dir_path)
