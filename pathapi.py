#!/usr/bin/env python
#coding:utf8
import re

path="/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"

def project(path):
	"""
	경로를 넣으면 프로젝트 이름을 반환.
	"""
	p=re.findall("/project/(\S[^/]+)", path.replace("\\", "/"))
	if len(p) != 1:
		return "", "project 정보를 경로에서 가지고 올 수 없음."
	return p[0], None

if __name__=="__main__":
	projectName, err =  project(path)
	if err:
		print err
	print projectName
