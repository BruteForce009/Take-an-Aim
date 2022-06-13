from app import db
import datetime


class MyDateTime(db.TypeDecorator):
    impl = db.DateTime

    def process_bind_param(self, value, dialect):
        if type(value) is str:
            return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return value


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    score = db.Column(db.Integer, default=0)
    date = db.Column(MyDateTime, default=datetime.datetime.now, nullable=False)
    # date = db.Column(db.datetime, nullable=False)

    def __repr__(self):
        return f'{self.username} has scored {self.score} on {self.date}'


'''
--- Terminal commands ---
python3/python
from app import db
db.create_all()
from models import Task
from datetime import datetime
t1 = Task(username="abc", date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
db.session.add(t1)
db.session.commit()
t2 = Task(username="def", date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
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