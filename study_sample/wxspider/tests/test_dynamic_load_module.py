#!/bin/python3
# -*- coding: utf-8 -*-

from argparse import Namespace


class Input:
    args = Namespace(arti=None, biz='狂人学堂', chrome=None, method='whole_page', page_limit='2', pipe='pipe_example', sleep=None)
    custom_pipe = []


def dynamic_load_call(url, sdir):
    sps = (Input.args.pipe if Input.args.pipe else '').split(',')
    for sp in sps:
        Input.custom_pipe.append(__import__(sp.strip()))

    for p in Input.custom_pipe:
        urls = p.crawl(url, sdir)


if __name__ == '__main__':
    dynamic_load_call('http://www.baidu.com', 'xxxxx')
