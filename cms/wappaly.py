#coding:utf-8

import datetime,sys,,warnings
from Wappalyzer import Wappalyzer, WebPage

red =  "\033[1;31m"
reset = "\033[0;0m"

def wappaly(url):
    warnings.simplefilter("ignore")
    try:
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)
        apps = wappalyzer.analyze(webpage)
        if apps:
            hits = []
            for app in apps:
                hits.append(app)
            b=(f"{', '.join(hits)}")
            return b
        else:
            b = "-"
            return b
    except Exception as e:
        #print ("["+checkwallytime()+"] "+red+"[+]"+reset+" Timeout.."+"\n")
        return "-"
    

def checkwallytime():
     time = datetime.datetime.now().strftime('%H:%M:%S')
     return time
