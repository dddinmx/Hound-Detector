#coding:utf-8

import os,sqlite3,re,datetime

path = os.path.dirname(os.path.abspath(__file__))
rtitle = re.compile(r'title="(.*)"')
rheader = re.compile(r'header="(.*)"')
rbody = re.compile(r'body="(.*)"')
rbracket = re.compile(r'\((.*)\)')

def count():
	with sqlite3.connect(path + '/web.db') as conn:
		cursor = conn.cursor()
		result = cursor.execute('SELECT COUNT(id) FROM `fofa`')
		for row in result:
			return row[0]
		
def check(num):
	with sqlite3.connect(path +'/web.db') as conn:
		cursor = conn.cursor()
		result = cursor.execute('SELECT name, keys FROM `fofa` WHERE id=\'{}\''.format(num))
		for row in result:
			return row[0], row[1]

def check_rule(key, header, body, title):
	try:
		if 'title="' in key:
			if re.findall(rtitle, key)[0].lower() in title.lower():
				return True
		elif 'body="' in key:
			if re.findall(rbody, key)[0] in body:
				return True
		else:
			if re.findall(rheader, key)[0] in header:
				return True
	except Exception as e:
		pass

def Compared(header, body, title):
	hits = []
	for id in range(1, int(count())):
		if id != 1365:
			name, key = check(id)
			#print (name + " " + key)
			#满足一个条件即可的情况
			if '||' in key and '&&' not in key and '(' not in key:
				for rule in key.split('||'):
					if check_rule(rule, header, body, title):
						hits.append(name)
						break
			#只有一个条件的情况
			elif '||' not in key and '&&' not in key and '(' not in key:
				if check_rule(key, header, body, title):
					hits.append(name)
			#需要同时满足条件的情况
			elif '&&' in key and '||' not in key and '(' not in key:
				num = 0
				for rule in key.split('&&'):
					if check_rule(rule, header, body, title):
						num += 1
				if num == len(key.split('&&')):
					hits.append(name)
			else:
				match = re.findall(rbracket, key)
				if match:
					if '&&' in re.findall(rbracket, key)[0]:
						for rule in key.split('||'):
							if '&&' in rule:
								num = 0
								for _rule in rule.split('&&'):
									if check_rule(_rule, header, body, title):
										num += 1
								if num == len(rule.split('&&')):
									hits.append(name)
									break
							else:
								if check_rule(rule, header, body, title):
									hits.append(name)
									break
					else:
				    	#并条件下存在与条件： 1&&2&&(3||4)
						for rule in key.split('&&'):
							num = 0
							if '||' in rule:
								for _rule in rule.split('||'):
									if check_rule(_rule, title, body, header):
										num += 1
										break
							else:
								if check_rule(rule, title, body, header):
									num += 1
						if num == len(key.split('&&')):
							hits.append(name)
		elif id == 1365:
			pass
	b=(f"[{', '.join(hits)}]")
	if b:
		return str(b)
	else:
		return "-"

def checkwebtime():
     time = datetime.datetime.now().strftime('%H:%M:%S')
     return time