# -*- coding: utf-8 -*-
import numpy as np

class Result(object):
	"""
	这个函数用于获取测试的数据，通过读取“test”中的
	"""
	def __init__(self, test):
		super(Result, self).__init__()
		self.test = test
		"""
		通过test 获取test文件夹中的所有图片[n*227*227*3]
		"""
		self.test_data

	def get_data(self):
		return self.test_data

	def get_result(self,pre):
		"""
		pre 为test中顺序的预测结果返回值是[50]的向量，
		因此 pre是[n*50]的一个二维数组，
		所以接下来要做的就是，把[50]的向量中最大的值所对应的数字取出来，按顺序放入result中
		"""
		result = [];
		"""
		假设我们已经得到了result，接下来
		我们将result生成一个CSV文件，保存
		"""
