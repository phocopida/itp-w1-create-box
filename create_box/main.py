"""This is the entry point of the program."""


def create_box(height, width, character):
    box=""
    if height > 0  and width > 0 and isinstance(character, str):
        for number in range(height):
           box += (width * character)+"\n"
            
        return box
    else:
        print ("try again")


if __name__ == '__main__':
    create_box(3, 4, '*')
    
def create_empty_box(height, width, character):
    box=""
    if height > 0  and width > 0 and isinstance(character, str):
        for number in range(height):
            if number == 0:
                box += (width * character)+"\n"
            elif number == height-1:
                box += (width * character)+"\n"
            else:
                box += character + " "*(width-2) + character+"\n"
        return box
    else:
        print ("try again")
