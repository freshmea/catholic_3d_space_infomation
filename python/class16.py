def main():
    with open('text.txt', 'r') as f:
        context = f.read()
    print(context)

if __name__ == '__main__':
    main()