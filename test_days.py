# -*- coding: utf-8 -*-

from io import StringIO as sio
import days


def test_day01():
    assert days.day01.solve(sio("1122"))[0] == 3
    assert days.day01.solve(sio("1111"))[0] == 4
    assert days.day01.solve(sio("1234"))[0] == 0
    assert days.day01.solve(sio("91212129"))[0] == 9
    assert days.day01.solve(sio("1212"))[1] == 6
    assert days.day01.solve(sio("1221"))[1] == 0
    assert days.day01.solve(sio("123425"))[1] == 4
    assert days.day01.solve(sio("123123"))[1] == 12
    assert days.day01.solve(sio("12131415"))[1] == 4
    assert days.day01.solve(open('input/day01')) == (1175, 1166)


def test_day02():
    assert days.day02.solve(open('input/day02.test1'))[0] == 18
    assert days.day02.solve(open('input/day02.test2'))[1] == 9
    assert days.day02.solve(open('input/day02')) == (45972, 326)


def test_day03():
    assert days.day03.solve(sio("1"))[0] == 0
    assert days.day03.solve(sio("12"))[0] == 3
    assert days.day03.solve(sio("23"))[0] == 2
    assert days.day03.solve(sio("1024"))[0] == 31
    assert days.day03.solve(open('input/day03')) == (326, 363010)


def test_day04():
    assert days.day04.solve(sio("aa bb cc dd ee"))[0] == 1
    assert days.day04.solve(sio("aa bb cc dd aa"))[0] == 0
    assert days.day04.solve(sio("aa bb cc dd aaa"))[0] == 1
    assert days.day04.solve(sio("abcde fghij"))[1] == 1
    assert days.day04.solve(sio("abcde xyz ecdab"))[1] == 0
    assert days.day04.solve(sio("a ab abc abd abf abj"))[1] == 1
    assert days.day04.solve(sio("iiii oiii ooii oooi oooo"))[1] == 1
    assert days.day04.solve(sio("oiii ioii iioi iiio"))[1] == 0
    assert days.day04.solve(open('input/day04')) == (386, 208)


def test_day05():
    assert days.day05.solve(open('input/day05.test')) == (5, 10)
    assert days.day05.solve(open('input/day05')) == (378980, 26889114)


def test_day06():
    assert days.day06.solve(sio("0\t2\t7\t0")) == (5, 4)
    assert days.day06.solve(open('input/day06')) == (7864, 1695)


def test_day07():
    assert days.day07.solve(open('input/day07.test')) == ('tknk', 60)
    assert days.day07.solve(open('input/day07')) == ('eqgvf', 757)


def test_day08():
    assert days.day08.solve(open('input/day08.test')) == (1, 10)
    assert days.day08.solve(open('input/day08')) == (4163, 5347)


def test_day09():
    assert days.day09.solve(sio("{}"))[0] == 1
    assert days.day09.solve(sio("{{{}}}"))[0] == 6
    assert days.day09.solve(sio("{{},{}}"))[0] == 5
    assert days.day09.solve(sio("{{{},{},{{}}}}"))[0] == 16
    assert days.day09.solve(sio("{<a>,<a>,<a>,<a>}"))[0] == 1
    assert days.day09.solve(sio("{{<ab>},{<ab>},{<ab>},{<ab>}}"))[0] == 9
    assert days.day09.solve(sio("{{<!!>},{<!!>},{<!!>},{<!!>}}"))[0] == 9
    assert days.day09.solve(sio("{{<a!>},{<a!>},{<a!>},{<ab>}}"))[0] == 3
    assert days.day09.solve(sio("<>"))[1] == 0
    assert days.day09.solve(sio("<random characters>"))[1] == 17
    assert days.day09.solve(sio("<<<<>"))[1] == 3
    assert days.day09.solve(sio("<{!>}>"))[1] == 2
    assert days.day09.solve(sio("<!!>"))[1] == 0
    assert days.day09.solve(sio("<!!!>>"))[1] == 0
    assert days.day09.solve(sio('<{o"i!a,<{i<a>'))[1] == 10
    assert days.day09.solve(open('input/day09')) == (11846, 6285)
