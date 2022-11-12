import re

def it_is_simple_assignment(word,line):
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
    # eliminates triple quotation
    for x in re.findall(r"'''(.*?)'''",source):
        source = source.replace(f"'''{x}'''","")
    for x in re.findall(r'"""(.*?)"""', source):
        source = source.replace(f'"""{x}"""', "")
    # eliminates double equals
    source = source.replace("==","")
    # disable multiline
    source = source.replace("\\\n"," ")
    # disable >= or <=
    source = source.replace("<="," ")
    source = source.replace(">="," ")

    results = []
    nested_function_level = 0
    for liner in source.split('\n'):
        liner = liner.strip()
        for line in liner.split(":"):

            # get a dictionary with the search result of every target var names in the sentence, if it's not none
            lookup_dict = {word: re.search(f'\\b{word}\\b', line)
                        for word in target_var_names if re.search(f'\\b{word}\\b', line)}
        
            # It will loop everyone of these results and pass them through some functions. from simple to complex. if any function returns true, it will add the word to the resutls, and eliminate it from the lookup_dictionary
            for word, result in lookup_dict.items():
                if word in results:
                    continue

                # FUNCION PARA ELIMINIAR CADENAS DE TEXTO
                for x in re.findall(r'"(.*?)"', line):
                    line = line.replace(f'"{x}"', '""')
                for x in re.findall(r"'(.*?)'", line):
                    line = line.replace(f"'{x}'", "''")

                # FUNCION PARA CHEQUEAR ASIGNACION SIMPLE y con comas
                if it_is_simple_assignment(word, line.strip()):
                    results.append(word)
                    continue
            
                # FUNCION PARA CHEQUEAR ASIGNACION EN LOS DEFS
                if it_is_function_assignment(word,line.strip()):
                    results.append(word)
                    continue

                # FUNCION PARA CHEQUEAR ASIGNACION EN LAS CLASS
                if it_is_class_assignment(word, line.strip()):
                    results.append(word)
                    continue

                

            [lookup_dict.pop(word) for word in results if word in lookup_dict.keys()]
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
        for filepath in sys.argv:
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
    