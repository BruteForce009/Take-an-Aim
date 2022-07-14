## Overview
This web application records username, tracks scores and updates leaderboard. It has been developed primarily to support another project: a <a href="https://github.com/BruteForce009/vision-game-tracker">computer vision based game setup</a>.

## Database creation
In the terminal enter the following commands:
```
python
from app import db
db.create_all()
```

#### To add a sample task:
```
from models import Task
from datetime import datetime
task_1 = Task(username="user_1", score=60, date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
db.session.add(task_1)
db.session.commit()
```

#### To view the tasks:
```
Task.query.all()
```

## To run the app
```
python3 run.py
```
