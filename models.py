from app import db



class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    Seeking_description = db.Column(db.String(250))
    
    shows = db.relationship('Show', backref='venue', lazy=True)
    
    def __repr__(self):
          return f'<Venus id={self.id}, name={self.name}, city={self.city}, state={self.state}>'

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    genres = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    
    website_link = db.Column(db.String(120))
    seeking_venue  = db.Column(db.Boolean, default=False)
    Seeking_description = db.Column(db.String(250))
    
    shows = db.relationship('Show', backref='artist', lazy=True)
    def __repr__(self):
          return f'<Artist id={self.id} name={self.name} phone={self.phone}>'

class Show(db.Model):
    __tablename__ ='Show'
    
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    
    artist_id = db.Column(db.Integer,db.ForeignKey('Artist.id'),nullable=False)
    venue_id = db.Column(db.Integer,db.ForeignKey('Venue.id'),nullable=False)
    
    def __repr__(self):
          return f'<Show id={self.id}, start_time={self.start_time}, artist_id={self.artist_id}, venue_id={self.venue_id}>'
      