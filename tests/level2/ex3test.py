__author__ = 'anamaria.sipos'

from exercises.level2.ex3 import time_slow
import time


@time_slow
def test1(name):
    return 'test hello there ' + name


@time_slow(2)
def test2(a, b):
    time.sleep(1)
    return a + b


@time_slow(1)
def test3(list):
    for item in list:
        print item


test1('ana')
test2(1, 2)
test3([1, 2, 3])