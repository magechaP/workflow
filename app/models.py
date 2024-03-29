rewel
# from flask_login import UserMixin
class Management:
    all_comments =[]
    '''
    Management class that returns Management Objects
    '''
    def __init__(self,title,department,description):
        self.title =title
        self.department=department
        self.description=description
    def save_description(self):
        Management.all_comments.append(self)
    @classmethod
    def clear_comments(cls):
        Management.all_comments.clear()
    @classmethod
    def get_comments(cls):
        response=[]
        for comment in cls.all_comments:

            response.append(comment)

        return response
class Finance:
    all_comments =[]
    '''
    Management class that returns Management Objects
    '''
    def __init__(self,title,description):
        self.title =title        
        self.description=description
    def save_description(self):
        Finance.all_comments.append(self)
    @classmethod
    def clear_comments(cls):
        Finance.all_comments.clear()
    @classmethod
    def get_comments(cls):
        response=[]
        for comment in cls.all_comments:

            response.append(comment)

        return response
class Hr:
    all_comments =[]
    '''
    Management class that returns Management Objects
    '''
    def __init__(self,title,description):
        self.title =title        
        self.description=description
    def save_description(self):
        Hr.all_comments.append(self)
    @classmethod
    def clear_comments(cls):
        Hr.all_comments.clear()
    @classmethod
    def get_comments(cls):
        response=[]
        for comment in cls.all_comments:

            response.append(comment)

        return response
class Maintenance:
    all_comments =[]
    '''
    Management class that returns Management Objects
    '''
    def __init__(self,title,description):
        self.title =title        
        self.description=description
    def save_description(self):
        Maintenance.all_comments.append(self)
    @classmethod
    def clear_comments(cls):
        Maintenance.all_comments.clear()
    @classmethod
    def get_comments(cls):
        response=[]
        for comment in cls.all_comments:

            response.append(comment)

        return response
=======
class User(UserMixin,db.model):
    __tablename__= 'users'

    id = db.Column(db.integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,d.ForeignKey('role.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    password_hash = db.Column(db.String(255))
    photos = db.relationship('PhotoProfile',backref = 'user' ,lazy="dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.name}'            
 authentication
