from . import db
from datetime import datetime
import uuid

class Groups(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    groupId = db.Column(db.String(250), default=uuid.uuid1(), nullable=False, unique=True)
    groupName = db.Column(db.String(150), nullable=False, unique=True)
    admin = db.Column(db.JSON, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))

    def __init__(self, groupName, admin):
        self.groupName = groupName
        self.admin = admin

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            'groupId': self.groupId,
            'groupName': self.groupName,
            'admin': self.admin,
            'createdAt': self.createdAt.isoformat() if self.created_at else None,
        }
