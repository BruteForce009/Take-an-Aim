--- Overview ---

This web application records username, tracks scores and updates leaderboard. It has been developed primarily to support another project: a <a href="https://github.com/BruteForce009/vision-game-tracker" class="abt-links">computer vision based game</a>.


--- Database creation ---

In the terminal enter the following commands:

$ python <br>
$ from app import db <br>
$ db.create_all() <br>
$ db.create_all() <br>
$ from models import Task <br>
$ from datetime import datetime <br>

To add a sample task:

$ t1 = Task(username="abc", date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')) <br>
$ db.session.add(t1) <br>
$ db.session.commit() <br>

To view the tasks:

$ Task.query.all() <br>
