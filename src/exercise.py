def main():
    #write your code below this line
    while True:
        line = input()

        if line == '':
            break

        words = line.split()

        for word in words:
            if word.find('av') != -1:
                print(word)

if __name__ == '__main__':
    main()
