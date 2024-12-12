from flask import request, jsonify
from datetime import datetime

from .models import Groups

def register_routes(app):

    @app.route('/groups', methods=['POST'])
    def group_post():
        data = request.json
        return jsonify(group), 201
