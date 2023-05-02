#!/usr/bin/env python3
"""
Author:   xinlin-z
Github:   https://github.com/xinlin-z/toc4github
Blog:     https://cs.pynote.net
License:  MIT
"""
import sys
import re
import argparse
from functools import singledispatch
from typing import Iterable, Union


def _make_toc(lines: Iterable[str]) -> tuple[int,str]:
    toc = ''
    pos = -1
    skip = 0
    for i,line in enumerate(lines):
        # skip empty line
        if(line:=line.strip()) == '':
            continue
        # skip code block started with 4 space
        if line.startswith(' '*4):
            continue
        # skip ``` block
        if line.startswith('```'):
            skip = abs(skip-1)
        if skip:
            continue
        # try to find placeholder {toc} and skip
        if line.strip().lower() == '{toc}':
            pos = i
            continue
        # line search and make toc
        if strs:=re.match(r'\s*(#+)\s(.*)',line):
            h = strs.group(1)
            if (hn:=len(h)) > 6:  # max head level is 6
                continue
            rest = strs.group(2).strip()
            # remove markdown syntax elements ~*_
            while a:=re.search(r'([~*_]{1,2})(.*)\1',rest):
                rest = rest[:a.start()] + a.group(2) + rest[a.end():]
            rest = re.sub(r'\s', '-', rest)  # space --> -
            rest = re.sub(r'[^-\w]', '', rest)  # squeeze other chars
            toc += ''.join((' '*(hn-1)*4, '* ',
                           '[',strs.group(2).strip(),'](#', rest,')'))+'\n'
    else:
        if skip:
            raise ValueError('``` block is open.')

    return pos, toc


@singledispatch
def make_toc(lines: Union[list[str],str]) -> str:
    """Return the TOC contents."""
    return _make_toc(lines)[1]


@make_toc.register
def _(strlines: str) -> str:
    return _make_toc(strlines.split('\n'))[1]


_VER = 'toc4github V0.16 by xinlin-z with love'\
       ' (https://github.com/xinlin-z/toc4github)'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-V', '--version', action='version', version=_VER)
    parser.add_argument('-d','--dryrun', action='store_true',
                        help='do not touch file, only show the TOC')
    parser.add_argument('-t','--title', action='store_true',
                        help='add a fixed title: Table of Contents')
    parser.add_argument('markdown_file',
                        help='the input markdown file, like README.md')
    args = parser.parse_args()

    try:
        with open(args.markdown_file) as f:
            lines = f.readlines()
        pos, toc = _make_toc(lines)
        toc = ('','# Table of Contents\n\n')[args.title] + toc
        if args.dryrun:
            print(toc, end='')
            sys.exit(0)
        if pos == -1:
            raise ValueError('No {toc} placeholder found!')
        lines[pos] = toc
        with open(args.markdown_file,'w') as f:
            f.write(''.join(lines))
    except Exception as e:
        print('Err:', str(e))
        sys.exit(1)


