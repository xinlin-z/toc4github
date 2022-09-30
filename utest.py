import unittest
from tocy import make_toc
import os
import subprocess


def shcmd(cmd, shell=False):
    """execute a cmd without shell, return exitcode"""
    proc = subprocess.run(cmd if shell else cmd.split(),
                          shell=shell,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    return proc.returncode


raw = """
{tocy}

# Test
## header
### head 3
#### head 4
##### head 5
###### head 6
####### not a head 7

# _abc
# a & b & c
# a       c
# a ( c )
# a(c)
# a.,.,!@#$%^&*().,.7

# *italic 12345*
# **bold 12345**
# _italic2 12345_
# __bold2 12345__
# ~cross out~
# ~~cross out 2~~
# **~bold cross out~**
# __~~blod cross out 2~~__
"""
cooked = ('* [Test](#Test)\n    '
          '* [header](#header)\n        '
          '* [head 3](#head-3)\n            '
          '* [head 4](#head-4)\n                '
          '* [head 5](#head-5)\n                    '
          '* [head 6](#head-6)\n'
          '* [_abc](#_abc)\n'
          '* [a & b & c](#a--b--c)\n'
          '* [a       c](#a-------c)\n'
          '* [a ( c )](#a--c-)\n'
          '* [a(c)](#ac)\n'
          '* [a.,.,!@#$%^&*().,.7](#a7)\n'
          '* [*italic 12345*](#italic-12345)\n'
          '* [**bold 12345**](#bold-12345)\n'
          '* [_italic2 12345_](#italic2-12345)\n'
          '* [__bold2 12345__](#bold2-12345)\n'
          '* [~cross out~](#cross-out)\n'
          '* [~~cross out 2~~](#cross-out-2)\n'
          '* [**~bold cross out~**](#bold-cross-out)\n'
          '* [__~~blod cross out 2~~__](#blod-cross-out-2)')


class test_make_toc(unittest.TestCase):

    def test_make_toc_1(self):
        toc = make_toc(raw)
        self.assertEqual(toc, cooked)
        toc = make_toc(raw.split('\n'))
        self.assertEqual(toc, cooked)

    def test_make_toc_2(self):
        fn = '__tocy_test.txt'
        with open(fn,'w') as f:
            f.write(raw)
        shcmd('python3 tocy.py %s' % fn)
        with open(fn) as f:
            cont = f.read()
        self.assertEqual(cont, '\n'+cooked+raw[7:])
        os.remove(fn)

    def test_make_toc_3(self):
        raw = """
        ```
        123456
        """
        self.assertRaises(ValueError, make_toc, raw)


if __name__ == '__main__':
    unittest.main()
