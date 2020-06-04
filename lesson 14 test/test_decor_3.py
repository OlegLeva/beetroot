open("logfile.txt", "w").close()

def file_in(file_name):
    def upper_list(func):
        def wraper(*args, **kwargs):
            l_up = (str(func(*args, **kwargs))).lower().title()
            with open(file_name, "a") as fn:
                fn.write(l_up + "\n")
            return l_up
        return wraper
    return upper_list

@file_in("logfile.txt")
def list_str(s):
    return sorted(s)

list_str(["maSha", "dRon", "leVA"])