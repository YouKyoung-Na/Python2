import keyboard
import pygame
pygame.init()

#게임방법 설명 창 만들기
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("lever3: 단축키 연습 게임 설명")
how_lv3 = pygame.image.load("lv3 설명서.jpg")
how_lv3 = pygame.transform.scale(how_lv3, (800,600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #게임 닫기 버튼 클릭시 종료
         running = False
    #배경화면삽입
    screen.blit(how_lv3, (0, 0))
    pygame.display.update()
pygame.quit()
print("level 3 시작")

#화면설정
screen = pygame.display.set_mode((800,600))#크기
pygame.display.set_caption("lever3: 단축키연습")#타이틀
lv3_img = pygame.image.load("소웨경 단축키.jpg")#배경사진
lv3_img = pygame.transform.scale(lv3_img, (800,600))

#fps
clock = pygame.time.Clock()

#캐릭터 이동클래스 만들기
class MOVE:
    def __init__(self, to_x, to_y):
        self.to_x = to_x
        self.to_y = to_y

    def left_or_right(self, to_x):
        return self.to_x
    def down(self, to_y):
        return self.to_y

#캐릭터 불러오기
character = pygame.image.load("sprite01.png")
to_x = 0  # 캐릭터 이동 좌표
to_y = 0
character_x_pos = 650 + to_x  #캐릭터 좌표
character_y_pos = 60 + to_y

#이벤트 루프
running = True
while running:
    for event in pygame.event.get(): #사용자의 움직임 받음
        if event.type == pygame.QUIT: #게임 닫기 버튼 클릭시 종료
            running = False
            pygame.quit()
    #배경화면,캐릭터 삽입
    screen.blit(lv3_img, (0, 0))
    screen.blit(character,(character_x_pos, character_y_pos))
    pygame.display.update()
        #키이벤트 만들기
    for event in pygame.event.get():
        character = None
        key = keyboard.read_key()
        if key == "ctrl" and "z":
            character = MOVE(-190,0)


    clock.tick(60)
#게임종료
pygame.quit()
print("level 3 종료")