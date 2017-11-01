# Orient

*Align pages quickly.*

## The context

We want to quickly scan and align a large number of sheets. We add 4 dots to
each sheet of paper:

    +---------+
    |    *    |
    |         |
    | *     * |
    |         |
    |    *    |
    +---------+

and our machine scans the image and produces `(x, y)` coordinates for each dot:

```
data = [(1940, 861), (1094, 211), (257, 857), (1096, 1604)]
```

## The problem

Sometimes the user does not properly align the sheet of paper on the scanner.
The sheet of paper could be diagonal or even sideways. Furthermore, the dots
are themselves not perfectly aligned. The question becomes: how can we
programmatically determine the proper orientation, given the presence of these
four dots?

## The solution: `orient`

Example:

```sh
>>> import orient
>>> data = [(1940, 861), (1094, 211), (257, 857), (1096, 1604)]
>>> print(orient.planes(data))
{'length': ((1940, 861), (257, 857)), 'width': ((1094, 211), (1096, 1604))}
```

As shown above, `orient.planes()` will give you the coordinates for the
`length` plane and the `width` plane.

## Tests

Test data sets are provided in `test.py`.
