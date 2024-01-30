#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        quotion = 0
        try:
            quotion = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except Exception:
            quotion = 0
        finally:
            new_list.append(quotion)
    return new_list
