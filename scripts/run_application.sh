#!/bin/bash
cd ../

. env/bin/activate
cd src
sudo --preserve-env $(which python) app.py
