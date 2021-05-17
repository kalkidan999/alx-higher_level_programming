#!/usr/bin/python3
def def list_division(my_list_1, my_list_2, list_length):
    box = []
    for i in range(0, list_length):
        try:   
            box.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        finally:
            pass
    return box