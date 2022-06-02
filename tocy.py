#!/usr/bin/env python3
import sys
import re


def make_toc(readme, dryrun=True):
    """Replace placeholder by TOC (dryrun=False), and return toc string.
    If no placeholder found, dryrun is alway True.
    """
    with open(readme) as f:
        lines = f.readlines()

    toc = ''
    pos = -1
    skip = 0
    for i,line in enumerate(lines):
        # skip empty line
        if line.rstrip('\n').strip() == '':
            continue
        # skip code block started with 4 space
        if line.startswith(' '*4):
            continue
        # skip ``` block
        if line.startswith('```'):
            skip = abs(skip-1)
        if skip: continue
        # try to find placeholder {tocy} and skip
        if line.strip().lower() == '{tocy}':
            pos = i
            continue
        # search and print out #+ title
        if strs:=re.match(r'\s*(#+)(.*)',line):
            ht = strs.groups()[0]
            if (htl:=len(ht)) > 6:  # max head level is 6
                continue
            rest = strs.groups()[1].strip()
            # git rid of markdown syntax elements ~*_
            while a:=re.search(r'([~*_]{1,2})(.*)\1',rest):
                rest = rest[:a.start()] + a.groups()[1] + rest[a.end():]
            rest = re.sub(r'\s', '-', rest)  # space --> -
            rest = re.sub(r'[^-\w]', '', rest)  # squeeze other chars
            toc += ''.join((' '*(htl-1)*4, '* ',
                           '[',strs.groups()[1].strip(),'](#', rest,')'))+'\n'

    if pos != -1 and dryrun is False:
        # There is a \n originally, the last \n in toc is used here.
        lines[pos] = toc
        with open(readme, 'w') as f:
            f.write(''.join(lines))

    return toc.rstrip('\n')


# python3 tocy.py [--dryrun] README.md
if __name__ == '__main__':
    try:
        if len(sys.argv) > 2:
            if sys.argv[1] == '--dryrun':
                print(make_toc(sys.argv[2]))
            else:
                raise ValueError('Command line error.')
        else:
            make_toc(sys.argv[1], False)
    except Exception as e:
        print(repr(e))


