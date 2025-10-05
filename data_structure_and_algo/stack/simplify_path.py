"""


You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:
To simplify a path, you need to follow a specific set of rules:
Canonical paths always start with a single forward slash /.
Multiple consecutive slashes are treated as a single slash. For example, /a//b becomes /a/b.
A single dot . represents the current directory. These should be ignored. For example, /a/./b becomes /a/b.
Two consecutive dots .. represent moving up one directory. For example, /a/b/.. becomes /a. If you're at the root directory /, moving up .. does nothing.
Any other name (e.g., abc, folder, _file) represents a valid directory or file name. These are part of the path.
Trailing slashes are removed, except for the root directory. For example, /a/b/ becomes /a/b, but / remains /.



Split the path: Start by splitting the input string path by the / delimiter. This gives you an array or list of path components. 
For example, if the path is /a/b/../c/, splitting it yields ["", "a", "b", "..", "c", ""].


Initialize a stack: Create an empty stack (or a similar data structure like a deque in Python) to store the valid directory names.

Iterate through the components: Loop through the list of components from step 1. For each component:
    Ignore empty strings and single dots: If the component is an empty string ("") or a single dot (.), do nothing and continue to the next component. These don't affect the path's structure.
    Handle double dots: If the component is two dots (..), check if the stack is not empty. If it isn't, pop the last element from the stack. This simulates moving up one directory.
    Push valid names: If the component is any other valid name (e.g., abc, folder), push it onto the stack.

Reconstruct the path: After iterating through all components, the stack will contain all the valid directory names in order. Now, join these names with a / and prepend a / to form the final canonical path.
If the stack is empty after the process (e.g., the path was . or /../), the simplified path is just /.
Otherwise, the final path is / followed by all the elements in the stack joined by /.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for current in path :
            if current == "..":
                if stack :
                    stack.pop()
            elif current == '.' or current == "":
                continue 
            else :
                stack.append(current)
        
        result = "/" + "/".join(stack)

        return result