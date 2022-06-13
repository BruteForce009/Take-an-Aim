from app import app, db
from flask import render_template, url_for, flash, redirect, get_flashed_messages
from gtts import gTTS
from datetime import datetime
import models
import forms
import random
import os


speak='Game Over! Your Score is'
language='en'


@app.route('/', methods=['GET', 'POST'])
@app.route('/play', methods=['GET', 'POST'])
def play():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        rand_score=random.randint(0, 100)
        task = models.Task(username=form.username.data, score=rand_score, date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        db.session.add(task)
        db.session.commit()
        gTTS(text=speak+f'{rand_score}', lang=language, slow=True).save("temp.mp3")
        os.system("temp.mp3")
        os.remove("temp.mp3")
        flash("Let's Play")
        return redirect(url_for('leaderboard'))
    return render_template('play.html', form=form)


@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    tasks = models.Task.query.order_by(models.Task.score.desc()).all()
    return render_template('leaderboard.html', tasks=tasks)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    form = forms.DeleteTaskForm()
    task = models.Task.query.get(task_id)
    if task:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(task)
                db.session.commit()
                flash('Task deleted')
            return redirect(url_for('leaderboard'))
        return render_template('delete.html', form=form, task_id=task_id, username=task.username)
    flash(f'Task with id {task_id} does not exit')
    return redirect(url_for('leaderboard'))
