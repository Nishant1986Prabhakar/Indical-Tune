import tkinter
import pygame
import button
import piano_lists as pl
import subprocess
from pygame import mixer

pygame.init()
pygame.mixer.set_num_channels(50)

font = pygame.font.Font('assets/Terserah.ttf', 48)
medium_font = pygame.font.Font('assets/Terserah.ttf', 28)
small_font = pygame.font.Font('assets/Terserah.ttf', 16)
real_small_font = pygame.font.Font('assets/Terserah.ttf', 10)
fps = 60
timer = pygame.time.Clock()
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []
key_note_played = []
buttons = []
left_oct = 4
right_oct = 5
Start_Button = False
Done_Button = False

left_hand = pl.left_hand
right_hand = pl.right_hand
piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels
key_notes = pl.key_notes

all_arohanam_raagas = pl.all_arohanam_raagas
list_of_arohanam_raagas = pl.list_of_arohanam_raagas
  
for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'/Users/n0p00qd/Desktop/Desktop Folder/Personal/Python/PythonPiano/assets/notes/{white_notes[i]}.wav'))

for i in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'/Users/n0p00qd/Desktop/Desktop Folder/Personal/Python/PythonPiano/assets/notes/{black_notes[i]}.wav'))

pygame.display.set_caption("Nishant's Python Piano")

play_raaga_img = pygame.image.load('assets/Play_Raaga.png').convert_alpha()
raaga_to_be_played_img = pygame.image.load('assets/Raaga_To_Be_Played.png').convert_alpha()
play_raaga_button = button.Button(900, 20, play_raaga_img, 0.8)
raaga_to_be_played_button = button.Button(900, 50, raaga_to_be_played_img, 0.8)
    
def draw_piano(whites, blacks):
    white_rects = []
    for i in range(52):
        rect = pygame.draw.rect(screen, 'white', [i * 35, HEIGHT - 300, 35, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i * 35, HEIGHT - 300, 35, 300], 2, 2)
        key_label = small_font.render(white_notes[i], True, 'black')
        screen.blit(key_label, (i * 35 + 3, HEIGHT - 20))
    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []
    for i in range(36):
        rect = pygame.draw.rect(screen, 'black', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 0, 2)
        for q in range(len(blacks)):
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, 'green', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 2, 2)
                    blacks[q][1] -= 1

        key_label = real_small_font.render(black_labels[i], True, 'white')
        screen.blit(key_label, (25 + (i * 35) + (skip_count * 35), HEIGHT - 120))
        black_rects.append(rect)
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'green', [j * 35, HEIGHT - 100, 35, 100], 2, 2)
            whites[i][1] -= 1

    return white_rects, black_rects, whites, blacks


def draw_hands(rightOct, leftOct, rightHand, leftHand):
    # left hand
    pygame.draw.rect(screen, 'dark gray', [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, 'black', [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 4, 4)
    text = small_font.render(leftHand[0], True, 'white')
    screen.blit(text, ((leftOct * 245) - 165, HEIGHT - 55))
    text = small_font.render(leftHand[2], True, 'white')
    screen.blit(text, ((leftOct * 245) - 130, HEIGHT - 55))
    text = small_font.render(leftHand[4], True, 'white')
    screen.blit(text, ((leftOct * 245) - 95, HEIGHT - 55))
    text = small_font.render(leftHand[5], True, 'white')
    screen.blit(text, ((leftOct * 245) - 60, HEIGHT - 55))
    text = small_font.render(leftHand[7], True, 'white')
    screen.blit(text, ((leftOct * 245) - 25, HEIGHT - 55))
    text = small_font.render(leftHand[9], True, 'white')
    screen.blit(text, ((leftOct * 245) + 10, HEIGHT - 55))
    text = small_font.render(leftHand[11], True, 'white')
    screen.blit(text, ((leftOct * 245) + 45, HEIGHT - 55))
    text = small_font.render(leftHand[1], True, 'black')
    screen.blit(text, ((leftOct * 245) - 148, HEIGHT - 55))
    text = small_font.render(leftHand[3], True, 'black')
    screen.blit(text, ((leftOct * 245) - 113, HEIGHT - 55))
    text = small_font.render(leftHand[6], True, 'black')
    screen.blit(text, ((leftOct * 245) - 43, HEIGHT - 55))
    text = small_font.render(leftHand[8], True, 'black')
    screen.blit(text, ((leftOct * 245) - 8, HEIGHT - 55))
    text = small_font.render(leftHand[10], True, 'black')
    screen.blit(text, ((leftOct * 245) + 27, HEIGHT - 55))
    # right hand
    pygame.draw.rect(screen, 'dark gray', [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, 'black', [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 4, 4)
    text = small_font.render(rightHand[0], True, 'white')
    screen.blit(text, ((rightOct * 245) - 165, HEIGHT - 55))
    text = small_font.render(rightHand[2], True, 'white')
    screen.blit(text, ((rightOct * 245) - 130, HEIGHT - 55))
    text = small_font.render(rightHand[4], True, 'white')
    screen.blit(text, ((rightOct * 245) - 95, HEIGHT - 55))
    text = small_font.render(rightHand[5], True, 'white')
    screen.blit(text, ((rightOct * 245) - 60, HEIGHT - 55))
    text = small_font.render(rightHand[7], True, 'white')
    screen.blit(text, ((rightOct * 245) - 25, HEIGHT - 55))
    text = small_font.render(rightHand[9], True, 'white')
    screen.blit(text, ((rightOct * 245) + 10, HEIGHT - 55))
    text = small_font.render(rightHand[11], True, 'white')
    screen.blit(text, ((rightOct * 245) + 45, HEIGHT - 55))
    text = small_font.render(rightHand[1], True, 'black')
    screen.blit(text, ((rightOct * 245) - 148, HEIGHT - 55))
    text = small_font.render(rightHand[3], True, 'black')
    screen.blit(text, ((rightOct * 245) - 113, HEIGHT - 55))
    text = small_font.render(rightHand[6], True, 'black')
    screen.blit(text, ((rightOct * 245) - 43, HEIGHT - 55))
    text = small_font.render(rightHand[8], True, 'black')
    screen.blit(text, ((rightOct * 245) - 8, HEIGHT - 55))
    text = small_font.render(rightHand[10], True, 'black')
    screen.blit(text, ((rightOct * 245) + 27, HEIGHT - 55))


def draw_title_bar():
    instruction_text = medium_font.render('Up/Down Arrows Change Left Hand', True, 'black')
    screen.blit(instruction_text, (WIDTH - 500, 10))
    instruction_text2 = medium_font.render('Left/Right Arrows Change Right Hand', True, 'black')
    screen.blit(instruction_text2, (WIDTH - 500, 50))
    img = pygame.transform.scale(pygame.image.load('assets/logo.png'), [150, 150])
    screen.blit(img, (-20, -30))
    title_text = font.render('Raaga Detector!', True, 'blue')
    screen.blit(title_text, (298, 18))
    title_text = font.render('Raaga Detector!', True, 'purple')
    screen.blit(title_text, (300, 20))
    #menu_text1 = small_font.render('Play The Raaga To Be Found', True, 'green')
    #screen.blit(menu_text1, (WIDTH - 800, 10))
    #menu_text2 = small_font.render('Ask For The Raaga To Be Played', True, 'yellow')
    #screen.blit(menu_text2, (WIDTH - 800, 50))

class Buttons:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
 
		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'
 
		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		#text
		self.text = text
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
		buttons.append(self)
 
	def change_text(self, newtext):
		self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
 
	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 
 
		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
 
		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		global Start_Button
		global Done_Button
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				self.change_text(f"{self.text}")
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					print('The Button Clicked is:', self.text)
					self.pressed = False
					self.change_text(self.text)
					if self.text == 'Start':
						Start_Button = True
					if self.text == 'Done':
						Done_Button = True                      
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'
   
gui_font = pygame.font.Font(None,30)

button1 = Buttons('Start',200,40,(670,8),5)
button2 = Buttons('Done',200,40,(670,58),5)
      
def buttons_draw():
	for b in buttons:
		b.draw()   

def find_arohanam_raag(key_note_played):
    try:
        found_raaga = ""
        length_arohanam_raag = 0
        played_arohanam_raaga = [None] * ((len(key_note_played)) -1)
        length_arohanam_raag = len(key_note_played)
        print("The size of array key_note_played is: ", length_arohanam_raag)
        for loop_count in range(0,length_arohanam_raag-1):
            played_arohanam_raaga[loop_count] = key_note_played[loop_count+1] - key_note_played[loop_count]        
        print("The Value of array played_arohanam_raaga is",played_arohanam_raaga)
        for match_count in range(0,len(all_arohanam_raagas)):
            print(played_arohanam_raaga,all_arohanam_raagas[match_count])
            if played_arohanam_raaga == list(all_arohanam_raagas[match_count]):
                print("The Raaga Played is :",list_of_arohanam_raagas[match_count])
                found_raaga = list_of_arohanam_raagas[match_count]
                break
        return found_raaga   
    except Exception as e:
        print(e)


run = True
while run:
    left_dict = {'Z': f'C{left_oct}',
                 'S': f'C#{left_oct}',
                 'X': f'D{left_oct}',
                 'D': f'D#{left_oct}',
                 'C': f'E{left_oct}',
                 'V': f'F{left_oct}',
                 'G': f'F#{left_oct}',
                 'B': f'G{left_oct}',
                 'H': f'G#{left_oct}',
                 'N': f'A{left_oct}',
                 'J': f'A#{left_oct}',
                 'M': f'B{left_oct}'}

    right_dict = {'R': f'C{right_oct}',
                  '5': f'C#{right_oct}',
                  'T': f'D{right_oct}',
                  '6': f'D#{right_oct}',
                  'Y': f'E{right_oct}',
                  'U': f'F{right_oct}',
                  '8': f'F#{right_oct}',
                  'I': f'G{right_oct}',
                  '9': f'G#{right_oct}',
                  'O': f'A{right_oct}',
                  '0': f'A#{right_oct}',
                  'P': f'B{right_oct}'}
    timer.tick(fps)
    screen.fill('gray')
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)

    if play_raaga_button.draw(screen):
        print('Clicked on Play The Raaga')
        applescript = """
        display dialog "Click On The Start Button And Play The Key Notes For Arohanam or Avarohanam And Click On Done...." ¬
        with title "This is a pop-up window" ¬
        with icon caution ¬
        buttons {"OK"}
        """

        subprocess.call("osascript -e '{}'".format(applescript), shell=True)
        
    if raaga_to_be_played_button.draw(screen):
        print('Clicked on The Raaga To Be Played')
        print('The values of all_arohanam_raagas is', all_arohanam_raagas)

    draw_hands(right_oct, left_oct, right_hand, left_hand)
    
    buttons_draw()
    
    # if button1 != False:
    #     print('Value of button1:', button1)
    #     print('Value of button2:', button2)
    
    draw_title_bar()
     
    # print('The Value of Start_Button is:',Start_Button)
    # print('The Value of Done_Button is:',Done_Button)
    
    if key_note_played and Start_Button == True:
        key_note_played.clear()
        print(key_note_played)
        print('Clearing the key_note_played array.')
        Start_Button = False
    if key_note_played and Done_Button == True:
        played_raaga_name = find_arohanam_raag(key_note_played)            
        key_note_played.clear()
        print(key_note_played)
        Done_Button = False  
        if played_raaga_name:
            applescript = """
            display dialog "The Raaga You Had Played is %s." ¬
            with title "This is a pop-up window" ¬
            with icon caution ¬
            buttons {"OK"}
            """ % played_raaga_name

            subprocess.call("osascript -e '{}'".format(applescript), shell=True)    
        
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False
            for i in range(len(black_keys)):
                if black_keys[i].collidepoint(event.pos):
                    black_sounds[i].play(0, 1000)
                    #print(black_keys[i])
                    #print(black_keys[i].x)
                    #print(key_notes.index(black_keys[i].x))
                    key_note_played.append(key_notes.index(black_keys[i].x))
                    black_key = True
                    active_blacks.append([i, 30])
            for i in range(len(white_keys)):
                if white_keys[i].collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0, 3000)
                    #print(white_keys[i])
                    #print(white_keys[i].x)
                    #print(key_notes.index(white_keys[i].x))
                    key_note_played.append(key_notes.index(white_keys[i].x))
                    active_whites.append([i, 30])  
        print(key_note_played)        
        if event.type == pygame.TEXTINPUT:
            if event.text.upper() in left_dict:
                if left_dict[event.text.upper()][1] == '#':
                    index = black_labels.index(left_dict[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                else:
                    index = white_notes.index(left_dict[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
            if event.text.upper() in right_dict:
                if right_dict[event.text.upper()][1] == '#':
                    index = black_labels.index(right_dict[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                else:
                    index = white_notes.index(right_dict[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if right_oct < 8:
                    right_oct += 1
            if event.key == pygame.K_LEFT:
                if right_oct > 0:
                    right_oct -= 1
            if event.key == pygame.K_UP:
                if left_oct < 8:
                    left_oct += 1
            if event.key == pygame.K_DOWN:
                if left_oct > 0:
                    left_oct -= 1

    pygame.display.flip()
pygame.quit()
