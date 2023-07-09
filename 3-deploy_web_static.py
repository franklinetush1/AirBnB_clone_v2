#!/usr/bin/python3

from datetime import datetime
from fabric.api import *
import os


def deploy():
    """Creates and distributes an archive to the web servers"""
    arch_path = do_pack()
    if arch_path is None:
        return False    
    return do_deploy(arch_path)


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


env.hosts = ['54.236.50.142', '52.87.231.81']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        archive_folder = filename.split(".")[0]
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_folder))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, archive_folder))
        run('rm /tmp/{}'.format(filename))        
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(archive_folder, archive_folder))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_folder))
        print("New version deployed!")
        return True
    except:
        return False
