# coding: utf-8

import help_text
import os


def check_cmd_para(cmd_para):
    if len(cmd_para) == 1 or len(cmd_para) != 2:
        return 0
    proteins = cmd_para[1]
    return 1 if check_dir(proteins) else 0


def check_dir(filename):
    """

    :param filename: 判断的名字
    :return: 如果是文件夹，如果存在返回1，不存在返回0。不是文件夹返回0。
    """
    if os.path.isdir(filename):
        return 1 if os.path.exists(filename) else 0
    else:
        return 0


def check_file(filename):
    """

    :param filename: 判断的名字
    :return: 是文件返回1，不是返回0。文件不存在返回0
    """
    if os.path.isfile(filename):
        return 1 if os.path.exists(filename) else 0
    else:
        return 0


def check_format(filename, target_format):
    """

    :param filename: 文件名，必须是文件
    :param target_format: 匹配的后缀
    :return: 是否是指定格式
    """
    file_format = os.path.splitext(filename)[-1]
    return 0 if file_format != f".{target_format}" else 1
