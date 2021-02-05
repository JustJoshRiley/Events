"""Create database models to represent tables."""
from events_app import db
import enum
from sqlalchemy.orm import backref



# TODO: Create a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(60), nullable=False)
    events_attending = db.relationship('Event', secondary='guest_event_table', back_populates='guests')

# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)

class Event_TYPE(enum.IntEnum):
    PARTY = 1,
    STUDY = 2,
    NETWORKING = 3,
    ETC = 4,

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date_and_time = db.Column(db.DateTime)
    guests = db.relationship('Guest', secondary='guest_event_table', back_populates='events_attending')
    event_type = db.Column(db.Enum(Event_TYPE))


guest_event_table = db.Table('guest_event_table',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'))
)