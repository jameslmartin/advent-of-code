
def scan(input, window_size):
    start = 0
    stop = window_size
    while stop <= len(input):
        window = input[start:stop]
        chars = set(window)
        if len(chars) == window_size:
            break
        else:
            start += 1
            stop +=1
    return stop

if __name__ == "__main__":
    with open("input.txt") as input:
        line = input.readline()
        marker = scan(line, window_size=4)
        message = scan(line, window_size=14)
    print(message)