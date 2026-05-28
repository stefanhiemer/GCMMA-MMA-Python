from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

ext = Extension(
    "mmapy.mmacy",
    sources=["src/mmapy/mmacy.pyx"],
    include_dirs=[np.get_include()],
)

setup(
    name="mmapy",
    ext_modules=cythonize([ext], language_level=3),
    package_dir={"": "src"},
)
