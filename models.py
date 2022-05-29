from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.username} created on {self.date}'


'''
--- Terminal commands ---
python3/python
from app import db
db.create_all()
from models import Task
from datetime import datetime
t1 = Task(username="abc", date=datetime.utcnow())
db.session.add(t1)
db.session.commit()
t2 = Task(username="def", date=datetime.utcnow())
db.session.add(t2)
db.session.commit()
tasks = Task.query.all()
tasks
[ abc created on ***, def created on *** ]
'''
'''
<a href="{{ url_for('edit', task_id=task.id) }}" class="btn btn-primary">Edit</a>
<a href="{{ url_for('delete', task_id=task.id) }}" class="btn btn-danger">Delete</a>
'''