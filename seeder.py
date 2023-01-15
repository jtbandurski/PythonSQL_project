import sqlite3
import os.path
from random import choice, randint

# users_list
first_names = ['Kuba','Hamed','Ahmed','Lilly','Ewa','Susan','Tom']
last_names = ['Kowalski','Malik', 'Omar', 'Smith', 'Majewska', 'Curry','Scott']
user_names = ['rockyBalboa','toby432','magician00','lilPad','elevatorGirl123','thatNASUS','IamTommy']
occupation = ['Student', 'Self-employed', 'Employee', 'Manager', 'Other']
password = ['admin1','admin2','admin3','martin23','gofrykocham!','marathon2010', 'whiskeyandcigars']
email = []
for f, l in zip(first_names, last_names):
    email.append(f + "." + l + "@gmail.com")

users_list = []

for i in range(len(first_names)):
    users_list.append((i, user_names[i],first_names[i],last_names[i],
                        choice(occupation),email[i],password[i]))

# habbits
habbits = []
user_ids = list(range(7))
habbit_type = [0,1]
success_activity = ['run', 'study', 'exersice', 'read books', 'socialise']
success_range = ['no more than', 'no less than', 'exactly']

i=0
for user_id in user_ids:
    number_of_habbits = randint(1,6)
    for k in range(number_of_habbits):
        h_name = 'Habbit' + str(k+1)
        h_desc = 'Description of habbit'
        h_days_target = randint(1,7)
        h_type = choice(habbit_type)
        if h_type == 0:
            h_activity = '0'
            h_range = "0"
            h_amount = 0
            h_unit = "0"
        else:
            h_activity = choice(success_activity)
            h_range = choice(success_range)
            h_amount = randint(1,20)
            if h_activity == "run":
                h_unit = 'km'
            else:
                h_unit ='hours'

        habbits.append((i, user_id, h_type, h_desc, h_name, h_days_target, 
                        h_activity, h_range, h_amount, h_unit))
        i=i+1

# habbits_tracker
habbits_tracker = []
# habbits_id = list(range(len(habbits)))
habbit_ids = list(range(29))
habbit_types = [1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,0,1]
dates = ['2023-01-10 18:47', '2023-01-11 15:21', '2023-01-12 09:01', '2023-01-13 12:21', '2023-01-14 22:43']
i=0
for habbit_id in habbit_ids:
    number_of_entries = randint(1,5)
    for k in range(number_of_entries):
        date = choice(dates)
        h_type = habbit_types[habbit_id]
        if h_type ==0:
            yes_no_value=choice([0,1])
            h_amount_value=None
        else:
            yes_no_value=None
            h_amount_value=randint(1,8)
        
        habbits_tracker.append((i, habbit_id, h_type, date, yes_no_value, h_amount_value))
        i=i+1
    
# posts
posts = []
user_ids = list(range(7))
dates = ['2023-01-10 18:47', '2023-01-11 15:21', '2023-01-12 09:01', '2023-01-13 12:21', '2023-01-14 22:43']
contents = ["Look what I've achieved!!!", 'Proud of myself :)','You can make it to ;))', 'Whoaaah so exhausted - worth it!']

i=0
for user_id in user_ids:
    number_of_posts = randint(0,3)
    for k in range(number_of_posts):
        publish_date = choice(dates)
        content = choice(contents)
        posts.append((i,user_id, publish_date, content))
        i=i+1

# comments
comments = []
user_ids = list(range(7))
post_ids = list(range(10))
comments_list = ['Keep it up!', 'Well done', 'Jealous','NICE :D']

i=0
for post_id in post_ids:
    number_of_comments = randint(0,3)
    for k in range(number_of_comments):
        publish_date = choice(dates)
        content = choice(comments_list)
        comments.append((i,post_id,user_id,publish_date,content))
        i=i+1

# comments
likes = []
user_ids = list(range(7))
post_ids = list(range(10))

i=0
for post_id in post_ids:
    number_of_likes = randint(0,3)
    for k in range(number_of_likes):
        publish_date = choice(dates)
        likes.append((i,post_id,user_id,publish_date,1))
        i=i+1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # sql query
    cursor.executemany("INSERT INTO users_list VALUES (?,?,?,?,?,?,?)",users_list)
    cursor.executemany("INSERT INTO habbits VALUES (?,?,?,?,?,?,?,?,?,?)", habbits)
    cursor.executemany("INSERT INTO habbits_tracker VALUES (?,?,?,?,?,?)", habbits_tracker)
    cursor.executemany("INSERT INTO posts VALUES (?,?,?,?)", posts)
    cursor.executemany("INSERT INTO comments VALUES (?,?,?,?,?)", comments)
    cursor.executemany("INSERT INTO likes VALUES (?,?,?,?,?)", likes)

    # print total number of changed rows
    print("number of affected rows: {0}".format(conn.total_changes))

    # commit
    conn.commit()

# closing connection
conn.close()