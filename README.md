# Created By ANONYMOUSx46

## Python Coded Revese Shell:

A Python-based reverse shell script that works seamlessly with the Kali Linux tool **netcat**. This script allows you to establish a remote connection to a machine, execute commands, and transfer files. The code can also be run through an obfuscator tool for added security.

## Prerequisites

- Python 3.x
- Kali Linux with netcat installed
- Obfuscator tool (optional)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/Reverse-shell.git
    cd Reverse-shell
    ```

2. **Configure the server address and port:**

    Edit the Python script to set your server's IP address and port:

    ```python
    server_address = 'YOUR_SERVER_IP'
    server_port = YOUR_SERVER_PORT
    ```

3. **Run the script:**

    ```bash
    python3 Rev3.py
    ```

## Usage

1. **Set up the listener on your Kali Linux machine:**

    ```bash
    nc -lvnp <PORT>
    ```

    Replace `<PORT>` with the port number you configured in the Python script.

2. **Run the reverse shell script on the target machine:**

    ```bash
    python3 Rev3.py
    ```

3. **Available Commands:**

    - `quit`: Exit the reverse shell.
    - `clear`: Clear the terminal screen.
    - `cd <directory>`: Change the current directory.
    - `set <var>=<value>`: Set an environment variable.
    - `upload <file_path>`: Upload a file to the target machine.
    - `download <file_path>`: Download a file from the target machine.
    - `rm <file_path>`: Remove a file from the target machine.
    - `mkdir <directory_path>`: Create a directory on the target machine.
    - `cat <file_path>`: Read a file's contents.
    - `python <script_path>`: Execute a Python script.

## Obfuscation (Optional)

For added security, you can run the script through an obfuscator tool. One popular option is [pyarmor](https://pypi.org/project/pyarmor/).

1. **Install pyarmor:**

    ```bash
    pip install pyarmor
    ```

2. **Obfuscate the script:**

    ```bash
    pyarmor pack -x " --exclude obf " reverse_shell.py
    ```

## Disclaimer

This project is intended for educational purposes only. The author is not responsible for any misuse of this tool.
