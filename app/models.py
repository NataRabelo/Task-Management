from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), index=True, unique=True)
    description = db.Column(db.String(500))
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.title}>'
