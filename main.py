import random

# 1st game (tutorial)
"""
import pygame

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def getSurf(self):
        return self.surf

    def getRect(self):
        return self.rect

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.getRect().move_ip(0, -2)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.getRect().move_ip(0, 2)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.getRect().move_ip(-2, 0)
        if pressed_keys[K_RIGHT]:
            self.getRect().move_ip(2, 0)

        if self.getRect().left < 0:
            self.getRect().left = 0
        if self.getRect().right > SCREEN_WIDTH:
            self.getRect().right = SCREEN_WIDTH
        if self.getRect().top <= 0:
            self.getRect().top = 0
        if self.getRect().bottom >= SCREEN_HEIGHT:
            self.getRect().bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("images/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

        self.speed = random.randint(2, 5)

    def getSurf(self):
        return self.surf

    def getRect(self):
        return self.rect

    def getSpeed(self):
        return self.speed

    def update(self):
        self.getRect().move_ip(-self.getSpeed(), 0)
        if self.getRect().right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):

    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("images/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def getSurf(self):
        return self.surf

    def getRect(self):
        return self.rect

    def update(self):
        self.getRect().move_ip(-1,0)
        if self.getRect().right < 0:
            self.kill()

pygame.mixer.init()

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

player = Player()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

pygame.mixer.music.load("sounds/Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)

move_up_sound = pygame.mixer.Sound("sounds/Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("sounds/Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("sounds/Collision.ogg")

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()
    clouds.update()

    screen.fill((135, 206, 250))

    for entity in all_sprites:
        screen.blit(entity.getSurf(), entity.getRect())

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()

        pygame.time.wait(200)

        running = False

    pygame.display.flip()

    clock.tick(60)

pygame.mixer.music.stop()
pygame.mixer.quit()

pygame.quit()
"""

# 2nd game (Wordle ?)
import webbrowser
import time

game_lang = "EN"


def startWordle(len_word, lang):
    words = []

    if lang == 'EN':
        file = "words_alpha"
    elif lang == 'FR':
        file = "liste_francais"

    with open(f'txts/{file}.txt', 'r') as f:  # English words
        for line in f:
            for word in line.split():
                words.append(word)

    len_words = len(words)

    word_to_find = ''
    word_hidden = ''
    letters_in = 'None'
    letters_not_in = 'None'

    words_guessed = []

    while len(word_to_find) != len_word:
        word_to_find = words[random.randint(0, len_words - 1)]

    for i in range(len_word):
        if word_to_find[i] == "-":
            word_hidden += '-'
        else:
            word_hidden += "_"

    tries = 1
    found = False

    while not found:
        print('')
        # print(f"DEBUG MODE IS ON, THE WORD IS --> {word_to_find}")
        print(f"Your current mode : {lang}")
        print("Here is the list of every word you said :")
        for word_said in words_guessed:
            print(word_said, end="\n")
        print('')
        print(f"This is what you found : {word_hidden} ({len_word} characters long)")
        print(f"Letters you guessed and are in the word --> {letters_in}")
        print(f"Letters you guessed and are not in the word --> {letters_not_in}")
        guess = ''

        while len(guess) != len_word:
            guess = input("What do you think is the word ? : ")
            print('')
            if guess == "Give_up":
                print(f"You lose, the word was {word_to_find}...")

                time.sleep(2)

                boolQ = input("Do you want to play again ? (Y/N) ")

                if boolQ == "Y":
                    return startWordle(random.randint(3, 28), lang)
                break
            elif len(guess) != len_word:
                print(f"This word is not {len_word} letter long !")
                if len(guess) < len_word:
                    print(f"({len(guess)} < {len_word})")
                else:
                    print(f"({len_word} > {len(guess)})")
                guess = ''
            elif guess not in words:
                print("This not is not in the dictionary !")
                guess = ''
            else:
                words_guessed.append(guess)

        if guess == word_to_find:
            print(f"Congrats ! The word to find was {word_to_find} in {tries} tries")
            if lang == 'EN':
                webbrowser.open(f'https://theopendictionary.com/word/{word_to_find}')
            elif lang == 'FR':
                webbrowser.open(f"https://www.larousse.fr/dictionnaires/francais/{word_to_find}")
            time.sleep(2)

            boolQ = input("Do you want to play again ? (Y/N) ")

            if boolQ == "Y":
                return startWordle(random.randint(3, 28), lang)
            break

        for i in range(len_word):
            if guess[i] in word_to_find and guess[i] not in letters_in:
                if letters_in == 'None':
                    letters_in = ''
                    letters_in += guess[i]
                else:
                    letters_in += f", {guess[i]}"
            elif guess[i] not in letters_not_in and guess[i] not in letters_in:
                if letters_not_in == 'None':
                    letters_not_in = ''
                    letters_not_in += guess[i]
                else:
                    letters_not_in += f", {guess[i]}"
            if guess[i] == word_to_find[i]:
                list_word_hidden = list(word_hidden)
                list_word_hidden[i] = word_to_find[i]
                word_hidden = ''.join(list_word_hidden)

        tries += 1


startWordle(random.randint(3, 28), game_lang)
