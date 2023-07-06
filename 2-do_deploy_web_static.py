#!/usr/bin/python3
"""Script that Distributes an archive to the web servers"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.236.50.142', '52.87.231.81']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        archive_folder = archive_filename.split(".")[0]
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
