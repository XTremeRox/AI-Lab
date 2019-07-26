#!/usr/bin/python3
def print_list_elements(l):
    for element in l:
        print(element, end=' ')
    print()
if __name__=="__main__":
    l = []
    l = ("Make me wanna say").split()
    print_list_elements(l)

    #insertion
    l.insert(4, "like")
    print_list_elements(l)

    #appending
    l.append("oh")
    print_list_elements(l)

    #removing
    l.remove("like")
    print_list_elements(l)