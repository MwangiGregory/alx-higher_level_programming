#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results_list = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
            break
        finally:
            results_list.append(res)
    return results_list
