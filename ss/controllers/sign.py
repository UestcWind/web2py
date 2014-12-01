# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from sign.py")

def sign():
	import time
	today=time.strftime("%Y-%m-%d", time.localtime())
	if request.vars.status_wu:
		return dict(time=today,result=request.vars)
	else:
		return dict(time=today)

def commit():
	rows = db(db.signin.today==request.vars.time).select()
	if rows:
		return '今天的签到情况已经提交过了'
	else:
		try:
			if request.vars.status_wu=='1':
				db.signin.insert(name=request.vars.wu,isComing=request.vars.status_wu,comingTime='',today=request.vars.time,absentReason='有事')
			else:
				db.signin.insert(name=request.vars.wu,isComing=request.vars.status_wu,comingTime='9:00:00',today=request.vars.time,absentReason='')
			if request.vars.status_luo=='1':
				db.signin.insert(name=request.vars.luo,isComing=request.vars.status_luo,comingTime='',today=request.vars.time,absentReason='有事')
			else:
				db.signin.insert(name=request.vars.luo,isComing=request.vars.status_luo,comingTime='9:00:00',today=request.vars.time,absentReason='')
			if request.vars.status_liu=='1':
				db.signin.insert(name=request.vars.liu,isComing=request.vars.status_liu,comingTime='',today=request.vars.time,absentReason='有事')
			else:
				db.signin.insert(name=request.vars.liu,isComing=request.vars.status_liu,comingTime='9:00:00',today=request.vars.time,absentReason='')
			if request.vars.status_yao=='1':
				db.signin.insert(name=request.vars.yao,isComing=request.vars.status_yao,comingTime='',today=request.vars.time,absentReason='有事')
			else:
				db.signin.insert(name=request.vars.yao,isComing=request.vars.status_yao,comingTime='9:00:00',today=request.vars.time,absentReason='')
			if request.vars.status_long1=='1':
				db.signin.insert(name=request.vars.long,isComing=request.vars.status_long1,comingTime='',today=request.vars.time,absentReason='有事')
			else:
				db.signin.insert(name=request.vars.long,isComing=request.vars.status_long1,comingTime='9:00:00',today=request.vars.time,absentReason='')
			if request.vars.status_xue=='1':
				db.signin.insert(name=request.vars.xue,isComing=request.vars.status_xue,comingTime='',today=request.vars.time,absentReason='有事')
			else:
				db.signin.insert(name=request.vars.xue,isComing=request.vars.status_xue,comingTime='9:00:00',today=request.vars.time,absentReason='')
			return '记录成功'	
		except:				
			return '记录失败'	
def show():
				
def ajax():
	return dict(message="hello from sign.py")
#def commit_sign():
