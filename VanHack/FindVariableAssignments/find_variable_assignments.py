import re

def it_is_simple_assignment(word: str,line: str) -> bool:
    """
        This functions receives a function name as a string and
        a one-line string and check if there is not a 
        simple overwritten python declaration
        **Line must be cleaned before entering this function
        Example:
            Input:
                word: "str"
                line: "str = new_weird_function
            Output: True
    """
    if not "=" in line:
        return False

    splited = line.split("=")
    if len(splited) <= 1:
        return False
    for part in splited[:-1]:
        if re.search(f'\\b{word}\\b',part):
            return True
    return False

def it_is_function_assignment(word,line):
    """
        This functions receives a line that begins with word 'def'
        and check if it is not using one of the builtins names.
        **Line must be cleaned before entering this function

        Example:
            Input:
                word: "str"
                line: "def str():
            Output: True
            Input:
                word: "str"
                line: "def str_but_different():
            Output: False
    """
    if line[:3] == "def":
        line = line[3:]
        line_list = line.split("(")
        if line_list[0].strip() == word:
            return True
        line = line.replace(" ","")
        first = line.find("(")
        if first > 0:
            parameters = line[first+1:-1].split(',')
            for param in parameters:
                if not "=" in param:
                    if re.search(f'\\b{word}\\b', line):
                        return True
                else:
                    if re.search(f'\\b{word}\\b', line.split('=')[0]):
                        return True
        else:
            return False

    else:
        return False

def it_is_class_assignment(word, line):
    """
        This functions receives a line that begins with word 'class'
        and check if it is not using one of the builtins names.
        **Line must be cleaned before entering this function

        Example:
            Input:
                word: "str"
                line: "class str:
            Output: True
            Input:
                word: "str"
                line: "class str_but_different:
            Output: False
    """
    if line[:5] == "class":
        line = line[5:]
        line_list = line.split("(")
        if line_list[0].strip() == word:
            return True
        else:
            return False
    else:
        return False

def find_variable_assignments(source, target_var_names):
    # eliminates triple quotation complete comment sections (FIXED)
    for x in re.findall(r"'{3}([\s\S]*?)'{3}",source):
        source = source.replace(f"'''{x}'''","")
    for x in re.findall(r'"{3}([\s\S]*?)"{3}', source):
        source = source.replace(f'"""{x}"""', "")

    # eliminates double equals so we not confuse them with variable assignment
    source = source.replace("==","")
    # disable multiline - we don't want multines. THIS IS NOT CORRECT
    # source = source.replace("\\\n"," ")
    # disable >= or <= so we not confuse them with simple '=' variable assignment
    source = source.replace("<="," ")
    source = source.replace(">="," ")

    results = []

    if re.findall("eval", source):
        results.append("eval")
    if re.findall("exec", source):
        results.append("exec")

    nested_function_level = 0
    for liner in source.split('\n'):
        liner = liner.strip()
        # It is posible to define after ':' -> Ex: "def hi(): str = not_str"
        for line in liner.split(":"):

            # get a dictionary with the search result of every target var names in the sentence, if it's not none
            lookup_dict = {word: re.search(f'\\b{word}\\b', line)
                        for word in target_var_names if re.search(f'\\b{word}\\b', line)}
        
            # It will loop everyone of these results and pass them through some functions. from simple to complex. if any function returns true, it will add the word to the resutls, and eliminate it from the lookup_dictionary
            for word, result in lookup_dict.items():
                if word in results:
                    continue

                # This will destroy comments
                for x in re.findall(r'"(.*?)"', line):
                    line = line.replace(f'"{x}"', '""')
                for x in re.findall(r"'(.*?)'", line):
                    line = line.replace(f"'{x}'", "''")

                # Simple Assignment
                if it_is_simple_assignment(word, line.strip()):
                    results.append(word)
                    # print("ENTRA A it_is_simple_assignment")
                    continue
            
                # def assignments
                if it_is_function_assignment(word,line.strip()):
                    results.append(word)
                    # print("ENTRA A it_is_function_assignment")
                    continue

                # class assginment
                if it_is_class_assignment(word, line.strip()):
                    # print("ENTRA A it_is_class_assignment")
                    results.append(word)
                    continue

                

            [lookup_dict.pop(word) for word in results if word in lookup_dict.keys()]
    if "exec" in results or 'eval' in results:
        print("--------------\n    - BE CAREFUL! Analyze this code personally, because the functions 'eval' or 'exec' has been detected. This may be very dangerous\n------------------------------------------")
    return results

# This part is new.
if __name__ == "__main__":
    import sys
    import builtins
    description = """
This command will check your python code and let you know if there is any
re-declaration of python native functions.
Just pass all the files you want to check as parameters.

Example:
python find_variable_assignments file1.py file2.py test/*.py

"""
    args = sys.argv[1:]
    if not args or args[0] == "--help":
        print(description)
    else:
        targets = dir(builtins)
        print("Files to check:\n")
        for filepath in args:
            print(f"--- {filepath}:")
            try:
                with open(filepath,'r') as f:
                    file_as_string = f.read()
                results = find_variable_assignments(file_as_string,target_var_names=targets)
            except Exception as e:
                print("     Unexpected Error: {e}")
            else:
                if not results:
                    print("    - Success! The file has not overwritten builtins functions.")
                else:
                    print(f"    - Warning! The file has overwritten the next buitlins functions: {', '.join(results)}")
                print("\n")
    