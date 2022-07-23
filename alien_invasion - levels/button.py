import pygame.font

class Button:

    def __init__(self, ai_game, pos_x, pos_y, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (162,228,184)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object.
        self.rect = pygame.Rect(pos_x, pos_y, self.width, self.height)

        # The button message only needs to be prepped once.
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)