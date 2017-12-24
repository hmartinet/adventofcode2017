# -*- coding: utf-8 -*-

from io import StringIO as sio
import logging
import days

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('tests')


def test_day01():
    log.info("test_day01")
    d = days.day01
    assert d.solve(sio("1122"))[0] == 3
    assert d.solve(sio("1111"))[0] == 4
    assert d.solve(sio("1234"))[0] == 0
    assert d.solve(sio("91212129"))[0] == 9
    assert d.solve(sio("1212"))[1] == 6
    assert d.solve(sio("1221"))[1] == 0
    assert d.solve(sio("123425"))[1] == 4
    assert d.solve(sio("123123"))[1] == 12
    assert d.solve(sio("12131415"))[1] == 4
    with open('input/day01') as f:
        assert d.solve(f) == (1175, 1166)


def test_day02():
    log.info("test_day02")
    d = days.day02
    with open('input/day02.test1') as f:
        assert d.solve(f)[0] == 18
    with open('input/day02.test2') as f:
        assert d.solve(f)[1] == 9
    with open('input/day02') as f:
        assert d.solve(f) == (45972, 326)


def test_day03():
    log.info("test_day03")
    d = days.day03
    assert d.solve(sio("1"))[0] == 0
    assert d.solve(sio("12"))[0] == 3
    assert d.solve(sio("23"))[0] == 2
    assert d.solve(sio("1024"))[0] == 31
    with open('input/day03') as f:
        assert d.solve(f) == (326, 363010)


def test_day04():
    log.info("test_day04")
    d = days.day04
    assert d.solve(sio("aa bb cc dd ee"))[0] == 1
    assert d.solve(sio("aa bb cc dd aa"))[0] == 0
    assert d.solve(sio("aa bb cc dd aaa"))[0] == 1
    assert d.solve(sio("abcde fghij"))[1] == 1
    assert d.solve(sio("abcde xyz ecdab"))[1] == 0
    assert d.solve(sio("a ab abc abd abf abj"))[1] == 1
    assert d.solve(sio("iiii oiii ooii oooi oooo"))[1] == 1
    assert d.solve(sio("oiii ioii iioi iiio"))[1] == 0
    with open('input/day04') as f:
        assert d.solve(f) == (386, 208)


def test_day05():
    log.info("test_day05")
    d = days.day05
    with open('input/day05.test') as f:
        assert d.solve(f) == (5, 10)
    with open('input/day05') as f:
        assert d.solve(f) == (378980, 26889114)


def test_day06():
    log.info("test_day06")
    d = days.day06
    assert d.solve(sio("0\t2\t7\t0")) == (5, 4)
    with open('input/day06') as f:
        assert d.solve(f) == (7864, 1695)


def test_day07():
    log.info("test_day07")
    d = days.day07
    with open('input/day07.test') as f:
        assert d.solve(f) == ('tknk', 60)
    with open('input/day07') as f:
        assert d.solve(f) == ('eqgvf', 757)


def test_day08():
    log.info("test_day08")
    d = days.day08
    with open('input/day08.test') as f:
        assert d.solve(f) == (1, 10)
    with open('input/day08') as f:
        assert d.solve(f) == (4163, 5347)


def test_day09():
    log.info("test_day09")
    d = days.day09
    assert d.solve(sio("{}"))[0] == 1
    assert d.solve(sio("{{{}}}"))[0] == 6
    assert d.solve(sio("{{},{}}"))[0] == 5
    assert d.solve(sio("{{{},{},{{}}}}"))[0] == 16
    assert d.solve(sio("{<a>,<a>,<a>,<a>}"))[0] == 1
    assert d.solve(sio("{{<ab>},{<ab>},{<ab>},{<ab>}}"))[0] == 9
    assert d.solve(sio("{{<!!>},{<!!>},{<!!>},{<!!>}}"))[0] == 9
    assert d.solve(sio("{{<a!>},{<a!>},{<a!>},{<ab>}}"))[0] == 3
    assert d.solve(sio("<>"))[1] == 0
    assert d.solve(sio("<random characters>"))[1] == 17
    assert d.solve(sio("<<<<>"))[1] == 3
    assert d.solve(sio("<{!>}>"))[1] == 2
    assert d.solve(sio("<!!>"))[1] == 0
    assert d.solve(sio("<!!!>>"))[1] == 0
    assert d.solve(sio('<{o"i!a,<{i<a>'))[1] == 10
    with open('input/day09') as f:
        assert d.solve(f) == (11846, 6285)


def test_day10():
    log.info("test_day10")
    from common import knot
    h = knot.knot([int(n) for n in "3, 4, 1, 5".split(',')], 1, [], 5)
    assert h[0] * h[1] == 12
    assert knot.hstr(knot.knot([ord(i) for i in ""])) == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert knot.hstr(knot.knot([ord(i) for i in "AoC 2017"])) == '33efeb34ea91902bb2f59c9920caa6cd'
    assert knot.hstr(knot.knot([ord(i) for i in "1,2,3"])) == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert knot.hstr(knot.knot([ord(i) for i in "1,2,4"])) == '63960835bcdc130f0b66d7ff4f6a5a8e'
    d = days.day10
    with open('input/day10') as f:
        assert d.solve(f) == (4480, 'c500ffe015c83b60fad2e4b7d59dabc4')


def test_day11():
    log.info("test_day11")
    d = days.day11
    assert d.solve(sio("ne,ne,ne"))[0] == 3
    assert d.solve(sio("ne,ne,sw,sw"))[0] == 0
    assert d.solve(sio("ne,ne,s,s"))[0] == 2
    assert d.solve(sio("se,sw,se,sw,sw"))[0] == 3
    with open('input/day11') as f:
        assert d.solve(f) == (696, 1461)


def test_day12():
    log.info("test_day12")
    d = days.day12
    with open('input/day12.test') as f:
        assert d.solve(f) == (6, 2)
    with open('input/day12') as f:
        assert d.solve(f) == (169, 179)


def test_day13():
    log.info("test_day13")
    d = days.day13
    with open('input/day13.test') as f:
        assert d.solve(f) == (24, 10)
    with open('input/day13') as f:
        assert d.solve(f) == (1900, 3966414)


def test_day14():
    log.info("test_day14")
    d = days.day14
    with open('input/day14.test') as f:
        assert d.solve(f) == (8108, 1242)
    with open('input/day14') as f:
        assert d.solve(f) == (8316, 1074)


def test_day15():
    log.info("test_day15")
    d = days.day15
    with open('input/day15.test') as f:
        assert d.solve(f) == (588, 309)
    with open('input/day15') as f:
        assert d.solve(f) == (569, 298)


def test_day16():
    log.info("test_day16")
    d = days.day16
    with open('input/day16.test') as f:
        ops = d.parse_input(f)
        assert d.Operator(ops, 'abcde').apply_n(1) == 'baedc'
        assert d.Operator(ops, 'abcde').apply_n(2) == 'ceadb'
    with open('input/day16') as f:
        assert d.solve(f) == ('kpbodeajhlicngmf', 'ahgpjdkcbfmneloi')


def test_day17():
    log.info("test_day17")
    d = days.day17
    assert d.solve(sio("3"))[0] == 638
    with open('input/day17') as f:
        assert d.solve(f) == (1282, 27650600)


def test_day18():
    # TODO: There is a problem with multiprocessing on Travis CI
    # log.info("test_day18")
    # d = days.day18
    # with open('input/day18.test1') as f:
    #     assert d.solve(f)[0] == 4
    # with open('input/day18.test2') as f:
    #     assert d.solve(f)[1] == 3
    # with open('input/day18') as f:
    #     assert d.solve(f) == (1187, 1187)
    pass


def test_day19():
    log.info("test_day19")
    d = days.day19
    with open('input/day19.test') as f:
        assert d.solve(f) == ('ABCDEF', 38)
    with open('input/day19') as f:
        assert d.solve(f) == ('RUEDAHWKSM', 17264)


def test_day20():
    log.info("test_day20")
    d = days.day20
    with open('input/day20.test1') as f:
        assert d.solve(f)[0] == 0
    with open('input/day20.test2') as f:
        assert d.solve(f)[1] == 1
    with open('input/day20') as f:
        assert d.solve(f) == (243, 648)


def test_day21():
    log.info("test_day21")
    d = days.day21
    with open('input/day21.test') as f:
        assert d.solve_for(f, 2)[0] == 12
    with open('input/day21') as f:
        assert d.solve(f) == (167, 2425195)


def test_day22():
    log.info("test_day22")
    d = days.day22
    with open('input/day22.test') as f:
        assert d.solve_for(d.parse(f), 7, 0) == 5
    with open('input/day22.test') as f:
        assert d.solve_for(d.parse(f), 70, 0) == 41
    with open('input/day22.test') as f:
        assert d.solve_for(d.parse(f), 10000, 0) == 5587
    with open('input/day22.test') as f:
        assert d.solve_for(d.parse(f), 100, 1) == 26
    with open('input/day22.test') as f:
        assert d.solve_for(d.parse(f), 10000000, 1) == 2511944
    with open('input/day22') as f:
        assert d.solve(f) == (5176, 2512017)


def test_day23():
    log.info("test_day23")
    d = days.day23
    with open('input/day23') as f:
        assert d.solve(f) == (6724, 903)
