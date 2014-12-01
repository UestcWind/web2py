# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from sign.py")

def sign():
	import time
	today=time.strftime("%Y-%m-%d", time.localtime())
	if request.vars.status_wu:
		return dict(time=today,result=request.vars.status_wu)
	else:
		return dict(time=today)

def commit():
	rows = db(db.signin.today==request.vars.time).select()
	if rows:
		return '今天的签到情况已经提交过了'
	else:
		try:
			if request.vars.status_wu=='1':
				db.signin.insert(name=request.vars.wu,isComing=request.vars.status_wu,comingTime='',today=request.vars.time,absentReason=request.vars.abs_wu)
			else:
				db.signin.insert(name=request.vars.wu,isComing=request.vars.status_wu,comingTime=request.vars.time_wu,today=request.vars.time,absentReason='')
			if request.vars.status_luo=='1':
				db.signin.insert(name=request.vars.luo,isComing=request.vars.status_luo,comingTime='',today=request.vars.time,absentReason=request.vars.abs_luo)
			else:
				db.signin.insert(name=request.vars.luo,isComing=request.vars.status_luo,comingTime=request.vars.time_luo,today=request.vars.time,absentReason='')
			if request.vars.status_liu=='1':
				db.signin.insert(name=request.vars.liu,isComing=request.vars.status_liu,comingTime='',today=request.vars.time,absentReason=request.vars.abs_liu)
			else:
				db.signin.insert(name=request.vars.liu,isComing=request.vars.status_liu,comingTime=request.vars.time_liu,today=request.vars.time,absentReason='')
			if request.vars.status_yao=='1':
				db.signin.insert(name=request.vars.yao,isComing=request.vars.status_yao,comingTime='',today=request.vars.time,absentReason=request.vars.abs_yao)
			else:
				db.signin.insert(name=request.vars.yao,isComing=request.vars.status_yao,comingTime=request.vars.time_yao,today=request.vars.time,absentReason='')
			if request.vars.status_long1=='1':
				db.signin.insert(name=request.vars.long,isComing=request.vars.status_long1,comingTime='',today=request.vars.time,absentReason=request.vars.abs_long)
			else:
				db.signin.insert(name=request.vars.long,isComing=request.vars.status_long1,comingTime=request.vars.time_long,today=request.vars.time,absentReason='')
			if request.vars.status_xue=='1':
				db.signin.insert(name=request.vars.xue,isComing=request.vars.status_xue,comingTime='',today=request.vars.time,absentReason=request.vars.abs_xue)
			else:
				db.signin.insert(name=request.vars.xue,isComing=request.vars.status_xue,comingTime=request.vars.time_xue,today=request.vars.time,absentReason='')
			return '记录成功'	
		except:				
			return '记录失败'		
def show():
	today=request.vars.time
	rows = db(db.signin.today==request.vars.time).select()
	str1=dict()
	str2='<table border="1" width="500" height="400"><tr><td>成员名</td><td>到了吗</td><td>到达时间</td><td>缺席原因</td</tr>'
	i=0
	for row in rows:
		str2
		str1[i]['name']=row.name
		if row.isComing=='0':
			str1[i]['isComing']='来了'
		else:
			str1[i]['isComing']='来了'
		str1[i]['name']=row.name
		str1[i]['name']=row.name
		str1[i]['name']=row.name
		str1[i]['name']=row.name
		str1[i]['name']=row.name
    	print row.myfield

	return dict(message=rows[0].name)			
def ajax():
	return dict(message="hello from sign.py")
#def commit_sign():
