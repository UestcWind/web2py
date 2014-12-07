# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from sign.py")

def sign():
	import time
	today=time.strftime("%Y-%m-%d", time.localtime())
	rows = db(db.signin.today==today).select()
	if  rows:
		return dict(time=today,warning='今天的签到工作已经圆满完成~')
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
	return  dict(link='sign.html')
def show_():
	today=request.vars.today
	rows = db(db.signin.today==today).select()
	if not rows:
		return '<span style="font-size:20px;color:red">"'+today+'"'+'格式不正确,或者这天是周末神马的</span>'
	str2=('<table border="1" width="500" height="400"><tr ><td colspan="4"><span style="font-size:25px;font-weight:bold" >'
		+today+'的签到情况'
		+'</span></td></tr><tr><td style="font-size:20px;font-weight:bold">成员名</td><td style="font-size:20px;font-weight:bold">'
		'到了吗</td><td style="font-size:20px;font-weight:bold">到达时间</td><td style="font-size:20px;font-weight:bold">缺席原因</td</tr>')
	for row in rows:
		str2+='<tr>'
		str2+='<td>'+row.name+'</td>'
		if row.isComing=='0':
			str1='来了'
		else:
			str1='没来'
		str2+='<td>'+str1+'</td>'	
		str2+='<td>'+row.comingTime+'</td>'
		str2+='<td>'+row.absentReason+'</td></tr>'
	return 	str2	
def ajax():
	return dict(message="hello from sign.py")
#def commit_sign():
