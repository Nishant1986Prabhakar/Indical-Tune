import sys
class Buttons:
	def check_click(self):
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
					print('The button clicked is:',self.text)
					self.pressed = False
					self.change_text(self.text) 
                    if self.text == 'Start': 
                        Start_Button = True
                        if self.text == 'Done': 
                            Done_Button = True
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77' 
