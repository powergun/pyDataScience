import argparse
import sys


def parse_args(args):
    p = argparse.ArgumentParser()
    subp = p.add_subparsers(title='scenes', dest='scene')
    basketball = subp.add_parser('basketball')
    basketball.add_argument('take')
    return p.parse_args(args)


def main():
    arg = parse_args(sys.argv[1:])
    print(arg)
    if arg.scene == 'basketball':
        do_basketball_dashboard(arg)


def do_basketball_dashboard(arg):
    if arg.take == '4':
        import basketball_dashboard
