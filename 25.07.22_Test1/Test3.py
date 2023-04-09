# print("Hello world")
# print()
# print("Hello planet", end=" \ ")
# print("Hello world")

# user_name = input("Please enter your name:")
# print(user_name)

side_a = float(input("Enter side A:"))
side_b = float(input("Enter side B:"))
side_c = float(input("Enter side C:"))

half_perimetr = (side_a + side_b + side_c) / 2
triangle_area = half_perimetr + (half_perimetr - side_a) *\
                (half_perimetr - side_b) * (half_perimetr - side_c) ** 0.5

print("The are of triangle is: " + str(triangle_area))