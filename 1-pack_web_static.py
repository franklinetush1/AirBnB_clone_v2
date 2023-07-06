#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Returns the path of the generated archive if successful,else None"""
    time_st = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(time_st)
    local("mkdir -p versions")
    output = local("tar -czvf versions/{} web_static".format(archive_name))
    archive_path = "versions/{}".format(archive_name)
    if output.failed:
        return None
    return archive_path
