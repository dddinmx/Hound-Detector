import urllib3,datetime,argparse
from webinfo import web_info
from cms import check,checkweb

green = "\033[1;32;m"
yellow = "\033[1;33;m"
red =  "\033[1;31m"
reset = "\033[0;0m"
blue = "\033[1;34m"
white = "\033[1;37m"

def printcmd(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    starttime = datetime.datetime.now().strftime('%H:%M:%S')
    print("["+starttime+"] "+white+"[+URL]: "+reset+url)
    header, body, title, status_code = web_info.get_info(url)
    icon_hash = web_info.get_iconhash(url)
    cw = checkweb.Compared(header, body, title)
    checkwebtime = checkweb.checkwebtime()
    ccms = check.rule(header,body,title,icon_hash)
    checkcmstime = check.checkcmstime()
    print ("["+checkwebtime+"] "+green+"[+"+status_code+"] "+reset+yellow+
    		cw+reset+" "+url+ " "+blue+"["+title+"]"+reset)
    print ("["+checkcmstime+"] "+white+"[CMS]: "+reset+red+ccms+reset+"\n")

def create_arg_parser():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-u", "--url", help="Add a URL")
    parser.add_argument("-f", "--file", help="Add a document path")
    return parser