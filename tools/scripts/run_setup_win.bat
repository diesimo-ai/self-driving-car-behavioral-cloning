@echo off

echo "installing requirements setup ..."

SETLOCAL 

REQ_FILE_PATH=".\requirements.txt"

pip3 install -r $REQ_FILE_PATH\requirements.txt -y