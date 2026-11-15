import pygame
import random
import copy
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("300x200+500+300")
root.title("贪吃蛇小游戏")
label1 = tk.Label(root, text="欢迎来到贪吃蛇小游戏！", font=("Arial", 16))
label1.pack(pady=10)
def show_game_over():
    root2 = tk.Toplevel(root)
    root2.geometry("300x200+500+300")
    root2.title("Game Over")
    label = tk.Label(root2, text="Game Over", font=("Arial", 20))
    label.pack(pady=10)
    button = tk.Button(root2, text="OK", command=lambda: [root2.destroy(), root.deiconify()])
    button.pack(pady=10)
    button_again = tk.Button(root2, text="重新开始", command=lambda: [root2.destroy(), main()])
    button_again.pack(pady=10)
    button_quit = tk.Button(root2, text="退出游戏", command=root.quit)
    button_quit.pack(pady=10)
def main():
    root.withdraw()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("贪吃蛇小游戏")
    clock = pygame.time.Clock()
    snake = [[100, 100], [90, 100], [80, 100]]
    set_left = False
    set_right = True
    set_up = False
    set_down = False
    food = [random.randint(2, 58) * 10, random.randint(2, 58) * 10]
    score = 0
    running = True
    while running:
        clock.tick(20)
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not set_right:
                    set_left = True
                    set_right = False
                    set_up = False
                    set_down = False
                if event.key == pygame.K_RIGHT and not set_left:
                    set_left = False
                    set_right = True
                    set_up = False
                    set_down = False
                if event.key == pygame.K_UP and not set_down:
                    set_left = False
                    set_right = False
                    set_up = True
                    set_down = False
                if event.key == pygame.K_DOWN and not set_up:
                    set_left = False
                    set_right = False
                    set_up = False
                    set_down = True
        head_x = snake[0][0]
        head_y = snake[0][1]
        if set_left:
            head_x -= 10
        if set_right:
            head_x += 10
        if set_up:
            head_y -= 10
        if set_down:
            head_y += 10
        new_head = [head_x, head_y]
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = copy.deepcopy(snake[i - 1])
        snake[0] = new_head
        for i in snake[0:]:
            if i[0] < 10 or i[0] > 580 or i[1] < 10 or i[1] > 580:
                running = False
            if new_head in snake[1:]:
                running = False
        if abs(new_head[0] - food[0]) < 10 and abs(new_head[1] - food[1]) < 10:
            score += 1
            food = [random.randint(2, 58) * 10, random.randint(2, 58) * 10]
            snake.append(copy.deepcopy(snake[-1]))
        for i in snake:
            pygame.draw.rect(screen, (0, 255, 0), (i[0], i[1], 10, 10))
        pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 10, 10))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, 600), 5)
        text1 = pygame.font.SysFont(None, 30).render("Snake Game", True, (0, 0, 0))
        screen.blit(text1, (640, 250))
        text2 = pygame.font.SysFont(None, 30).render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(text2, (640, 280))
        pygame.display.update()
    pygame.quit()
    show_game_over()
    messagebox.showinfo("Game Over", "游戏结束！您的得分为：" + str(score))
button_begin = tk.Button(root, text="开始游戏", command=main)
button_begin.pack(pady=10)
button_again = tk.Button(root, text="重新开始", command=main)
button_again.pack(pady=10)
button_quit = tk.Button(root, text="退出游戏", command=root.quit)
button_quit.pack(pady=10)
root.mainloop()
