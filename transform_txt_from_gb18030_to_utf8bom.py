# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-01 21:14
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
from os import system
from os.path import isfile
from chardet import detect
from sys import argv
from codecs import open

"""
自动检测 txt 文件的字符编码，如果不是 utf-8，则转换为 utf-8
"""

if len(argv) == 1:
    print("need more argv")
    exit(-1)

for argv in argv[1:]:
    if isfile(argv):
        with open(argv, "rb") as f:
            encoding_type = detect(f.read())["encoding"]
            print("{} - {}".format(encoding_type, argv.split(sep="\\")[-1]))
            if encoding_type is None or (encoding_type.lower() != "utf-8-sig" and encoding_type.lower() != "utf-8"):
                try:
                    content = open(argv, 'r', "GB18030", "ignore").read()
                    open(argv, 'w', "utf-8-sig").write(content)
                except IOError as e:
                    print("I/O error: {}".format(e))
            else:
                print("encoding_type = {}".format(encoding_type))

system("echo 按任意键退出... && pause > nul")
