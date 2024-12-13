from flask import request, jsonify
from datetime import datetime

from .models import Groups
from . import db

def register_routes(app):

    @app.route('/groups', methods=['POST'])
    def group_post():
        data = request.json
        group = Groups (
            groupName=data['groupName'],
            admin={
                'name': data['admin']['name'],
                'email': data['admin']['email']
            }
        )
        db.session.add(group)
        db.session.commit()
        return jsonify({
            'groupId': group.groupId,
            'groupName': group.groupName,
            'admin': group.admin,
            'createdAt': group.createdAt.isoformat() if group.createdAt else None
        }), 201
