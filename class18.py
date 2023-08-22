def main():
    with open('text.txt', 'r') as f:
        context = f.readlines()

    for line in context:
        print(line)

if __name__ == '__main__':
    main()
