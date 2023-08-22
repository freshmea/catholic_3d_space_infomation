def main():
    # filepointer = open('text.txt', 'w')
    # filepointer.write("Hellow Python Programming.. I'm catholic stuent")
    # filepointer.close()
    
    with open('text1.txt', 'w') as filepointer:
        filepointer.write("hellow this is second file.")

if __name__ == '__main__':
    main()
