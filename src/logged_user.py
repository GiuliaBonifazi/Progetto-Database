user = {"userId" : None, "name": "", "surname": "", "admin" : False, "order": []}

def get_user():
    global user
    return user

def reset_logged_user():
    global user
    user = user = {"userId" : 1, "name": "", "surname": "", "admin" : False, "order": []}