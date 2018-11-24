5. IO, Debug, Import, Set, Dict
===============================

IO
--

Handling Input and Output.

Read & write file
-----------------

Introduce using file.
open(), modes (r/w/a binary/text), close(), with, iter over lines.

Iterate over lines::

  with open('/etc/hosts') as f:
      for line in f:
          print(line, end='')
  print("Has file f closed? {0}".format(f.closed))


Default encoding depends on OS settings (not always UTF-8).

Tuple unpacking
---------------

- Multi-assignment
- Unpacking in function call with `*`
- When list when tuple?

Debug
-----

- Run module with pdb
- Basic commands::

  > h: help
  > l: list
  > n: next
  > b: break
  > c: continue
  > p: print
  > s: step into

Import
------

- math
- import antigravity
- import this
- xkcd.com, news.ycombinator.com
- random

Python module
-------------

- What is a Python module?
- How to write a python module?
- How to run a Python module?

Dictionary
----------

- Ways to create dict: literal, dict comprehension, dict(list of tuples)
- What is a real dict, says English-Vietnamese dict? what are its properties?
  So does Python dict
- Only hashable objects can be used as key
- Present several real-world dicts
- Iterate over dict (k,v, items(), keys(), values())
- Iterate over key only
- Example with nested dict
- Dict keys has no order
- Introduction to JSON, serialization.
- Check membership (``x in list``)::

    if x in range(100000): # algorithm complexity O(N)

- Check membership of ``dict`` is ``O(1) - constant``

Set
---

- Like list, but uniq items.

- Let everyone enter ``{0, 1, 2, 8, 1000}``, is the result same on all machines?
  -> Set is unordered, so there is no indexing.
- It is unordered, NOT random, random is different order every time on same
  machine
- Operators: ``-``, ``^``, ``&``, ``|``
- Convert a list to a set
- dict.keys() are a set
- Key cannot be mutable, e.g List.
- `hash(all data type)` to see

Compare with is and ==
----------------------

- Use ``is`` only for boolean, ``None``, empty tuple.

Iterable
--------

List, tuple, dict, set, string.

Reading code
------------

- Important than write
- Let's practice https://github.com/saltstack/salt/blob/develop/salt/state.py

References
----------

- List vs Tuple: 
  - http://docs.python.org/faq/design.html#why-are-there-separate-tuple-and-list-data-types
  - http://docs.python.org/tutorial/datastructures.html#tuples-and-sequences
  - http://www.stackoverflow.com/questions/31192923/lists-vs-tuples-what-to-use-and-when
