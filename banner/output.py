#coding:utf-8

import urllib3,datetime,argparse
from webinfo import web_info
from cms import check,checkweb,wappaly

green = "\033[1;32;m"
yellow = "\033[1;33;m"
red =  "\033[1;31m"
reset = "\033[0;0m"
blue = "\033[1;34m"
white = "\033[1;37m"
cyan = "\033[0;36m"

def printcmd(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    starttime = datetime.datetime.now().strftime('%H:%M:%S')
    print("["+starttime+"] "+red+"[+URL]: "+reset+url)
    header, body, title, status_code = web_info.get_info(url)
    if status_code == "200":
        icon_hash = web_info.get_iconhash(url)
        cw = checkweb.Compared(header, body, title)
        checkwebtime = checkweb.checkwebtime()
        print ("["+checkwebtime+"] "+green+"[+"+status_code+"] "+reset+yellow+
        		cw+reset+" "+url+ " "+blue+"["+title+"]"+reset)
        ccms = check.rule(header,body,title,icon_hash)
        cwapply = wappaly.wappaly(url)
        checkwallytime = wappaly.checkwallytime()
        if (cwapply and ccms) is not None:
            ccms_set = set(ccms.split(", "))
            cwapply_set = set(cwapply.split(", "))
            cwcms_set = ccms_set | cwapply_set
            cwcms_list = list(cwcms_set)
            cwcms_list.sort()
            cwcms_result = "[" + "] [".join(cwcms_list) + "]"
            print ("["+checkwallytime+"] "+white+"[FP]: "+reset+cyan+cwcms_result+reset+"\n")
        else:
            pass
    else:
        icon_hash = web_info.get_iconhash(url)
        cw = checkweb.Compared(header, body, title)
        checkwebtime = checkweb.checkwebtime()
        print ("["+checkwebtime+"] "+yellow+"[+"+status_code+"] "+reset+yellow+
        		cw+reset+" "+url+ " "+blue+"["+title+"]"+reset)
        ccms = check.rule(header,body,title,icon_hash)
        checkcmstime = check.checkcmstime()
        print ("["+checkcmstime+"] "+white+"[FP]: "+reset+red+ccms+reset+"\n")

def create_arg_parser():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-u", "--url", help="Add a URL")
    parser.add_argument("-f", "--file", help="Add a document path")
    return parser