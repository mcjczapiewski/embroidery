

def draw_rectangle(
    width, height, border_color=1, fill_color=1, border_width=1
):
    matrix = []
    for row_number in range(height):
        new_row = str(border_color) * width
        matrix.append(list(map(int, new_row)))
    row_number = 1
    for row in matrix[:]:
        if border_width < row_number <= height - border_width:
            starting = border_width
            ending = len(row) - border_width
            for item in row[starting:ending]:
                row[starting] = fill_color
                starting += 1
        row_number += 1
    return matrix


def draw_triangle(height, border_color=1, fill_color=1):
    matrix = []
    #     if height < 1:
    #         print("The height can't be lower than 1!")
    #         return matrix
    #     elif height > 40:
    #         print("Height value greater than 40 would not look good on screen, \
    # please change it.")
    #         return matrix
    number_of_columns = 1 + (height - 1) * 2
    number_of_rows = height
    new_row = str(border_color)
    append_to_matrix(matrix, new_row, number_of_columns)
    for row_number in range(1, height):
        new_row = str(border_color) * (1 + 2 * row_number)
        append_to_matrix(matrix, new_row, number_of_columns)
    matrix = change_fill_color(matrix, number_of_rows, border_color, number_of_columns, fill_color)
    return matrix


def draw_christmas_tree(blocks, border_color=1, fill_color=2):
    matrix = []
    number_of_columns = 5 + (-2 + 2 * 2) * (blocks - 1)
    number_of_rows = blocks * 3
    number_of_border_colors = -1
    for row_number in range(number_of_rows):
        if row_number % 3 == 0 and row_number > 0:
            number_of_border_colors -= 2
        else:
            number_of_border_colors += 2
        new_row = str(border_color) * number_of_border_colors
        append_to_matrix(matrix, new_row, number_of_columns)
    matrix = change_fill_color(matrix, number_of_rows, border_color, number_of_columns, fill_color)
    return matrix


def append_to_matrix(matrix, new_row, number_of_columns):
    matrix.append(list(map(int, new_row.center(number_of_columns, "0"))))


def change_fill_color(matrix, number_of_rows, border_color, number_of_columns, fill_color):
    row_number = 1
    for row in matrix[:]:
        if row_number < number_of_rows and row.count(border_color) > 2:
            fill_number = row.count(border_color) - 3
            middle_list_point = int(number_of_columns / 2)
            if fill_number > 1:
                starting = int(middle_list_point - fill_number / 2)
                ending = int(middle_list_point + fill_number / 2 + 1)
                for item in row[starting:ending]:
                    row[starting] = fill_color
                    starting += 1
            else:
                row[middle_list_point] = fill_color
        row_number += 1
    return matrix


def draw_circle(radius):
    matrix = []
    return matrix


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end="")
        print()
    print()


if __name__ == "__main__":
    color_scheme = {0: " ", 1: "*", 2: "."}
    embroider(
        [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 2, 1, 0, 0],
            [0, 1, 2, 2, 2, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
        ],
        color_scheme,
    )

    embroider(draw_rectangle(10, 10, border_color=1, fill_color=2, border_width=2), color_scheme)
    embroider(draw_triangle(10, border_color=1, fill_color=2), color_scheme)
    embroider(draw_christmas_tree(7), color_scheme)
    # This should have the same output:
    # embroider(draw_triangle(4, border_color=1, fill_color=2), color_scheme)
