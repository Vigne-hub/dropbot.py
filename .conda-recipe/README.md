Conda recipe to build `dropbot` package python 3 bindings.

Build
=====

Install `conda-build`:

    conda install conda-build

Build recipe (from this directory):

    conda build . -c alexsk -c dropbot -c conda-forge


Install
=======

The pre-built package may be installed from the [`alexsk`][2] channel using:

    conda install vignesh229::dropbot -c alexsk -c dropbot -c conda-forge


[1]: https://anaconda.org/sci-bots/dropbot
[2]: https://anaconda.org/sci-bots
