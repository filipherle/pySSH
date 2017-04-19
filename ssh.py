import paramiko
from paramiko import client
import time
SSH = paramiko.SSHClient()
import sys
sys.dont_write_bytecode = True
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'

def SSHConnect(ip, user, passwd):
    SSH.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())
    try:
        SSH.connect(ip, username=user, 
            password=passwd)
    except:
        print "Error!"
        exit(1)
def SSHClose(time_in_seconds):
    try:
        time.sleep(time_in_seconds)
        SSH.close()
    except TypeError:
        time.sleep(1)
        SSH.close()
        
def SSHExecute(command_to_exec):
    stdin, stdout, stderr = SSH.exec_command(command_to_exec)
    stdin.close()
    for line in stdout.read().splitlines():
        print(line)
def SSHColors(color, msg):
    if color == "green":
        print GREEN + msg
    elif color == "purple":
        print PURPLE + msg
    elif color == "cyan":
        print CYAN + msg
    elif color == "darkcyan":
        print DARKCYAN + msg
    elif color == "tan":
        print TAN + msg
    elif color == "red":
        print RED + msg
    elif color == "blue":
        print BLUE + msg
    elif color == "yellow":
        print YELLOW + msg
    else:
        print "error"
        
