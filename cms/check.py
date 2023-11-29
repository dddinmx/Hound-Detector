#coding:utf-8

import json,datetime

def rule(header, body, title, icon_hash):

    with open('./cms/finger.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    
    count = 0
    for obj in data['fingerprint']:
        if 'method' in obj:
            count += 1
    
    hits = []
    for id in range(0, count):
        fingerprint = data["fingerprint"][id]
        cms = fingerprint["cms"]
        method = fingerprint["method"]
        location = fingerprint["location"]
        keyword = fingerprint["keyword"]
        starttime = datetime.datetime.now().strftime('%H:%M:%S')

        if method == 'keyword' and location == 'body':
            if "," in str(keyword):
                if all(name in body for name in keyword):
                     hits.append(cms)
            else:
                if str(keyword[0]) in body:
                     hits.append(cms)
        elif method == 'keyword' and location == 'title':
             if str(keyword[0]) == str(title):
                  hits.append(cms)
        elif method == 'icon_hash' and location == 'body':
             if str(keyword[0]) == str(icon_hash):
                  hits.append(cms)
        elif method == "keyword" and location == "header":
             if "," in str(keyword):
                  if any(name in header for name in keyword):
                       hits.append(cms)
             elif str(keyword[0]) in str(header):
                hits.append(cms)
    b=(f"{', '.join(hits)}")
    #bb = list(set(str(b).split(", ")))  
    return str(b)

def checkcmstime():
     time = datetime.datetime.now().strftime('%H:%M:%S')
     return time
