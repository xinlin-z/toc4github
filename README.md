* [Tocy](#Tocy)
    * [Usage](#Usage)
    * [Test](#Test)
    * [Showcase](#Showcase)

# Tocy

A tiny tool to automatically create Table Of Content (TOC) for README.md
of Github.com.

## Usage

Insert a placeholder `{tocy}` in the proper line of README.md, then:

``` shell
$ python3 tocy.py <path/to/README.md>
```

You can also use `--dryrun` to check TOC lines first:

``` shell
$ python3 tocy.py --dryrun <path/to/README.md>
```

> If no placeholder found in README.md, dryrun is True! If more than one
placeholders found, the last one take effect!

Or, you can call `make_toc` in your code:

``` python
...
from tocy import make_toc
...
print(make_toc(readme_file))
make_toc(readme_file, dryrun=False)
...
```

## Test

``` shell
$ python3 tocy.py --dryrun test/README.md
* [Test](#Test)
    * [header](#header)
        * [head 3](#head-3)
            * [head 4](#head-4)
                * [head 5](#head-5)
                    * [head 6](#head-6)
* [_abc](#_abc)
* [a & b & c](#a--b--c)
* [a       c](#a-------c)
* [a ( c )](#a--c-)
* [a(c)](#ac)
* [a.,.,!@#$%^&*().,.7](#a7)
* [*italic 12345*](#italic-12345)
* [**bold 12345**](#bold-12345)
* [_italic2 12345_](#italic2-12345)
* [__bold2 12345__](#bold2-12345)
* [~cross out~](#cross-out)
* [~~cross out 2~~](#cross-out-2)
* [**~bold cross out~**](#bold-cross-out)
* [__~~blod cross out 2~~__](#blod-cross-out-2)
```

## Showcase

![tocy](/tocy.png)

