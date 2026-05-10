import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("First game")
clock = pygame.time.Clock()

# дөрвөлжин
rect_x = 50
rect_y = 50
rect_w = 100
rect_h = 50
rect_speed = 2

# дугуй
circle_x = 300
circle_y = 200
circle_radius = 40
follow_speed = 1   # дугуй дөрвөлжин рүү ойртох хурд

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Тоглогчийн оролт
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:    
        rect_y -= rect_speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:  
        rect_y += rect_speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:  
        rect_x -= rect_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        rect_x += rect_speed

    # Дөрвөлжин дэлгэцийн хязгаартай үлдэх
    rect_x = max(0, min(rect_x, 640 - rect_w))
    rect_y = max(0, min(rect_y, 640 - rect_h))

    # Дугуй дөрвөлжин рүү ойртох
    target_x = rect_x + rect_w // 2
    target_y = rect_y + rect_h // 2

    if circle_x < target_x:
        circle_x += follow_speed
    elif circle_x > target_x:
        circle_x -= follow_speed
       
   
    if circle_y < target_y:
        circle_y += follow_speed
    elif circle_y > target_y:
        circle_y -= follow_speed
       

    # Дэлгэц шинэчлэх
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (rect_x, rect_y, rect_w, rect_h))
    pygame.draw.circle(screen, (255, 0, 0), (int(circle_x), int(circle_y)), circle_radius)

    pygame.display.flip()
    clock.tick(144)

pygame.quit()