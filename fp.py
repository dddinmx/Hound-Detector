#coding:utf-8

import sys
from banner import banner,output

def main():
    banner.banner()
    if len(sys.argv)!=3 and sys.argv[1] != "-h":	
         print("-h 查看帮助")
         sys.exit()
    parser = output.create_arg_parser()
    args = parser.parse_args()
    if args.url:
        url = sys.argv[2]
        output.printcmd(url)
    if args.file:
        file = sys.argv[2]
        with open(file, 'r') as file:
        	for line in file:
                 url = line.strip()
                 output.printcmd(url)

if __name__ == "__main__":
    main()
