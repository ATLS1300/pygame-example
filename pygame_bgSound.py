'''
Example code - Simple Sound

Demonstates how to play backgond music. Sound effects require classes.
Requires tech.wav to be in the same folder as this script.

*** ATTENTION ***
When working with sounds or images, files must be in the same folder. Do not use paths (path/to/folder/file.wav), or they will
not un on any computer and you will lose points for errors.

You must also mak surer that you woking folder in VS code is the same folder that contains this script and your 
sound/image files. Click the folder icon on the lefthand menu and select the containing folder. A new VS Code
window will generate and you will have to reopen the file.

'''
import pygame
import pygame.mixer as mixer #alias for faster typing
pygame.init()


# FOR BACKGROUND MUSIC 
# Load music using file name (.mp3 or .wav are usable)
soundfile = "tech.wav" # change to your file name
mixer.music.load(soundfile)

# Play the song at startup
mixer.music.play()

# Stop the song
#mixer.music.stop()

# USE IN SIMPLE ANIMATION
w = 600
h = 400
win = pygame.display.set_mode((w,h))

def main():
    running = True

    while running:
        win.fill((0,0,0))
         
        for event in pygame.event.get():
            # ========= Add events here ========= 
            
            if (event.type == pygame.QUIT):
                pygame.quit()
                
        pygame.display.update()

# RUN CODE
main()