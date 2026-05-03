import pygame

pygame.init()
# A window must be open to capture keyboard input
screen = pygame.display.set_mode((400, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Detect key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("Move Up")
            elif event.key == pygame.K_s:
                print("Move Down")
            elif event.key == pygame.K_a:
                print("Move Left")
            elif event.key == pygame.K_d:
                print("Move Right")
            elif event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
