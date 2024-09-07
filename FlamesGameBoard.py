import pygame 
import sys

# Step 1: Initiate Pygame board
# Step 2: Draw Input boxes
# Step 3: Draw button for result
# Step 4: Animate the result
class FlamesGameBoard:

    def __init__(self, game_screen, game_clock):
        # Initiate board title, input text boxes, play button, final result text box configuration for the board
        self.clock = game_clock
        self.screen = game_screen
        self.base_font = pygame.font.Font(None, 22)
        self.title_text = " F - Friendship  L - Love    A - Affection   M - Marriage    E - Enemy   S - Siblings"
        self.title = { "rect": pygame.Rect(self.screen.get_width()/28, self.screen.get_width()/18,self.screen.get_width()/2, 32),"color": pygame.Color('lightsteelblue3'),"text": self.title_text,"active": False}
        self.input_text_boxes = [
            {"rect": pygame.Rect(self.screen.get_width()/6,self.screen.get_width()/6, 140, 32),"color": pygame.Color('lightskyblue3'),"text": "Your first name","active": False},
            {"rect": pygame.Rect(self.screen.get_width()/2,self.screen.get_width()/6, 140, 32),"color": pygame.Color('chartreuse4'),"text": "Friend first name","active": False}
        ]
        self.play_button = {"rect": pygame.Rect(self.screen.get_width()/3,self.screen.get_width()/4, 140, 32),"color": pygame.Color('lightseagreen'),"text": "Click here to see the result","active": False}

        self.final_result_box = {"rect": pygame.Rect(self.screen.get_width()/8,self.screen.get_width()/2.8, 200, 50),"color": pygame.Color('lightsteelblue3'),"text": "Result","active": False}

    # Get the final result of the game with the names
    def playFlames(self, your_name, friend_name):
        
        flames_dict = { "F": "Friendship", "L": "Love", "A": "Affection", "M": "Marriage", "E": "Enemy", "S": "Siblings" }

        # Remove identical letters from names
        # Calculate the total charcters in the names and play flames
        if len(your_name) > 0 and len(friend_name) > 0:
            
            # Remove any spaces in names
            your_name = your_name.replace(' ','')
            friend_name = friend_name.replace(' ','')

            identical_chars = []

            # Find identical letters in names
            for y_len in range(len(your_name)):
                for f_len in range(len(friend_name)):
                    if your_name[y_len] == friend_name[f_len]:
                        identical_chars.append(your_name[y_len])
                        break
            
            # Remove the identical letters from the names
            for char in identical_chars:
                your_name = your_name.replace(char,'',1)
                friend_name = friend_name.replace(char,'',1)

            # count the letters in names
            total_letters_count = len(your_name)+len(friend_name)

            # initiate list with FLAMES letters which is convinient for iteration, remove items
            the_word = ['F','L','A','M','E','S']

            # calculate the list length which is 'FLAMES' word length
            the_word_length = len(the_word)

            # Loop until one word remains in the list
            while len(the_word) > 1 and total_letters_count > 0:

                # initiate the iteration count for FLAMES word
                the_iter_count = 0
                char_index = 0
                # Logic behind this game
                # Iterate the 'FLAMES' word letter by letter until the total_letters_count, the remove the letter from the word 'FLAMES'.
                # Repeat this procedure until one letter remains in the word 'FLAMES'
                # That letter represents the relationship between two names
                while the_iter_count < total_letters_count and len(the_word) > 1:
                    for char_index in range(len(the_word)):
                        the_iter_count += 1
                        if the_iter_count == total_letters_count and char_index < len(the_word):
                            try:
                                the_word.pop(char_index)
                            except:
                                print("Something gone wrong. Check your game")
                            print(the_word)
                            if char_index < len(the_word):
                                char_index += 1
                                the_iter_count = 0


                # # Iterate the list with the index until it exceeds the 'FLAMES' word length
                # while the_word_index >= len(the_word): 

                #     # Recalculate the index (Length of 'FLAMES' word - the calculated index - 1)
                #     the_word_index = abs(len(the_word) - the_word_index)
                    
                # # Remove the letter from the list with calculated index
                # the_word.pop(the_word_index)

            # get the result of the letter from FLAMES
            print(the_word)
            result = str(the_word[0])
            if len(result) > 0:
                for letter in flames_dict.keys():
                    if letter == result: return 'Success: ' + flames_dict[letter]
            else:
                return 'Success: ' + flames_dict['F']
        else:
            return 'Names should not be blank'

    # Draw Board Title - title should be inactive
    def draw_title(self):
        #pygame.draw.rect(self.screen, self.title["color"], self.title["rect"], 2)
        title_text_surface = self.base_font.render(self.title["text"],True,(255, 255, 255))
        self.screen.blit(title_text_surface,(self.title["rect"].x + 5, self.title["rect"].y + 5))
        self.title["rect"].w = max(100,title_text_surface.get_width() + 10)

    # Draw Input Text boxes - inputs by keystrokes
    def draw_input_boxes(self):
        for box in self.input_text_boxes:
            pygame.draw.rect(self.screen,box["color"],box["rect"],2)
            text_surface = self.base_font.render(box["text"],True,(255, 255, 255))
            self.screen.blit(text_surface,(box["rect"].x + 5,box["rect"].y + 5))
            box["rect"].w = max(200,text_surface.get_width() + 10)
    
    # Input Text boxes Event Handler
    def text_handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in self.input_text_boxes:
                if box["rect"].collidepoint(event.pos):
                    box["active"] = not box["active"]
                    box["text"] = ""
                else:
                    box["active"] = False
        elif event.type == pygame.KEYDOWN:
            for box in self.input_text_boxes:
                if box["active"]:
                    if event.key == pygame.K_BACKSPACE:
                        box["text"] = box["text"][:-1]
                    else:
                        box["text"] += event.unicode
            
    # Draw Play Button - should be active by mouse click or mouse button down
    def draw_button(self):
        pygame.draw.rect(self.screen,self.play_button["color"],self.play_button["rect"],2)
        button_text_surface = self.base_font.render(self.play_button["text"],True,(255,255,255))
        self.screen.blit(button_text_surface,(self.play_button["rect"].x + 5,self.play_button["rect"].y + 5))
        self.play_button["rect"].w = max(self.screen.get_width()/3,button_text_surface.get_width() + 10)

    # Button event handler
    def button_handle_event(self,event):
        names = []
        if event.type == pygame.MOUSEMOTION:
            if self.play_button["rect"].collidepoint(event.pos):
                self.play_button["active"] = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button["rect"].collidepoint(event.pos):
                if self.play_button["active"]:
                    for input_box in self.input_text_boxes:
                        names.append(str(input_box["text"]))
                    self.final_result_box["text"] = self.playFlames(names[0], names[1])

    # Draw final Result text box - box should be inactive
    def draw_final_result_box(self):
        #pygame.draw.rect(self.screen, self.final_result_box["color"], self.final_result_box["rect"], 2)
        button_text_surface = self.base_font.render(self.final_result_box["text"],True,(255,255,255))
        self.screen.blit(button_text_surface,(self.final_result_box["rect"].x + 5,self.final_result_box["rect"].y + 5))
        self.final_result_box["rect"].w = max(100,button_text_surface.get_width() + 10)

def main_game():

    pygame.init()
    pygame.display.set_caption("F L A M E S Game - by Bhuvana")
    screen = pygame.display.set_mode((600,400))
    clock = pygame.time.Clock()
    myboard = FlamesGameBoard(screen, clock)

    print("Game On")

    game_input_boxes = myboard.input_text_boxes
    game_button = myboard.play_button
    game_result = myboard.final_result_box
    
    while True:
        #print(pygame.event.get())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                print("Game Quits")
            else:
                myboard.text_handle_event(event)
                myboard.button_handle_event(event)

        myboard.screen.fill((30,30,30))
        myboard.draw_title()
        myboard.draw_input_boxes()
        myboard.draw_button()
        myboard.draw_final_result_box()

        pygame.display.update()
        myboard.clock.tick(30)

main_game()
