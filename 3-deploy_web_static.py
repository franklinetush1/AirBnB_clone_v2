#!/usr/bin/python3
from fabric import task
from datetime import datetime

def do_pack():
    """Returns the path of the generated archive if successful,else None"""
    time_st = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(time_st)
    local("mkdir -p versions")
  	output = local("tar -czvf versions/{} web_static".format(archive_name))
	archive_path = "versions/{}."format(archive_name)
    if output.failed:
        return None
    return archive_path



def deploy():
    """Creates and distributes an archive to the web servers"""
    arch_path = do_pack()
    if not arch_path:
        return False    
    return do_deploy(arch_path)
