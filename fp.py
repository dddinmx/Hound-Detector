#coding:utf-8

import sys,datetime
from banner import banner,output

def endtime():
     time = datetime.datetime.now().strftime('%H:%M:%S')
     return time

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
        print ("["+endtime()+"] "+"Completed End")
    if args.file:
        file = sys.argv[2]
        with open(file, 'r') as file:
        	for line in file:
                 url = line.strip()
                 output.printcmd(url)
        print ("["+endtime()+"] "+"Completed End")

if __name__ == "__main__":
    main()
