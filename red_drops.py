import math
import keyboard

coordinates = [[29.5, 82.5],
        [21.8, 87.8],
        [10.6, 81.5],
        [21.9, 73.1],
        [11.2, 62.4],
        [12.3, 13],
        [22.1, 10.4],
        [31.1, 9.9],
        [55.9, 10.1],
        [69.8, 10.3],
        [73.5, 12.7],
        [83.1, 10.3],
        [89.5, 13.5],
        [80.5, 21.2],
        [87.8, 37.9],
        [89.7, 70.1],
        [85.8, 78.5],
        [76.8, 87.2]]


def calculate_distance(point1, point2):
    difference_of_X = point2[0] - point1[0]
    difference_of_Y = point2[1] - point1[1]

    difference_of_X = difference_of_X ** 2
    difference_of_Y = difference_of_Y ** 2

    sum = difference_of_Y + difference_of_X

    return math.sqrt(sum)

if __name__ == '__main__':
    x_value = float(input("Enter your current X coordinate\n"))
    y_value = float(input("Enter your current Y coordinate\n"))
    startIndex = -1
    currentShortestDistance = float("inf")

    for i in range(len(coordinates)):
        distance = calculate_distance([x_value, y_value], coordinates[i])

        if distance < currentShortestDistance:
            currentShortestDistance = distance
            startIndex = i

    print("The closest Red Drop is located at: ")
    print(coordinates[startIndex])
    print("\n")


    print("Hit the Enter key to see the next Red Drop location\n")
    while True:
        keyboard.wait("enter")
        startIndex += 1
        startIndex %= len(coordinates)
        print("The next Red Drop location is at: ")
        print(coordinates[startIndex])
        print("\n")
        print("Hit the Enter key to see the next Red Drop location\n")
