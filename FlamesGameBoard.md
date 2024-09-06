# GameInPython
My first Board Game Project - F L A M E S

"F": "Friendship", "L": "Love", "A": "Affection", "M": "Marriage", "E": "Enemy", "S": "Siblings"

# About this game
```
  Enter your name in the 'your name' textbox
  Enter friend name in 'Friend name' textbox

  Click the box 'Click to see the result'

  Result box will show the result of the game

  You can play multiple times with different names in the same board.

  Quit the game by click 'X' button of the board

  Enjoy and have fun!!!!
```

## Step 1: Initiate Pygame board
```
  def __init__(self, game_screen, game_clock):
          # Initiate board title, input text boxes, play button, final result text box configuration for the board
          self.clock = game_clock
          self.screen = game_screen
          self.base_font = pygame.font.Font(None, 22)
          self.title_text = " F - Friendship  L - Love    A - Affection   M - Marriage    E - Enemy   S - Siblings"
          self.title = { "rect": pygame.Rect(self.screen.get_width()/28, self.screen.get_width()/18, self.screen.get_width()/2, 32), "color": pygame.Color('lightsteelblue3'), "text": self.title_text, "active": False}
          self.input_text_boxes = [
              {"rect": pygame.Rect(self.screen.get_width()/6, self.screen.get_width()/6, 140, 32), "color": pygame.Color('lightskyblue3'), "text": "Your first name", "active": False},
              {"rect": pygame.Rect(self.screen.get_width()/2, self.screen.get_width()/6, 140, 32), "color": pygame.Color('chartreuse4'), "text": "Friend first name", "active": False}
          ]
          self.play_button = {"rect": pygame.Rect(self.screen.get_width()/3, self.screen.get_width()/4, 140, 32), "color": pygame.Color('lightseagreen'), "text": "Click here to see the result", "active": False}  
          self.final_result_box = {"rect": pygame.Rect(self.screen.get_width()/8, self.screen.get_width()/2.8, 200, 50), "color": pygame.Color('lightsteelblue3'), "text": "Result", "active": False}
```
          
## Step 2: Draw Input boxes for 'Input'
```
  def draw_input_boxes(self):
        for box in self.input_text_boxes:
            pygame.draw.rect(self.screen, box["color"], box["rect"], 2)
            text_surface = self.base_font.render(box["text"], True, (255, 255, 255))
            self.screen.blit(text_surface, (box["rect"].x + 5, box["rect"].y + 5))
            box["rect"].w = max(200, text_surface.get_width() + 10)
```
## Step 3: Draw button for result for 'Click to see the result'
```
  def draw_button(self):
        pygame.draw.rect(self.screen, self.play_button["color"], self.play_button["rect"], 2)
        button_text_surface = self.base_font.render(self.play_button["text"],True,(255,255,255))
        self.screen.blit(button_text_surface, (self.play_button["rect"].x + 5, self.play_button["rect"].y + 5))
        self.play_button["rect"].w = max(self.screen.get_width()/3, button_text_surface.get_width() + 10)
```

## Step 4: Handler for Textbox and Button
```
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
```
```
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
```
## Step 5: Draw Result Textbox to see the final result
```
  def draw_final_result_box(self):
        #pygame.draw.rect(self.screen, self.final_result_box["color"], self.final_result_box["rect"], 2)
        button_text_surface = self.base_font.render(self.final_result_box["text"],True,(255,255,255))
        self.screen.blit(button_text_surface, (self.final_result_box["rect"].x + 5, self.final_result_box["rect"].y + 5))
        self.final_result_box["rect"].w = max(100, button_text_surface.get_width() + 10)
```

### Logic behind this game
```
Iterate the 'FLAMES' word letter by letter until the total_letters_count, the remove the letter from the word 'FLAMES'.
Repeat this procedure until one letter remains in the word 'FLAMES'
That letter represents the relationship between two names
```
