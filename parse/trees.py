
def insert(tree, element):
    if tree == None:
        return (None, element, None)
    else:
        left_child = tree[0]
        this_element = tree[1]
        right_child = tree[2]
        if element <= this_element:
            new_left_child = insert(left_child, element)
            return (new_left_child, this_element, right_child)
        else:
            # element >= this_element
            new_right_child = insert(right_child, element)
            return (left_child, this_element, new_right_child)

def print_tree(tree):
    if tree == None:
        return
    else:
        left_child = tree[0]
        this_element = tree[1]
        right_child = tree[2]
        print_tree(left_child)
        print this_element
        print_tree(right_child)

def contains(tree, element):
    if tree == None:
        return False
    else:
        left_child = tree[0]
        this_element = tree[1]
        right_child = tree[2]
        if this_element == element:
            return True
        elif this_element <= element:
            return contains(left_child,element)
        else:
            return contains(right_child,element)


# t1 = (None, "midpoint", None)
# t2 = insert(t1, "zuma, jacob")
# t3 = insert(t2, "atwood, margaret")
#
# print_tree(t3)
# print contains(t3, "hahha")


t4 = None
for i in [6,3,5,6,24,6,4,5,8,6,34,5,7,9,0,7,8,9,2,1,2,3,4,7]:
    t4 = insert(t4, i)

print_tree(t4)
print contains(t4, "99")
