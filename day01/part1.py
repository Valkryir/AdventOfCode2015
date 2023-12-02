def main():
    directions = open('input.txt')

    currentFloor = 0

    currentPosition = 0

    for entry in directions:
        for nextFloor in entry:
            currentPosition += 1
            if nextFloor == "(":
                currentFloor += 1

            elif nextFloor == ")":
                currentFloor -= 1

            if currentFloor == -1:
                break;

    print(currentPosition)


if __name__ == '__main__':
    main()
