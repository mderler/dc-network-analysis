from raylibpy import *
from drawing import draw_point_grid


def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "DC Network Analysis")

    BG_COLOR = Color(22, 22, 22)
    GRID_SIZE = 50

    camera = Camera2D()
    camera.zoom = 1.0

    set_target_fps(60)

    while not window_should_close():
        if is_mouse_button_down(MOUSE_BUTTON_RIGHT):
            delta = get_mouse_delta()
            delta  = delta * (-1.0 / camera.zoom)
            camera.target += delta

        wheel = get_mouse_wheel_move()

        if wheel != 0:
            mouseWorldPos = get_screen_to_world2d(get_mouse_position(), camera)
            camera.offset  = get_mouse_position()
            camera.target  = mouseWorldPos
            zoomIncrement = 0.125
            camera.zoom  += (wheel * zoomIncrement)

            if camera.zoom < 0.75:
                camera.zoom = 0.75

        begin_drawing()
        clear_background(BG_COLOR)

        begin_mode2d(camera)

        grid_start = get_screen_to_world2d(Vector2(-GRID_SIZE, -GRID_SIZE), camera)
        grid_end = get_screen_to_world2d(Vector2(SCREEN_WIDTH, SCREEN_HEIGHT), camera)

        draw_point_grid(grid_start, grid_end, GRID_SIZE)

        draw_circle(100, 100, 10, YELLOW)

        end_mode2d()

        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
