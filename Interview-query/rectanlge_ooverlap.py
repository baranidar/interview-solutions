#https://www.interviewquery.com/questions/rectangle-overlap
def rectangle_overlap(a, b):
    def get_rectangle_bounds(rec):
        x_coordinates = []
        y_coordinates = []
        for item in rec:
            x_coordinates.append(item[0])
            y_coordinates.append(item[1])

        return min(x_coordinates), max(x_coordinates), min(y_coordinates), max(y_coordinates)

    min_x_a, max_x_a, min_y_a, max_y_a = get_rectangle_bounds(a)
    min_x_b, max_x_b, min_y_b, max_y_b = get_rectangle_bounds(b)

    overlap_in_x = min_x_a <= max_x_b and min_x_b <= max_x_a
    overlap_in_y = min_y_a <= max_y_b and min_y_b <= max_y_a

    return overlap_in_x and overlap_in_y

a = [(-3,5), (-3,2),(0,5),(0,2)]
b = [(-1,4), (3,4), (3,1), (-1,1)]

print(rectangle_overlap(a, b))