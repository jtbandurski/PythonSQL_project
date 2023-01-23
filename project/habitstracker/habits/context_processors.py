from habits.views import *

def userName(request):
    
    if 'user_Name' not in session:
        user_name = ''
    else:
        user_name = session['user_Name']
    return {
        'username' :  user_name
    }