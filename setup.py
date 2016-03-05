from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Build import cythonize
except ImportError:
    use_cython = False
else:
    use_cython = True

ext = ".py" if use_cython else ".c"
ext_modules = [Extension("genetic", ["genetic" + ext])]

if use_cython:
    ext_modules = cythonize(ext_modules)

setup(
    ext_modules=ext_modules,
)

