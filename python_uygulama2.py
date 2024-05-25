import math

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)] 

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)
print("Minimum mesafe:", min_distance)

# Örnek nokta tanımlaması yapılmadan, kullanıcıdan nokta girişi alarak bu kod yazmak istenirse;
# import math

# # Noktaların kullanıcıdan alınması
# def get_points():
#     points = []
#     n = int(input("Kaç nokta gireceksiniz? "))
#     for i in range(n):
#         x = float(input("{}. noktanın x koordinatını girin: ".format(i+1)))
#         y = float(input("{}. noktanın y koordinatını girin: ".format(i+1)))
#         points.append((x, y))
#     return points

# # Öklid Mesafesi İçin Bir Fonksiyon Yazma
# def euclideanDistance(point1, point2):
#     x1, y1 = point1
#     x2, y2 = point2
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# # Mesafelerin Hesaplanması
# def calculate_distances(points):
#     distances = []
#     for i in range(len(points)):
#         for j in range(i+1, len(points)):
#             distance = euclideanDistance(points[i], points[j])
#             distances.append(distance)
#     return distances

# # Minimum Mesafenin Bulunması
# def find_minimum_distance(distances):
#     min_distance = min(distances)
#     return min_distance

# # Noktaların alınması
# points = get_points()

# # Mesafelerin Hesaplanması
# distances = calculate_distances(points)

# # Minimum Mesafenin Bulunması
# min_distance = find_minimum_distance(distances)
# print("Minimum mesafe:", min_distance)

