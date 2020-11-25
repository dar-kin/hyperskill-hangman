def check_email(string):
    if " " in string or "@" not in string or "." not in string[string.find("@") + 2:]:
        return False
    else:
        return True
