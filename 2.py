import turtle


def draw_pythagoras_tree(branch_len, level, angle):
    if level == 0:
        return

    turtle.forward(branch_len)

    turtle.left(angle)
    draw_pythagoras_tree(branch_len * 0.7, level - 1, angle)

    turtle.right(2 * angle)

    draw_pythagoras_tree(branch_len * 0.7, level - 1, angle)

    turtle.left(angle)

    turtle.backward(branch_len)


def pythagoras_tree(level):
    turtle.speed('fastest')
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()

    draw_pythagoras_tree(100, level, 30)

    turtle.done()


try:
    level = int(input("Введіть рівень рекурсії (рекомендовано 5-10): "))
    if level < 0:
        raise ValueError("Рівень рекурсії має бути додатним числом.")
except ValueError as e:
    print(f"Помилка: {e}")
else:
    pythagoras_tree(level)
