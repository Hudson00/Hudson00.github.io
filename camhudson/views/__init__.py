"""Feature loader for the API package.

An __init__.py like this is meant to import all the public-facing
functionality to the package user, i.e. expose the package's API.
"""

# EX: from app_root_dir.target_dir.target_file import target_method
from camhudson.views.anonymous import handle_anonymous_message
from camhudson.views.contact import get_contact_info
from camhudson.views.index import get_index
from camhudson.views.resume import get_resume
from camhudson.views.robots import get_robots
from camhudson.views.static import get_static_file
from camhudson.views.page_not_found import get_404
