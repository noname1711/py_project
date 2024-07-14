import pygame, sys, random, math
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
FPS = 60
SIZE = 4.5 # Kích thước viên đạn nổ ra
SPEED_CHANGE_SIZE = 0.05 # Tốc độ nhỏ lại của viên đạn khi nổ ra
CHANGE_SPEED = 0.07 # Tốc độ chậm lại của viên đạn
RAD = math.pi/180 # Đỏi từ radian sang độ
A_FALL = 1.5 # Gia tốc rơi tự do
NUM_BULLET = 50 # Số đạn nổ ra trong 1 quả pháo
SPEED_MIN = 2 # Tốc độ nhỏ nhất của 1 viên đạn
SPEED_MAX = 4 # Tốc độ lớn nhất của một viên đạn
TIME_CREAT_FW = 40 # Khoảng thời gian liên tiếp giữa 2 lần bắn
NUM_FIREWORKS_MAX = 3 # Số lượng pháo lớn nhất bắn lên 
NUM_FIREWORKS_MIN = 1 # Số lượng pháo nhỏ nhất bắn lên
SPEED_FLY_UP_MAX = 12 # Tốc độ lớn nhất của viên đạn bay lên (trước khi nổ)
SPEED_FLY_UP_MIN = 8 # Tốc độ nhỏ nhất của viên đạn bay lên (trước khi nổ)

class Dot(): # Những chấm theo sau của mỗi viên đạn
	def __init__(self, x, y, size, color):
		self.x = x 
		self.y = y
		self.size = size
		self.color = color
	def update(self):
		# Giảm kích thước chấm
		if self.size > 0:
			self.size -= SPEED_CHANGE_SIZE*5
		else:
			self.size = 0
	def draw(self): # Vẽ một chấm
		if self.size > 0:
			pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))

class BulletFlyUp(): # Viên đạn bay lên trước khi nổ
	def __init__(self, speed, x):
		self.speed = speed
		self.x = x
		self.y = WINDOWHEIGHT
		self.dots = [] # Một list các chấm theo sau
		self.size = SIZE/2
		self.color = (255, 255, 100)

	def update(self):
		self.dots.append(Dot(self.x, self.y, self.size, self.color)) # Mỗi lần đạn đi qua sẽ có một chấm thêm vào
		# Xác định lại vị trí viên đạn
		self.y -= self.speed
		self.speed -= A_FALL*0.1
		# update từng chấm
		for i in range(len(self.dots)):
			self.dots[i].update()
		# Xoá những chấm có kích thước <= 0
		i = 0
		while i < len(self.dots):
			if self.dots[i].size <= 0:
				self.dots.pop(i)
			else:
				i += 1

	def draw(self):
		pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size)) # Vẽ viên đạn
		# Vẽ từng chấm
		for i in range(len(self.dots)):
			self.dots[i].draw()

class Bullet(): # Viên đạn sau khi nổ
	def __init__(self, x, y, speed, angle, color):
		self.x = x
		self.y = y
		self.speed = speed
		self.angle = angle # Góc hợp bởi viên đạn và phương ngang
		self.size = SIZE
		self.color = color

	def update(self):
		# Xác định tốc độ theo 2 phương
		speedX = self.speed * math.cos(self.angle*RAD) 
		speedY = self.speed * -math.sin(self.angle*RAD)
		# Xác định lại vị trí viên đạn
		self.x += speedX
		self.y += speedY
		self.y += A_FALL
		# Giảm tốc độ đạn
		if self.size > 0:
			self.size -= SPEED_CHANGE_SIZE
		else:
			self.size = 0
		# Giảm kích thước đạn
		if self.speed > 0:
			self.speed -= CHANGE_SPEED
		else:
			self.speed = 0

	def draw(self): # Vẽ 1 viên đạn
		if self.size > 0:
			pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))

class FireWork(): # Quả pháo hoa
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dots = [] # List các chấm theo sau mỗi viên đạn

		def creatBullets(): # Tạo list các viên đạn
			bullets = []
			color = Random.color()
			for i in range(NUM_BULLET):
				angle =  (360/NUM_BULLET)*i
				speed = random.uniform(SPEED_MIN, SPEED_MAX)
				bullets.append(Bullet(self.x, self.y, speed, angle, color))
			return bullets
		self.bullets = creatBullets();

	def update(self):
		for i in range(len(self.bullets)): # update từng viên đạn
			self.bullets[i].update()
			self.dots.append(Dot(self.bullets[i].x, self.bullets[i].y, self.bullets[i].size, self.bullets[i].color))
		for i in range(len(self.dots)): # update từng chấm
			self.dots[i].update()
		# Xoá những chấm có kích thước <= 0
		i = 0
		while i < len(self.dots):
			if self.dots[i].size <= 0:
				self.dots.pop(i)
			else:
				i += 1
	def draw(self):
		for i in range(len(self.bullets)): # Vẽ từng viên đạn
			self.bullets[i].draw()
		for i in range(len(self.dots)): # Vẽ từng chấm
			self.dots[i].draw()

class Random():
	def __init__(self):
		pass
		
	def color(): # Tạo màu ngẫu nhiên (màu sáng)
		
		color1 = random.randint(0, 255)
		color2 = random.randint(0, 255)
		if color1 + color2 >= 255:
			color3 = random.randint(0, 255)
		else:
			color3 = random.randint(255 - color1 - color2, 255)
		colorList = [color1, color2, color3]
		random.shuffle(colorList)
		return colorList
	def num_fireworks(): # Số pháo mỗi lần bắn
		return random.randint(NUM_FIREWORKS_MIN, NUM_FIREWORKS_MAX)
	def randomBulletFlyUp_speed(): # Tốc độ viên đạn bay lên
		speed = random.uniform(SPEED_FLY_UP_MIN, SPEED_FLY_UP_MAX)
		return speed
	def randomBulletFlyUp_x(): # Vị trí viên đạn bay lên
		x = random.randint(int(WINDOWWIDTH*0.2), int(WINDOWHEIGHT*0.8))
		return x

def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	fireWorks = []
	time = TIME_CREAT_FW
	bulletFlyUps = []
	
	while True:
		DISPLAYSURF.fill((0, 0, 0)) # Xoá nền
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
		if time == TIME_CREAT_FW: # Tạo (những) viên đạn bay lên sau khoảng thời gian xác đinh
			for i in range(Random.num_fireworks()):
				bulletFlyUps.append(BulletFlyUp(Random.randomBulletFlyUp_speed(), Random.randomBulletFlyUp_x()))

		for i in range(len(bulletFlyUps)): 
			bulletFlyUps[i].draw()
			bulletFlyUps[i].update()

		for i in range(len(fireWorks)):
			fireWorks[i].draw()
			fireWorks[i].update()

		i = 0
		while i < len(bulletFlyUps):
			if bulletFlyUps[i].speed <= 0: # Viên đạn bay lên đạt độ cao tối đa
				fireWorks.append(FireWork(bulletFlyUps[i].x, bulletFlyUps[i].y)) # Tạo quả pháo ngay vị trí viên đạn
				bulletFlyUps.pop(i) # Xoá viên đạn đó
			else:
				i += 1
		# Xoá quả pháo hoa khi kích thước những viên đạn <= 0
		i = 0
		while i < len(fireWorks):
			if fireWorks[i].bullets[0].size <= 0:
				fireWorks.pop(i)
			else:
				i += 1

		# Đếm khoảng thời gian bắn
		if time <= TIME_CREAT_FW:
			time += 1
		else:
			time = 0
		pygame.display.update()
		FPSCLOCK.tick(FPS)

if __name__ == '__main__':
	main()