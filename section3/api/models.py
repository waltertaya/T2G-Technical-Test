from . import db
import datetime
import uuid

class Groups(db.Model):
    __tablename__ = 'groups'

    groupId = db.Column(db.Integer, primary_key=True, default=uuid.uuid1())
    groupName = db.Column(db.String(150), nullable=False)
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
