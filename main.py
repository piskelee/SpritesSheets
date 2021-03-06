import sys
import pygame

TITLE = "SpriteSheets"
WIDTH = 1024
HEIGHT = 768
FPS = 60


def get_image(sheet, frame_x, frame_y, img_width, img_height, scale):
    img = pygame.Surface((img_width, img_height)).convert_alpha()
    img.blit(sheet, (0, 0), ((frame_x * img_width), (frame_y * img_height), img_width, img_height))
    img = pygame.transform.scale(img, (img_width * scale, img_height * scale))
    return img


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.cat_img = pygame.image.load("cat.png").convert_alpha()

        self.frame_0 = get_image(self.cat_img, 0, 1, 141, 141, 1)
        self.frame_1 = get_image(self.cat_img, 1, 1, 141, 141, 1)
        self.frame_2 = get_image(self.cat_img, 2, 1, 141, 141, 1)
        self.frame_3 = get_image(self.cat_img, 3, 1, 141, 141, 1)

    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill("black")

            # self.screen.blit(cat_img, (0, 0))
            self.screen.blit(self.frame_0, (0, 0))
            self.screen.blit(self.frame_1, (150, 0))
            self.screen.blit(self.frame_2, (300, 0))
            self.screen.blit(self.frame_3, (450, 0))

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.update()
