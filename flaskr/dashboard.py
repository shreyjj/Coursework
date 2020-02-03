from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('dashboard', __name__)


@bp.route('/')
@login_required
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, stock, quantity, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('dashboard/index.html', posts=posts)


@bp.route('/portfolio', methods=("GET", "POST"))
@login_required
def portfolio():
    return render_template('dashboard/portfolio.html')


@bp.route('/research', methods=("GET", "POST"))
@login_required
def research():
    return render_template('dashboard/research.html')


@bp.route('/add-new-stock', methods=('GET', 'POST'))
@login_required
def new_stock():
    if request.method == 'POST':
        stock = request.form['stock']
        quantity = request.form['quantity']
        error = None

        if not stock:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (stock, quantity, author_id)'
                ' VALUES (?, ?, ?)',
                (stock, quantity, g.user['id'])
            )
            db.commit()
            return redirect(url_for('dashboard.research'))
    return render_template('dashboard/new_stock.html')