from raylibpy import Vector2, Color, draw_circle, RAYWHITE

def draw_point_grid(start: Vector2, end: Vector2, grid_size: float):
        grid_lines_x = int((end.x - start.x) // grid_size) + 2
        grid_lines_y = int((end.y - start.y) // grid_size) + 2

        for y in range(grid_lines_y):
            for x in range(grid_lines_x):
                offset_x = start.x - (start.x % grid_size)
                offset_y = start.y - (start.y % grid_size)

                real_x = int(x * grid_size + offset_x)
                real_y = int(y * grid_size + offset_y)

                draw_circle(real_x, real_y, 2.0, RAYWHITE)

def draw_resistor(position: Vector2, color: Color):
    pass
