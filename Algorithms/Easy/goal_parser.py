"""
1678. Goal Parser Interpretation

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
"""


class Interpret(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command_mapping = {
            "()": "o",
            "(al)": "al",
        }
        for command_input, command_output in command_mapping.items():
            command = command.replace(command_input, command_output)
        return command

    def interpret2(self, command):
        """
        :type command: str
        :rtype: str
        """
        return command.replace("()", "o").replace("(al)", "al")


if __name__ == "__main__":
    command1 = "G()(al)"
    command2 = "G()()()()(al)"
    command3 = "(al)G(al)()()G"
    print(Interpret().interpret(command=command1))
    print(Interpret().interpret(command=command2))
    print(Interpret().interpret(command=command3))
