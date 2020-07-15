# coding=utf-8
# 生成指定长度和个数的字符串名称，输出到excel，并用这些名称批量修改images目录下的文件
import os

from util import yfile, yrandom


def clean():
    os.rmdir('out')


STR_LENGTH = 5  # 字符串长度
STR_SIZE = 200  # 字符串个数

# 1.根据传入参数，生成需要的字符串列表
_name_list = yrandom.create_random_letter_list(STR_LENGTH, STR_SIZE)
# 2.保存列表到excel
yfile.save_str_to_file('\n'.join(_name_list), 'out\\names.csv')
# 3.根据字符串列表重命名images目录下的文件
yfile.rename_images_in_dir(_name_list, 'images')
