from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_brackets_stack.append(' ')


    for i, next in enumerate(text):
        if next in "([{":
            
            bo=Bracket(next,i+1)
            opening_brackets_stack.append(bo)

        if next in ")]}":
            last_op_br=opening_brackets_stack.pop()
            br=last_op_br.char
            if(are_matching(br,next)==False):
                bc=Bracket(next,i+1)
                
                print(bc.position)
                return


    if(len(opening_brackets_stack)>1):
        brac=opening_brackets_stack.pop()
        print(brac.position)

    else:
        print("Success")
 
        
def main():

    text=input()

    if(text.startswith("I")):
        
        find_mismatch(text)

    if(text.startswith("F")):
        filename=input()
        file=open(filename,"r")
        find_mismatch(file.read())
    else:
        find_mismatch(text)

   

if __name__ == "__main__":
    main()
