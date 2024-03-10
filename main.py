from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/', methods=['GET'])
def job_list():
    # Если база данных осутствует, то перед запуском данного кода необходимо запустить программу "data_basing.py"
    db_session.global_init("db/mars_explorer.sqlite")
    db_sess = db_session.create_session()
    jobs = []
    for j in db_sess.query(Jobs).all():
        job = {
            'title': f'{j.job}'.capitalize(),
            'leader': f'{db_sess.query(User).filter(User.id == j.team_leader).first().surname} {
                db_sess.query(User).filter(User.id == j.team_leader).first().name}',
            'duration': f'{j.work_size} hours',
            'collaborators': j.collaborators,
            'is_finished': j.is_finished
        }
        jobs.append(job)
    return render_template('index.html', jobs=jobs)


if __name__ == '__main__':
    main()
