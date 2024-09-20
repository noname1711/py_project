import pygame, sys, random, math
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
FPS = 60
SIZE = 5 # Kích thước viên đạn nổ ra
SPEED_CHANGE_SIZE = 0.05 # Tốc độ nhỏ lại của viên đạn khi nổ ra
CHANGE_SPEED = 0.07 # Tốc độ chậm lại của viên đạn
RAD = math.pi/180 # Đổi từ radian sang độ
A_FALL = 1.5 # Gia tốc rơi tự do
NUM_BULLET = 50 # Số đạn nổ ra trong 1 quả pháo
SPEED_MIN = 2 # Tốc độ nhỏ nhất của 1 viên đạn
SPEED_MAX = 4 # Tốc độ lớn nhất của một viên đạn
TIME_CREATE_FW = 40 # Khoảng thời gian liên tiếp giữa 2 lần bắn
NUM_FIREWORKS_MAX = 3 # Số lượng pháo lớn nhất bắn lên 
NUM_FIREWORKS_MIN = 1 # Số lượng pháo nhỏ nhất bắn lên
SPEED_FLY_UP_MAX = 12 # Tốc độ lớn nhất của viên đạn bay lên (trước khi nổ)
SPEED_FLY_UP_MIN = 8 # Tốc độ nhỏ nhất của viên đạn bay lên (trước khi nổ)

BANNER = pygame.image.load('./hpnw.png')
BANNER = pygame.transform.scale(BANNER, (WINDOWWIDTH, 150))
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

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
		self.color = (255, 255, 255)
	def update(self):
		self.dots.append(Dot(self.x, self.y, self.size, self.color)) # Mỗi lần đạn đi qua sẽ có một chấm thêm vào
		# Xác định lại vị trí viên đạn
		self.y -= self.speed
		self.speed -= A_FALL*0.1
		# update từng chấm
		for dot in self.dots:
			dot.update()
		# Xoá những chấm có kích thước <= 0
		for dot in self.dots:
			if dot.size <= 0:
				self.dots.pop(self.dots.index(dot))
	def draw(self):
		pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size)) # Vẽ viên đạn
		# Vẽ từng chấm
		for dot in self.dots:
			dot.draw()
		
class Bullet(): # Viên đạn sau khi nổ
	def __init__(self, x, y, speed, angle, color):
		self.x = x
		self.y = y
		self.speed = speed
		self.angle = angle # Góc hợp bởi viên đạn và phương ngang
		self.size = SIZE
		self.color = color
		self.fire_sound = pygame.mixer.Sound('fw_04.mp3')
		self.fire_sound.set_volume(0.2)
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
			self.fire_sound.play()
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
		for bullet in self.bullets: # update từng viên đạn
			bullet.update()
			self.dots.append(Dot(bullet.x, bullet.y, bullet.size, bullet.color))
		for dot in self.dots: # update từng chấm
			dot.update()
		# Xoá những chấm có kích thước <= 0
		for dot in self.dots:
			if dot.size <= 0:
				self.dots.pop(self.dots.index(dot))
	def draw(self):
		for bullet in self.bullets: # Vẽ từng viên đạn
			bullet.draw()
		for dot in self.dots: # Vẽ từng chấm
			dot.draw()

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
	pygame.display.set_caption('FIREWORKS')
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	fireWorks = []
	time = TIME_CREATE_FW
	bulletFlyUps = []
	DISPLAYSURF.fill((0, 0, 0))
	font = pygame.font.SysFont('consolas', 30)  # Chọn font và size chữ
	textSurface = font.render('Happy New Year!', True, RED)
	textSize = textSurface.get_size()
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
		if time == TIME_CREATE_FW: # Tạo (những) viên đạn bay lên sau khoảng thời gian xác đinh
			for i in range(Random.num_fireworks()):
				bulletFlyUps.append(BulletFlyUp(Random.randomBulletFlyUp_speed(), Random.randomBulletFlyUp_x()))

		DISPLAYSURF.fill((0, 0, 0))

		DISPLAYSURF.blit(textSurface, textSurface.get_rect(center = DISPLAYSURF.get_rect().center))

		DISPLAYSURF.blit(BANNER, (0, 0))

		DISPLAYSURF.blit(BANNER, (0, WINDOWHEIGHT-150))

		for bulletFlyUp in bulletFlyUps: 
			bulletFlyUp.draw()
			bulletFlyUp.update()

		for fireWork in fireWorks:
			fireWork.draw()
			fireWork.update()

		for bulletFlyUp in bulletFlyUps:
			if bulletFlyUp.speed <= 0: # Viên đạn bay lên đạt độ cao tối đa
				fireWorks.append(FireWork(bulletFlyUp.x, bulletFlyUp.y)) # Tạo quả pháo ngay vị trí viên đạn
				bulletFlyUps.pop(bulletFlyUps.index(bulletFlyUp)) # Xoá viên đạn đó
		
		# Xoá quả pháo hoa khi kích thước những viên đạn <= 0
		for fireWork in fireWorks:
			if fireWork.bullets[0].size <= 0:
				fireWorks.pop(fireWorks.index(fireWork))

		# Đếm khoảng thời gian bắn
		if time <= TIME_CREATE_FW:
			time += 1
		else:
			time = 0

		pygame.display.update()
		FPSCLOCK.tick(FPS)

if __name__ == '__main__':
	main()
