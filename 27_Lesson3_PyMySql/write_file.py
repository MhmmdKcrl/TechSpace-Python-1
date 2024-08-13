import pymysql
from typing import List


# Connect to the database
connection = pymysql.connect(   
    host = 'localhost',
    user = 'root',
    password='12345',
    db='TechSpace',
    port = 3307,
    charset = 'utf8mb4', 
    # cursorclass= pymysql.cursors.DictCursor 
)


def get_all_blogs():
        with connection.cursor() as cursor:
            sql = "SELECT * FROM TechSpace.Blogs;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    # print(get_all_blogs())


def write_to_file(blog_list: List) -> None:
    with open('blog_list.txt', 'w') as file:
        for blog in blog_list:
            for key, value in blog.items():
                file.write(f"{key}: {value}\n")
            file.write("-------------------------\n")
            

# write_to_file(get_all_blogs())