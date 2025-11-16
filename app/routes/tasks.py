from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Task

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@tasks_bp.route("/")
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("tasks.html", tasks=tasks)


@tasks_bp.route("/add", methods=["POST"])
@login_required
def add_task():
    title = request.form["title"]
    new_task = Task(title=title, user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()
    flash("Task added successfully.", "success")
    return redirect(url_for("tasks.index"))


@tasks_bp.route("/toggle/<int:id>", methods=["POST"])
@login_required
def toggle(id):
    task = Task.query.get(id)
    if task and task.user_id == current_user.id:
        if task.status == "Pending":
            task.status = "In Progress"
        elif task.status == "In Progress":
            task.status = "Done"
        else:
            task.status = "Pending"
        db.session.commit()
        flash("Task status updated.", "info")
    return redirect(url_for("tasks.index")) 



@tasks_bp.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete(id):
    task = Task.query.get(id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted.", "info")
    return redirect(url_for("tasks.index"))



@tasks_bp.route("/clear", methods=["POST"])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash("All tasks cleared!", "info")
    return redirect(url_for("tasks.index"))
