* [Tocy](#Tocy)
    * [Installation](#Installation)
    * [Command Line Usage](#Command-Line-Usage)
    * [In Code Usage](#In-Code-Usage)
    * [Showcase](#Showcase)

# Tocy

A tiny tool to automatically create Table Of Contents (TOC) for markdown
file, like README.md of Github.com.

## Installation

``` shell
$ pip3 install tocy
```

## Command Line Usage

Insert a placeholder `{tocy}` in the proper line of README.md, then:

``` shell
$ python3 -m tocy <path/to/README.md>
```

You can also use `--dryrun` to check the generated TOC first:

``` shell
$ python3 -m tocy --dryrun <path/to/README.md>
```

> If no placeholder found in README.md, dryrun is True! If more than one
placeholders found, the last one take effect! Placehoder should be a
single line by itself.

## In Code Usage

Or, you can call `make_toc` in your code:

``` python
>>> from tocy import make_toc
>>> lines = """
... # head1
... ## head2
... ### head3
... """
>>> print(make_toc(lines))
* [head1](#head1)
    * [head2](#head2)
        * [head3](#head3)
```

`make_toc` only return the generated TOC, and you should insert them to
your markdown file anywhere you like by yourself.

## Showcase

![tocy](/tocy.png)

