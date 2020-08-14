import argparse
import discord
from client.client import Client

def main():
    parser = argparse.ArgumentParser(description='Creating and management discord server with python')
    parser.add_argument('-t', '--token', type=str, metavar='TOKEN', required=True,
                        help='Your developer bot token from discord')
    parser.add_argument('-g', '--guild', type=int, metavar='ID', required=True,
                        help='Your guild id, server id from discord')
    parser.add_argument('-s', '--setup', type=bool, metavar='BOOL', default=False,
                        help="Create server from scratch (True/False)")
    parser.add_argument('-l', '--logger', type=int, metavar='ID', default=20,
                        help='Custom logger output (ID  from logging module')
    args = parser.parse_args()
    client = Client(args.guild, run_setup=args.setup, log_level=args.logger)
    client.run(args.token)


if __name__ == "__main__":
    main()