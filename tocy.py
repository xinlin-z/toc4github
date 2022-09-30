#!/usr/bin/env python3
import sys
import re
import argparse
from functools import singledispatch


def _make_toc(lines):
    toc = ''
    pos = -1
    skip = 0
    for i,line in enumerate(lines):
        # skip empty line
        if (line:=line.strip()) == '':
            continue
        # skip code block started with 4 space
        if line.startswith(' '*4):
            continue
        # skip ``` block
        if line.startswith('```'):
            skip = abs(skip-1)
        if skip:
            continue
        # try to find placeholder {tocy} and skip
        if line.strip().lower() == '{tocy}':
            pos = i
            continue
        # search and join toc
        if strs:=re.match(r'\s*(#+)(.*)',line):
            h = strs.group(1)
            if (hn:=len(h)) > 6:  # max head level is 6
                continue
            rest = strs.group(2).strip()
            # git rid of markdown syntax elements ~*_
            while a:=re.search(r'([~*_]{1,2})(.*)\1',rest):
                rest = rest[:a.start()] + a.group(2) + rest[a.end():]
            rest = re.sub(r'\s', '-', rest)  # space --> -
            rest = re.sub(r'[^-\w]', '', rest)  # squeeze other chars
            toc += ''.join((' '*(hn-1)*4, '* ',
                           '[',strs.group(2).strip(),'](#', rest,')'))+'\n'
    else:
        if skip:
            raise ValueError('``` block is open.')

    return pos, toc.rstrip('\n')


@singledispatch
def make_toc(lines):
    """Return the TOC contents."""
    return _make_toc(lines)[1]


@make_toc.register(str)
def _(strlines):
    return _make_toc(strlines.split('\n'))[1]


# $ python3 tocy.py [--dryrun] path/to/README.md
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-V', action='version',
                        version='tocy V0.13 by xinlin-z')
    parser.add_argument('--dryrun', action='store_true',
                        help='do not really write input file')
    parser.add_argument('mdfile',
                        help='input markdown file, like readme.md')
    args = parser.parse_args()

    try:
        with open(args.mdfile) as f:
            lines = f.readlines()
        pos, toc = _make_toc(lines)
        if pos == -1:
            raise ValueError('no placeholder found.')
        if args.dryrun:
            print(toc)
        else:
            lines[pos] = toc + '\n'
            with open(args.mdfile,'w') as f:
                f.write(''.join(lines))
    except Exception as e:
        print('Err:', str(e))
        sys.exit(1)


