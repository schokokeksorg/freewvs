contribute
==========

If you want to contribute you can use pull requests and the issue tracker
on our github mirror:

 https://github.com/schokokeksorg/freewvs/

If you prefer you can also contact us via e-mail:

 https://schokokeks.org/kontakt

coding style
============

Code should conform to the PEP8 coding standard. Furthermore we enable
additional rules in pycodestyle and run some other linting tools
(pylint, pyflakes, dlint).

The freewvsdb files should be linted JSON as created by json.dumps with
2 spaces indenting.

All code and JSON style requirements can be checked by running the unit
tests:

```
python -m unittest
```
