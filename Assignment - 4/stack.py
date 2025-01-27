from collections import deque
import copy

class Stack(object):

    def __init__(self):
        self.__stack = deque()

    def pop_element(self):
        if self.__stack ==  None:
            return None
        else:
            return self.__stack.pop()

    def push_element(self, new_element):
        if self.__stack is None:
            self.__stack = deque()
        self.__stack.append(new_element)

    def top_element(self):
        if self.__stack is not None and len(self.__stack) > 0:
            top = copy.deepcopy(self.__stack[len(self.__stack)-1])
            return top
        else:
            return None

    def print_stack(self, order):
        if order == 0:
            if self.__stack is None or len(self.__stack) == 0:
                print("No elements found!")
            else:
                tmp = copy.deepcopy(self.__stack)
                print("Stack elements - from top to bottom:")
                while len(tmp)>0:
                    print(tmp.pop())
        elif order == 1:
            if self.__stack is None or len(self.__stack) == 0:
                print("No elements found!")
            else:
                tmp = copy.deepcopy(self.__stack)
                print("Stack elements - from bottom to top:")
                tmp.reverse()
                while len(tmp)>0:
                    print(tmp.pop())
        else:
            print("Invalid order value! Please enter 0 or 1!")

    def stack_size(self):
        if self.__stack is None:
            return None
        else:
            return len(self.__stack)