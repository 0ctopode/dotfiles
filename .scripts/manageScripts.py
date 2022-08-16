#!/usr/bin/python3.10

"""
manageScripts.py - HRBush - 07/01/21
Command line tool to add and remove entries in the rofi script launcher
"""
import os

cmd_file = '/home/hrbush/.config/rofi/cmd.csv'


def add_entry():
    label = input("Script label: ")
    path = input("Path to script: ")

    f = open(cmd_file, 'a')
    f.write(label + ',' + path + '\n')
    f.close()


def remove_entry():
    label = input("Label of entry to remove: ")

    with open(cmd_file, 'r') as f:
        lines = f.readlines()
    with open(cmd_file, 'w') as f:
        for line in lines:
            if not line.startswith(label):
                f.write(line)


def main():
    response = input("<add> or <remove> entry?: ")
    if response.lower() == 'add':
        add_entry()
    elif response.lower() == 'remove':
        remove_entry()


if __name__ == '__main__':
    main()

