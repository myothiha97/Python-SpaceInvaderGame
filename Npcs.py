class Npc:
    def __init__(self, playerImg):
        self.playerImg = playerImg

    def play(self,screen,x,y):
        return screen.blit(self.playerImg,(x,y))
    