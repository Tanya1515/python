from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    usertype = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128))
    jobs = db.relationship('Jobs', backref='job_applier', lazy=True)
    applications = db.relationship('Application', backref='application_submiter', lazy=True)

    def __repr__(self):
        return f"User('{self.id}', '{self.usertype}', '{self.email}')"