def parse_args():
    import argparse
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