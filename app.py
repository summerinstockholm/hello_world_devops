#!/usr/bin/env python3

import datetime
import os

# Получаю в переменную значение времени на сейчас и вывожу его на экран с тексто Hello
def do_magic():
    now = datetime.datetime.now()
    return "Hello! {0}".format(now)
# Для uwsgi:
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [do_magic()]
# Если мой файл включили как модуль, то он ниче не будет делать.
if __name__ == "__main__":
    if 'REQUEST_URI' in os.environ:
        print("Content-type: text/html\n\n")
    print(do_magic())
