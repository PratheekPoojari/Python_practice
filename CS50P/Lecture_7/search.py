import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): 
    print("Valid")      # re.search(pattern, string, flag = 0), 'r' -> helps in the use of '\', by representing the   
                        # string as a 'raw string'; . -> any character except a newline; * -> 0 or more repetitions;
else:                   # + -> 1 or more repetitions; ? -> 0 or 1 repetition; {m} -> 'm' repetitions; {m, n} -> 'm 
    print("Invalid")    # to n' repetitions, where 'm' is the minimum and 'n' is the maximum. '^' -> matches the start of the string; 
                        #'$' -> matches the end of the string, just before the '\n' character; '[]' -> set of characters; 
                        # '[^]' -> complementing the set(anything except those values); '\w' -> refers to any word character(a-z, A-Z, 0-9, _);
                        # '\W' -> complement of '\w'; '\d' -> decimaal digit(0-9); '\D' -> complement of '\d'; '\s' -> whitespace character; 
                        # '\S' -> complement of '\s'; (A|B) -> either A or B; (.....) -> a group; (?:) -> non-capturing version.
                        # "flags" -> re.IGNORECASE, re.MULTILINE, re.DOTALL -> makes it so that '.' covers '\n' as well.
