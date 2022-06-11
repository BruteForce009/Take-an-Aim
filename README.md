## Overview
This web application records username, tracks scores and updates leaderboard. It has been developed primarily to support another project: a <a href="https://github.com/BruteForce009/vision-game-tracker">computer vision based game</a>.

### Database creation 
<hr/>
In the terminal enter the following commands:
'''
python <br>
from app import db
db.create_all()
db.create_all()
from models import Task
from datetime import datetime
'''

#### To add a sample task: <hr>
'''
t1 = Task(username="abc", date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
db.session.add(t1)
db.session.commit()
'''

#### To view the tasks:
----------------------
'''
Task.query.all()
'''
