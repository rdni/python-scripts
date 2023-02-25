import pygame

"""Basic pong game, with a player, enemy, and ball."""

class Player(object):
    def __init__(self):
        self.position = 50
        self.score = 0
        self.size = 50
        self.speed = 5
    
    def move(self, direction):
        if direction == "up":
            self.position -= self.speed
        elif direction == "down":
            self.position += self.speed
        elif direction == "logical":
            # For tesing only
            if self.position <= 150:
                self.position += self.speed
            elif self.position >= 150:
                self.position -= self.speed
            else:
                self.position += self.speed
        else:
            raise NotImplementedError
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (0, self.position, self.size / 5, self.size))
    
class Enemy(object):
    def __init__(self):
        self.position = 50
        self.score = 0
        self.size = 10
        self.speed = 5
    
    def move(self, direction):
        if direction == "up":
            self.position -= self.speed
        elif direction == "down":
            self.position += self.speed
        elif direction == "logical":
            if self.position < 150:
                self.position += self.speed
            elif self.position > 150:
                self.position -= self.speed
        else:
            raise NotImplementedError
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (290, self.position, self.size, self.size))
        
class Ball(object):
    def __init__(self):
        self.position = [150, 150]
        self.size = 10
        self.speed = [5, 5]
    
    def move(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        if self.position[0] < 0:
            self.speed[0] = -self.speed[0]
        elif self.position[0] > 290:
            self.speed[0] = -self.speed[0]
        if self.position[1] < 0:
            self.speed[1] = -self.speed[1]
        elif self.position[1] > 290:
            self.speed[1] = -self.speed[1]
        
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.position[0], self.position[1], self.size, self.size))

class GameState(object):
    def __init__(self) -> None:
        self.player = None
        self.enemy = None
        self.ball = None
        self.screen = None
        self.clock = None
        self.running = False
        self.fps = 60
        self.size = self.width, self.height = 300, 300
        
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.enemy = Enemy()
        self.ball = Ball()
        
    def update(self):
        self.player.move("logical")
        self.enemy.move("logical")
        self.ball.move()
        
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        self.ball.draw(self.screen)
        
    def clear(self):
        self.screen.fill((0, 0, 0))
    
    def run(self):
        self.init()
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    exit()
            self.clear()
            self.update()
            pygame.display.flip()
            self.clock.tick(self.fps)
            
if __name__ == "__main__":
    game = GameState()
    game.run()