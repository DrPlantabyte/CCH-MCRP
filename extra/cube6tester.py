
def main():
	cube_list = []
	
	cube_list.append(Cube())
	for x in range (0,4):
		for y in range (0,4):
			cube2 = Cube()
			cube2.rotate_x(x)
			cube2.rotate_y(y)
			is_new = True
			for cube1 in cube_list:
				is_new = is_new and Cube.isUnique(cube1, cube2)
			if(is_new):
				cube_list.append(cube2)
	for cube1 in cube_list:
		cube1.printToTerminal()

class Cube:
	top = 1
	left = 2
	front = 3
	right = 4
	back = 5
	bottom = 6
	
	x_rot = 0
	y_rot = 0
	
	def printToTerminal(self):
		print('{ "model": "XXX", "x": ',self.x_rot,', "y": ',self.y_rot,' }')
	
	def __init__(self):
		pass
	
	def _rotate_y(self):
		temp = self.front
		self.front = self.left
		self.left = self.back
		self.back = self.right
		self.right = temp
		self.y_rot += 90
		while(self.y_rot >= 360):
			self.y_rot -= 360
	
	def _rotate_x(self):
		temp = self.top
		self.top = self.front
		self.front = self.bottom
		self.bottom = self.back
		self.back = temp
		self.x_rot += 90
		while(self.x_rot >= 360):
			self.x_rot -= 360
	
	def rotate_y(self, n):
		n2 = n
		while n2 < 0:
			n2 += 4
		for i in range(0,n2):
			self._rotate_y()
	
	def rotate_x(self, n):
		n2 = n
		while n2 < 0:
			n2 += 4
		for i in range(0,n2):
			self._rotate_x()
	
	def isEqual(cube1, cube2):
		return (cube1.top == cube2.top and cube1.front == cube2.front and cube1.left == cube2.left and cube1.right == cube2.right and cube1.back == cube2.back and cube1.bottom == cube2.bottom)
		
	def isUnique(cube1, cube2):
		return (cube1.top != cube2.top and cube1.front != cube2.front and cube1.left != cube2.left and cube1.right != cube2.right and cube1.back != cube2.back and cube1.bottom != cube2.bottom)
	
main()
			