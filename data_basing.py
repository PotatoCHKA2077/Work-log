from data import db_session
from data.users import User
from data.jobs import Jobs


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    db_sess = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Weir"
    user.name = "Andy"
    user.age = 30
    user.position = "astrogeologist"
    user.speciality = "astrogeologist"
    user.address = "module_2"
    user.email = "andy_weir@mars.org"
    user.hashed_password = "geolog"
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Sanders"
    user.name = "Teddy"
    user.age = 27
    user.position = "engineer"
    user.speciality = "cyberengineer"
    user.address = "module_2"
    user.email = "sanders_teddyn@mars.org"
    user.hashed_password = "engnr"
    db_sess.add(user)
    db_sess.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess.add(job)
    db_sess.commit()

    job = Jobs()
    job.team_leader = 2
    job.job = 'exploration of mineral resources'
    job.work_size = 15
    job.collaborators = '4, 3'
    job.is_finished = False
    db_sess.add(job)
    db_sess.commit()

    job = Jobs()
    job.team_leader = 3
    job.job = 'development of a management system'
    job.work_size = 25
    job.collaborators = '5'
    job.is_finished = False
    db_sess.add(job)
    db_sess.commit()


main()
