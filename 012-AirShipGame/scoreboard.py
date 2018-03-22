import pygame.font

class Scoreboard():
    def __init__(self,setting,screen,status):
        self.screen = screen
        self.setting = setting
        self.status = status
        self.screen_rect = screen.get_rect()

        #设置显示积分的颜色和字体
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #准备初始得分
        self.prep_score()

    def prep_score(self):
        """将得分转化为图片"""
        round_score = int(round(self.status.score,-1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str,True,self.text_color)

        #绘制分数
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)