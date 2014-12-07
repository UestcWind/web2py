# -*- coding: utf-8 -*-
# try something like
def index(): 
	#member_count=db.member_.id.count()
	member_count=db(db.member_.id>0).count()
	if member_count==0:
		return dict(warning="还没有添加任何公司成员")
	#records=SQLTABLE(db().select(db.member_.ALL),columns=['name'])
	records=db().select(db.member_.ALL)
	return	dict(records=records) 

def create():
	form = SQLFORM(db.member_).process()
	if form.accepted:
		response.flash = '添加成功'
	return dict(form=form)	

def edit():
	#response.view='member/create.html'
	record = db.member_(request.args(0)) or redirect(URL('member','index'))
	url = URL('download')
	form = SQLFORM(db.member_, record, deletable=True,
					upload=url, fields=['name', 'avatar'],showid=False,
					labels={'name':'姓名','avatar':'头像'},readonly=False)
	if form.process().accepted:
		response.flash = '修改成功'
	elif form.errors:
		response.flash = '修改出错！'
	return dict(form=form)			

def download():
    return response.download(request,db)    