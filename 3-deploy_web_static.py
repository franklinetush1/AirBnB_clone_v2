#!/usr/bin/python3

def deploy():
    """Creates and distributes an archive to the web servers"""
    arch_path = do_pack()
    if not arch_path:
        return False    
    return do_deploy(arch_path)
