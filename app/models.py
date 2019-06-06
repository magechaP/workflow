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