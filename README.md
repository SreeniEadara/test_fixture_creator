# Test Fixture Creator
Sreenivas Eadara

## Overview
Used in the generation of test fixtures for boards designed with test points.
Will generate an empty PCB with the same edge cuts, dimensions, and test points as a provided input. The test points will retain their nets.

The copied over test points can then be replaced with pogo pins, headers, etc. by opening in pcbnew and replacing.

## Usage
Create a mamba environment using the provided environment.yml, OR install the kiutils package using pip.

```
mamba env create -f environment.yml
```

OR

```
pip install kiutils
```

Once you have the mamba environment active / have installed kiutils, run test_fixture.py.

```
python3 test_fixture.py
```
