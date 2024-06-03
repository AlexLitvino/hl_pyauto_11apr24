# class Multiply:
#
#     def __init__(self, multiplicator):
#         self.multiplicator = multiplicator
#
#     def multiply(self, number):
#         return self.multiplicator * number
#
#
# multiply_by_5 = Multiply(5)
# print(multiply_by_5.multiply(10))
# print(callable(multiply_by_5))
#
# class Multiply:
#
#     def __init__(self, multiplicator):
#         self.multiplicator = multiplicator
#
#     def __call__(self, number):
#         return self.multiplicator * number
#
# multiply_by_5 = Multiply(5)
# print(multiply_by_5(10))
# print(callable(multiply_by_5))

# ######################################################################################################################
# For callbacks

# def perform_action(func, op1, op2):
#     return func(op1, op2)
#
#
# class Action:
#
#     def __init__(self, action):
#         self.action = action
#
#     # choosing function with ladder of if/elif/else
#     def __call__(self, op1, op2):
#         self.log_action(op1, op2)
#         if self.action == 'add':
#             return op1 + op2
#         elif self.action == 'sub':
#             return op1 - op2
#         elif self.action == 'mlp':
#             return op1 * op2
#         elif self.action == 'div':
#             return op1 / op2
#         else:
#             raise ValueError("Unknown action")
#
#     def log_action(self, op1, op2):
#         print(f"Action '{self.action}' was called with operands {op1} and {op2}")
#
#
# add = Action('add')
# print(perform_action(add, 4, 6))


# ######################################################################################################################

# def perform_action(func, op1, op2):
#     return func(op1, op2)
#
#
# class Action:
#
#     action_mapping = {
#         'add': lambda x, y: x + y,
#         'sub': lambda x, y: x - y,
#         'mlp': lambda x, y: x * y,
#         'div': lambda x, y: x / y
#     }
#
#     @staticmethod
#     def default_action(op1, op2):
#         raise ValueError("Unknown action")
#
#     def __init__(self, action):
#         self.action = action
#
#     # with dictionary
#     def __call__(self, op1, op2):
#         self.log_action(op1, op2)
#         return Action.action_mapping.get(self.action, Action.default_action)(op1, op2)
#
#         # if self.action == 'add':
#         #     return op1 + op2
#         # elif self.action == 'sub':
#         #     return op1 - op2
#         # elif self.action == 'mlp':
#         #     return op1 * op2
#         # elif self.action == 'div':
#         #     return op1 / op2
#         # else:
#         #     raise ValueError("Unknown action")
#
#     def log_action(self, op1, op2):
#         print(f"Action '{self.action}' was called with operands {op1} and {op2}")
#
#
# add = Action('addQ')
# print(perform_action(add, 4, 6))

# ######################################################################################################################

def perform_action(func, op1, op2):
    return func(op1, op2)


class Action:

    def __init__(self, action):
        self.action = action

    # match/case
    def __call__(self, op1, op2):
        self.log_action(op1, op2)
        match self.action:
            case 'add' | 'sum':
                return op1 + op2
            case 'sub':
                return op1 - op2
            case 'mlp':
                return op1 * op2
            case 'div':
                return op1 / op2
            case _:
                raise ValueError("Unknown action")

    def log_action(self, op1, op2):
        print(f"Action '{self.action}' was called with operands {op1} and {op2}")


add = Action('sum')
print(perform_action(add, 4, 6))
