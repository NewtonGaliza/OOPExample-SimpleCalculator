class calc(object):
	
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def sum(self):
		return self.a + self.b

	def sub(self):
		return self.a - self.b

	def mult(self):
		return self.a * self.b

	def div(self):
		return self.a / self.b

c = calc(128,2)

print ('Sum:', c.sum())

'''
redefine values
c.a = 3
c.b = 2
'''
