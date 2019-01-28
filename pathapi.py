#!/usr/bin/env python
#coding:utf8
import re

path="/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"

def project(path):
	"""
	경로를 넣으면 프로젝트 이름을 반환.
	"""
	#p=re.findall("/project/(\S[^/]+)", path.replace("\\", "/"))
	p=re.findall("/project/(\w+)", path.replace("\\", "/"))
	if len(p) != 1:
		return "", "project 정보를 경로에서 가지고 올 수 없음."
	return p[0], None

def seq(path):
	"""
	경로를 넣으면 시퀀스 이름을 반환.
	"""
	p = re.findall("/shot/(\S[^/]+)", path.replace("\\", "/"))
	if len(p)!=1:
		return "", "seq 정보를 경로에서 가지고 올 수 없음."
	return p[0], None

def shot(path):
	"""
	경로를 넣으면 샷 이름을 반환.
	"""
	p=re.findall("/FOO/(\w+)", path.replace("\\", "/"))
	if len(p)!=1:
		return "", "shot 정보를 경로에서 가지고 올 수 없음."
	return p[0], None

def task(path):
	"""
	경로를 넣으면 태스크를 반환.
	"""
	p=re.findall("/\d+/(\S[^/]+)", path.replace("\\", "/"))
	if len(p)!=1:
		return "", "task 정보를 경로에서 가지고 올 수 없음."
	return p[0], None

def version(path):
	"""
	경로를 넣으면 버전 정보가 반환.
	"""
	p = re.findall("_v(\d+)", path.replace("\\", "/"))
	if len(p)!=1:
		return -1, "version 정보를 경로에서 가지고 올 수 없음."
	return int(p[0]), None

#this path must be f="FOO_0010_comp_v001.1001.exr"
def seqNum(path):
	"""
	경로를 넣으면 시퀀스 넘버가 반환
	
	"""
	p = re.findall("\.(\d+)\.", path.replace("\\", "/"))
	if len(p)!=1:
		return -1, "sequence number를 경로에서 가지고 올 수 없음."
	return int(p[0]), None


#print help(seqNum)

"""
#이제 이걸 테스트코드에서 확인을 하고있기 때문에 작성할 필요 없음..
if __name__=="__main__":
	projectName, err =  project(path)
	if err:
		print err
	print projectName

	projectName, err= seq(path)
i	if err:
		print err
	print projectName
"""
