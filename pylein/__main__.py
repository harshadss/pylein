import argparse

from .workflow import create

def parse_cmd_args():
    cmd = argparse.ArgumentParser(description="""Create a standard project
                                               structure for Python projects""")
    cmd.add_argument('--name', action = 'store',
                     help = """Name of the project""")    
    # type is NOT optional at the same time need it to be non positional,
    # forced to be required
    cmd.add_argument('--template', action = 'store', required = True,
                     help = """What type of project?""", type=str,
                     choices=["lib", "app"])
    cmd.add_argument('--test', action = 'store_true',
                     help = """Add test information and files?""")

    args = cmd.parse_args()
    return args
    
def main():
    args = parse_cmd_args()
    create(args)
    
if __name__ == '__main__':
    main()
