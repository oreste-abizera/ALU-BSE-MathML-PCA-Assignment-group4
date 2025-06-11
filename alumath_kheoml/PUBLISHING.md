# Publishing to PyPI

This guide explains how to publish the `alumath_kheoml` package to PyPI so it can be installed with pip.

## Prerequisites

1. Create a PyPI account at https://pypi.org/account/register/
2. Install required tools:
   ```bash
   pip install build twine
   ```

## Building the Package

1. Navigate to the package directory:
   ```bash
   cd alumath_kheoml
   ```

2. Build the package:
   ```bash
   python -m build
   ```
   This will create distribution files in the `dist/` directory.

## Testing the Package

Before uploading to PyPI, you can test the package on TestPyPI:

1. Create a TestPyPI account at https://test.pypi.org/account/register/

2. Upload to TestPyPI:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

3. Install from TestPyPI:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ alumath_kheoml
   ```

4. Test the installation:
   ```python
   from alumath_kheoml import Matrix, matrix_multiply
   import numpy as np
   
   A = Matrix(np.array([[1, 2], [3, 4]]))
   print(A)
   ```

## Publishing to PyPI

If everything works correctly on TestPyPI, you can publish to the real PyPI:

1. Upload to PyPI:
   ```bash
   python -m twine upload dist/*
   ```

2. Enter your PyPI username and password when prompted.

3. Your package should now be available on PyPI and can be installed using:
   ```bash
   pip install alumath_kheoml
   ```

## Updating the Package

To update the package:

1. Update the version number in `setup.py` and `__init__.py`
2. Rebuild the package:
   ```bash
   python -m build
   ```
3. Upload the new version to PyPI:
   ```bash
   python -m twine upload dist/*
   ```
