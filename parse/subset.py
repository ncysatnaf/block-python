# Task: Write a procedure that accpets a list as an argument.
# The procedure should print out all of the subsets of that list.

def sublists(big_list, selected_so_far):

    if big_list == []:
        return [selected_so_far]
    else:
        current_element = big_list[0]
        rest_of_big_list = big_list[1:]
        return sublists(rest_of_big_list, selected_so_far + [current_element]) + \
               sublists(rest_of_big_list, selected_so_far)

dinner_guests = ["LM", "ECS", "SBA"]
print sublists(dinner_guests, [])
