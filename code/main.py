import tkinter as tk
import random
import time

class Tetris(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tetris")  # Устанавливаем заголовок окна игры
        self.resizable(False, False)  # Запрещаем изменение размеров окна

        # Создаем холст для отрисовки игрового поля
        self.canvas = tk.Canvas(self, width=300, height=600, bg="black")
        self.canvas.pack()

        # Создаем метки для отображения счета и уровня
        self.score_label = tk.Label(self, text="Score: 0", font=("Arial", 16))
        self.score_label.pack()
        self.level_label = tk.Label(self, text="Level: 1", font=("Arial", 16))
        self.level_label.pack()

        # Создаем кнопку для перезапуска игры
        self.restart_button = tk.Button(self, text="Restart", command=self.restart_game)
        self.restart_button.pack()

        # Инициализируем переменные для счета, уровня и количества удаленных линий
        self.score = 0
        self.level = 1
        self.lines_cleared = 0

        # Определяем формы тетромино и их цвета
        self.shapes = [
            [(0, 1), (1, 1), (2, 1), (3, 1)],  # I shape
            [(0, 1), (1, 0), (1, 1), (2, 1)],  # T shape
            [(0, 1), (1, 1), (2, 1), (2, 0)],  # L shape
            [(0, 0), (0, 1), (1, 1), (1, 0)],  # O shape
            [(0, 1), (1, 1), (1, 0), (2, 0)],  # S shape
            [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z shape
            [(0, 1), (1, 1), (1, 0), (2, 1)],  # J shape
        ]

        self.colors = ["cyan", "purple", "orange", "yellow", "green", "red", "blue"]

        # Инициализируем переменные для текущей, следующей и сохраненной фигур
        self.current_shape = None
        self.next_shape = random.choice(self.shapes)
        self.hold_shape = None
        self.shape_color = None

        # Создаем игровое поле
        self.board = [[0] * 10 for _ in range(20)]

        # Привязываем клавиши для управления игрой
        self.bind("<Key>", self.key_pressed)

        # Запускаем игру
        self.start_game()

    def start_game(self):
        # Начинаем новую игру
        self.current_shape = self.next_shape
        self.shape_color = random.choice(self.colors)
        self.next_shape = random.choice(self.shapes)
        self.current_position = [0, 4]  # Устанавливаем начальную позицию фигуры
        self.drop_shape()  # Запускаем падение фигуры

    def restart_game(self):
        # Перезапускаем игру и сбрасываем все переменные
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.board = [[0] * 10 for _ in range(20)]
        self.update_score_label()
        self.update_level_label()
        self.start_game()

    def draw_shape(self, shape, offset, color):
        # Отрисовываем фигуру на холсте
        for x, y in shape:
            self.canvas.create_rectangle(
                (y + offset[1]) * 30, (x + offset[0]) * 30,
                (y + offset[1] + 1) * 30, (x + offset[0] + 1) * 30,
                fill=color, outline="black"
            )

    def clear_lines(self):
        # Удаляем заполненные линии и обновляем счет и уровень
        full_lines = [i for i, row in enumerate(self.board) if all(row)]
        for i in full_lines:
            del self.board[i]
            self.board.insert(0, [0] * 10)

        self.score += len(full_lines) * 100
        self.lines_cleared += len(full_lines)
        if self.lines_cleared >= self.level * 10:
            self.level += 1
        self.update_score_label()
        self.update_level_label()

    def drop_shape(self):
        # Падение текущей фигуры вниз
        if self.check_collision(self.current_shape, [self.current_position[0] + 1, self.current_position[1]]):
            self.place_shape(self.current_shape, self.current_position, self.shape_color)
            self.clear_lines()
            if self.check_game_over():
                self.game_over()
                return
            self.start_game()
        else:
            self.current_position[0] += 1
            self.update()
            self.after(500 - (self.level - 1) * 50, self.drop_shape)

    def move_shape(self, dx, dy):
        # Движение текущей фигуры влево или вправо
        new_position = [self.current_position[0] + dx, self.current_position[1] + dy]
        if not self.check_collision(self.current_shape, new_position):
            self.current_position = new_position
            self.update()

    def check_collision(self, shape, offset):
        # Проверка на столкновение фигуры с другими фигурами или границами поля
        for x, y in shape:
            new_x, new_y = x + offset[0], y + offset[1]
            if new_x >= 20 or new_y < 0 or new_y >= 10 or self.board[new_x][new_y]:
                return True
        return False

    def place_shape(self, shape, offset, color):
        # Размещение фигуры на игровом поле
        for x, y in shape:
            new_x, new_y = x + offset[0], y + offset[1]
            self.board[new_x][new_y] = color

    def check_game_over(self):
        # Проверка на окончание игры (когда фигуры достигают верхней границы поля)
        return any(self.board[0])

    def game_over(self):
        # Вывод сообщения "Game Over" на экран
        self.canvas.create_text(150, 300, text="Game Over", fill="white", font=("Arial", 24))

    def key_pressed(self, event):
        # Обработка нажатий клавиш для управления игрой
        if event.keysym == "Left":
            self.move_shape(0, -1)
        elif event.keysym == "Right":
            self.move_shape(0, 1)
        elif event.keysym == "Down":
            self.move_shape(1, 0)
        elif event.keysym == "Up":
            self.rotate_shape()
        elif event.keysym == "space":
            while not self.check_collision(self.current_shape, [self.current_position[0] + 1, self.current_position[1]]):
                self.current_position[0] += 1
            self.drop_shape()

    def rotate_shape(self):
        # Поворот текущей фигуры
        new_shape = [(-y, x) for x, y in self.current_shape]
        if not self.check_collision(new_shape, self.current_position):
            self.current_shape = new_shape
            self.update()

    def update(self):
        # Обновление отображения игрового поля и текущей фигуры
        self.canvas.delete("all")
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    self.canvas.create_rectangle(
                        x * 30, y * 30,
                        (x + 1) * 30, (y + 1) * 30,
                        fill=cell, outline="black"
                    )
        self.draw_shape(self.current_shape, self.current_position, self.shape_color)

    def update_score_label(self):
        # Обновление метки счета
        self.score_label.config(text=f"Score: {self.score}")

    def update_level_label(self):
        # Обновление метки уровня
        self.level_label.config(text=f"Level: {self.level}")

if __name__ == "__main__":
    app = Tetris()
    app.mainloop()
