"""Feature loader for the API package.

An __init__.py like this is meant to import all the public-facing
functionality to the package user, i.e. expose the package's API.
"""

# EX: from app_root_dir.target_dir.target_file import target_method
from camhudson.views.index import get_index
