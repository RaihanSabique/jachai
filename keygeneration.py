import os
import subprocess

def key_pair_generator():
    cmd1='ssh-keygen -t rsa -b 1024 -m PEM -f jwtRS256.key'
    os.system(cmd1)
    cmd2='openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub'
    os.system(cmd2)
    private_key = subprocess.run(['cat', 'jwtRS256.key'], stdout=subprocess.PIPE)
    public_key = subprocess.run(['cat', 'jwtRS256.key.pub'], stdout=subprocess.PIPE)
    print(private_key.stdout.decode('utf-8'))
    print(public_key.stdout.decode('utf-8'))
    return private_key.stdout.decode('utf-8'),public_key.stdout.decode('utf-8')
