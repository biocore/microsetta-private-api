from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("microsetta-private-api")
except PackageNotFoundError:
    __version__ = "0.0.0"
