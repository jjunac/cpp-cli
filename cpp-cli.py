#!/usr/bin/env python

import os
import argparse

from sample import makefile, cpp, vscode


def new_project(args):
    print " * Creating directory..."
    name = args.name
    if os.path.exists(name):
        print "Directory already exists"
        return
    os.makedirs(name)

    print " * Generating Makefile..."
    makefile.generate(name)

    print " * Generating main cpp file..."
    cpp.generate_main(name)

    print " * Generating VSCode utility files..."
    os.makedirs("{}/.vscode".format(name))
    vscode.generate_launch(name)
    vscode.generate_tasks(name)
    vscode.generate_properties(name)
    vscode.generate_settings(name)

    print "Done"


def generate_class(args):
    for name in args.name:
        print " * Generating {} class file and header...".format(name)
        cpp.generate_class(name)
        cpp.generate_header(name)
    print " * Updating Makefile..."
    makefile.update_sources(args.name)
    print "Done"


def analyze_args():
    parser = argparse.ArgumentParser()

    subparser_command = parser.add_subparsers(title="commands", description="available commands")

    parser_new = subparser_command.add_parser("new", help="create new project")
    parser_new.add_argument("name", help="name of the project")
    parser_new.set_defaults(func=new_project)

    parser_generate = subparser_command.add_parser("g", help="generate new files")
    subparser_generate = parser_generate.add_subparsers(title="structure", description="available structure to generate")

    parser_generate_class = subparser_generate.add_parser("class", help="generate class files")
    parser_generate_class.add_argument("name", nargs="+", help="name of the classes")
    parser_generate_class.set_defaults(func=generate_class)

    return parser.parse_args()


def main():
    print "C++ CLI by Jeremy Junac"
    args = analyze_args()
    args.func(args)

if __name__ == '__main__':
    main()