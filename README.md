# Table of Contents

* [toc4github Intro](#toc4github-Intro)
* [Install](#Install)
* [Command Line](#Command-Line)
* [Interface](#Interface)
* [Screenshot](#Screenshot)

# toc4github Intro

A tiny tool to automatically create Table of Contents (TOC) for markdown
file, like README.md of Github.com.

# Install

``` shell
$ pip install toc4github
```

# Command Line

Insert a placeholder `{toc}` in the proper line of README.md, this
is the start line of TOC, then run:

``` shell
$ python3 -m toc4github <path/to/README.md>
```

Now, the placeholder is replaced by TOC, markdown file is updated.

You can also use `--dryrun` to check the generated TOC first:

``` shell
$ python3 -m toc4github --dryrun <path/to/README.md>
```

This would only print out TOC, nothing is changed.

`--title` option is used if you need a title just before TOC. The title
is always `Table of Contents`.

# Interface

Or, you can call `make_toc` in your code:

``` python
>>> from toc4github import make_toc
>>> a = """
... # head1
... ## head2
... ### head3
... #### head4
... Now, it's time to say something...:)
... ### head3 again
... ## head2 again
... Today is a good day
... ## head3 again again
... Tomorrow will be fine, trust me!^___^
... # last head1
... The end.
... """
>>> print(make_toc(a))
* [head1](#head1)
    * [head2](#head2)
        * [head3](#head3)
            * [head4](#head4)
        * [head3 again](#head3-again)
    * [head2 again](#head2-again)
    * [head3 again again](#head3-again-again)
* [last head1](#last-head1)
```

`make_toc` only return the generated TOC, and you should insert them to
your markdown file anywhere you like by yourself.

# Screenshot

![toc4github](/toc4github.png)

Be happy with github...^___^
