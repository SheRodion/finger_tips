# ID 67502300
from collections import Counter


def counter(finger_tips, field):
    keys_field = Counter(
        int(symbol) for row in field for symbol in row if symbol != '.')
    count = sum(symbol <= 2 * finger_tips for symbol in keys_field.values())
    return count


if __name__ == '__main__':
    finger_tips = int(input())
    field = (input() for _ in range(4))
    print(counter(finger_tips, field))
