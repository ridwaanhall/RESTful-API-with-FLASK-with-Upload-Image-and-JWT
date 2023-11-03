from app import db


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    judul = db.Column(db.VARCHAR(50), nullable=False)
    pathname = db.Column(db.VARCHAR(100), nullable=False)
    
    def __repr__(self):
        return '<Images {}>'.format(self.name)