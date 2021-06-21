from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# from flask_app.models.ninja import ### other models ###

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_validation_schema').query_db(query)
        emails = []
        for email in results:
            emails.append(Email(email))
        return emails


    @classmethod
    def insert(cls, data):
        query = "INSERT INTO emails (name,email, created_at, updated_at) VALUES ( %(name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('email_validation_schema').query_db(query, data)


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM emails WHERE id=%(id)s"
        return connectToMySQL('email_validation_schema').query_db(query,data)


    @staticmethod  # make sure no duplicate email # has email structure
    def validate_user(email):
        is_valid = True # the keys must match the request.form keys or NAME in the HTML
        if len(email['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(email['email']) < 3:
            flash("location must be at least 3 characters.")
            is_valid = False
        return is_valid


    @staticmethod
    def validate_user(email):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid