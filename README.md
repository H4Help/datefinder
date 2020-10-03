datefinder - extract dates from text (H4H Fork)
====================================

This is a fork of datefinder.

A python module for locating dates inside text. Use this package to extract all sorts 
of date like strings from a document and turn them into datetime objects.

This fork adds additional functionality to find datetime objects in common french language patterns.

This module finds the likely datetime strings and then uses  
`dateutil` to convert to the datetime object.


Installation
------------

```bash
python setup.py install
```

How to Use
----------

```python
t = "29/06/2020 à 10h00"
    matches = [i for i in datefinder.find_dates(t)]
    d = datetime(2020, 6, 29, 10, 0, 0, 0)
    assert d in matches
```

Support
-------

For any issues please reach out to d.katz@humans4help.com 

