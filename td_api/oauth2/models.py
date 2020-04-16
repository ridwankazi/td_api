from application.create_app import db

class OauthTokens(db.Model):

    __tablename__ = 'oauth_tokens'
    id = db.Column(db.Integer,
                   primary_key=True)
    access_token = db.Column(db.String(),
                         index=False,
                         unique=True,
                         nullable=False)
    refresh_token = db.Column(db.String(),
                      index=True,
                      unique=True,
                      nullable=False)
    last_set_datetime = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
