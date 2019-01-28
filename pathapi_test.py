#!/usr/bin/env python
#coding:utf8
import unittest
from pathapi import *

class Test_path(unittest.TestCase):
	def test_project(self):
		self.assertEqual(project("/project/circle"), ("circle", None))
		self.assertEqual(project("/project/circle/"), ("circle", None))
		self.assertEqual(project("\\\\10.20.30.40\\project\\circle\\"), ("circle", None))
		self.assertEqual(project("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("circle", None))
		
	def test_seq(self):
		self.assertEqual(seq("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("FOO", None))
		
	def test_shot(self):
		self.assertEqual(shot("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("0010", None))
		self.assertEqual(shot("/project/circle/shot/FOO/C0010/comp"), ("C0010", None))

	def test_task(self):
		self.assertEqual(task("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("comp", None))
		
	def test_version(self):
		self.assertEqual(version("FOO_0010_comp_v001.nk"), (001, None))
	
	def test_seqNum(self):
		self.assertEqual(seqNum("FOO_0010_comp_v001.1001.exr"), (1001, None))

if __name__=="__main__":
	unittest.main()
