import pymysql

# Connect to the database
connection = pymysql.connect(   
    host = 'localhost',
    user = 'root',
    password='12345',
    db='TechSpace',
    port = 3307,
    charset = 'utf8mb4', 
    cursorclass= pymysql.cursors.DictCursor 
)



# create a table
def create_blog():
    with connection:
        with connection.cursor() as cursor:
            sql = """
            CREATE TABLE if not exists TechSpace.Blogs2(
            id int primary key auto_increment,
            title varchar(100),
            author_name varchar(100)
            );
            """
            cursor.execute(sql)
        connection.commit()

# create_blog()

# insert data into the table
def insert_into_blog(blog_name, author):
    with connection:
        with connection.cursor() as cursor:
            sql = f"INSERT into TechSpace.Blogs(title, author_name) Value(%s, %s);"
            cursor.execute(sql, (blog_name, author))
        connection.commit()

# insert_into_blog('Blog5', 'Author1')






# get all the blogs
def get_blogs():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM TechSpace.Blogs;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

# for _ in get_blogs():
#     print(_)
print(get_blogs())





# update a blog
def update_blog(id, title):
    with connection:
        with connection.cursor() as cursor:
            sql = f"""UPDATE TechSpace.Blogs 
                SET title = %s 
                WHERE id = %s;"""
            cursor.execute(sql, (title, id))
        connection.commit()

# update_blog(3, 'Python Blog')




# get a single blog
def get_single_blog(id):
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM TechSpace.Blogs WHERE id = %s; "
            cursor.execute(sql, (id))
            result = cursor.fetchone()
        return result
        
# print(get_single_blog(3))
        




# filter by blog name
def filter_by_name(title):
    with connection.cursor() as cursor:
        sql = f"""SELECT * FROM TechSpace.Blogs 
        WHERE title like "%{title}%"; """
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
# print(filter_by_name('python'))




# delete a blog
def delete_blog(id):
    with connection:
        with connection.cursor() as cursor: 
            sql = f"DELETE FROM TechSpace.Blogs WHERE id = %s;"
            cursor.execute(sql, (id))
        connection.commit()


# delete_blog(14)


