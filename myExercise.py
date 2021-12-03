import sys

filename = sys.argv[1]
student_names = sys.argv[2].split(',')

try:
    f = open(filename)
    count = 0
    for line in f.readlines():
        line1 = line
        line = line.split(':')
        if line[0] in student_names[count]:
            print(line1)
        else:
            raise Exception("No record of %s was found." % student_names[count])
        count += 1
except FileNotFoundError:
    print("The file you entered not found. Try again.")
except EOFError:
    print("End of file case.")
except IOError:
    print("An error occured when reading a file.")
except Exception as e:
    print(e)




