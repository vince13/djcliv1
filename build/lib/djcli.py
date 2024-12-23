#!/usr/bin/env python3

import sys
import subprocess
import json
import os


CONFIG_FILE = "djcli_github.json"
COMMANDS = {}

def load_custom_commands():
    global COMMANDS
    try:
        with open(CONFIG_FILE, "r") as file:
            COMMANDS = json.load(file)
    except FileNotFoundError:
        print(f"Configuration file '{CONFIG_FILE}' not found.")
        COMMANDS = {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{CONFIG_FILE}'.")
        COMMANDS = {}

def execute_command(user_command, commands):
    """Execute the mapped command."""
    # Allow both $ <command> and djcli_github <command>
    if user_command.startswith("$"):
        user_command = user_command[1:]  # Strip the `$`

    if user_command in commands:
        full_command = commands[user_command]
        print(f"Running: {' '.join(full_command)}")
        try:
            subprocess.run(full_command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
    else:
        print(f"Command '{user_command}' not recognized.")
        print("Available commands:")
        for alias in commands.keys():
            print(f"  $ {alias}")


def main():
    load_custom_commands()

    if len(sys.argv) < 2:
        print("Usage: djcli_github <command>")
        print("Available commands:")
        for alias, full_command in COMMANDS.items():
            print(f"  $ {alias} -> {full_command}")
        sys.exit(1)

    user_command = " ".join(sys.argv[1:]).lower()

    if user_command in COMMANDS:
        full_command = COMMANDS[user_command]
        print(f"Running: {full_command}")
        try:
            subprocess.run(full_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
    else:
        print(f"Command '{user_command}' not recognized.")
        print("Available commands:")
        for alias, full_command in COMMANDS.items():
            print(f"  $ {alias} -> {full_command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
