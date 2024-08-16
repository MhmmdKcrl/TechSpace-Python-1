from flask import Flask, request, render_template

app = Flask(__name__)
# app = Flask(__name__, template_folder='folder_name')
# app = Flask('app')

blog_list = [
        {
            "id":1,
        "title": "Blog 1",
        "content": "content 1",
        "author": "author 1",
        },
        {
            "id":2,
        "title": "Blog 2",
        "content": "content 2",
        "author": "author 2",
        },
        {
            "id":3,
        "title": "Blog 3",
        "content": "content 3",
        "author": "author 3",
        },
        {
            "id":4,
        "title": "Blog 4",
        "content": "content 4",
        "author": "author 4",
        }

    ]


@app.route('/')
@app.route('/home')
def index():
    page="Home"
    return render_template('index.html', page=page)


@app.route('/about/')
def about_page():
    page = "About"

    return render_template('about.html', page=page)

@app.route('/blogs/')
def blogs():
    page_name = "Blogs"

    context = {
        "blogs": blog_list,
        "page": page_name
    }
    return render_template('blog.html', **context)


@app.route('/blogs/<int:blog_id>')
def blog_detail(blog_id):
    # if blog_id >0 and blog_id <= len(blog_list):
    return blog_list[blog_id-1]
    # return "Blog not found"

# @app.route('/blogs/<string:blog_title>')
# def blog_detail_with_string(blog_title):
#     return f"Blog with title {blog_title}"


# @app.route('/blogs/<int:blog_id>')
# def blog_detail(blog_id):
#     # print(request.args, "------------------")
#     # request.args = {
#     #     "title": "Tech",
#     #     "content" : "Space"
#     # }
#     title = request.args.get('title')
#     content = request.args.get('content')
#     # title = request.args["title"]
#     if title and content:
#         return f"Blog with title {title}, content {content}"
#     return blog_list[blog_id-1]



if __name__ == '__main__':
    app.run(port=4000, debug=True, host='localhost')
