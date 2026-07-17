from math import radians, cos, sin
import datetime

angle_degrees = 40
angle_radians = radians(angle_degrees)

sin_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sin_value)
print(cos_value)


birthday = datetime.date(1991, 9, 14)
print(birthday.day)
print(birthday.month)
print(birthday.year)