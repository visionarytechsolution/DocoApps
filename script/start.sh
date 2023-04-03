#!/bin/bash
cd /home/ubuntu
python3 manage.py migrate
sudo tee /etc/systemd/system/django.service <<EOF
[Unit]
Description=Django server daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/
ExecStart=/usr/bin/python3 manage.py runserver 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl start django
sudo systemctl enable django
sudo systemctl status django