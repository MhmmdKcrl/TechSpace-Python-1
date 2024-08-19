from extensions import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.Boolean, default=True)
    image = db.Column(db.Text, nullable=True)
    new_field = db.Column(db.String(100), nullable=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f"<{self.title}>"
    
    
    def __init__(self, title, content, image):
        self.title = title
        self.content = content
        self.image = image

    def save(self):
        db.session.add(self)
        db.session.commit()
    
