#!/bin/bash
# script that sets up the web servers for deployment
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "25i\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
