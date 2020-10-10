
class Bullet():
    _instances = []
    ''' Bullet class should have only 1 instance '''
    def __init__(self,Img):
        self.Img = Img
        self.bullet_state = False
        if len(self._instances) == 0:
            self._instances.append(self)
        else:
            raise Exception("This class is Singleton")

    def fire(self,screen,x,y):
        self.bullet_state = True
        screen.blit(self.Img , (x+16,y+16))

    def display(self,screen,x,y):
        return screen.blit(self.Img , (x,y))

        


