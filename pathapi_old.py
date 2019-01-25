#coding:utf8
import os

def Projects():
	root="/project"
	if not os.path.exists(root):
		return [], "There is no project."
	projects=[]
	for p in os.listdir(root):
		if p.startwith("."):
			continue
		if os.path.isfile(root+"/"+p):
			continue
		projects.append(p)
	return projects, None

if __name__=="__main__":
	plist, err = Projects()
	if err:
		print err
	print Projects()

#Python can have two... return value
#if error occurs, second value will be checked and then it will be printed.
