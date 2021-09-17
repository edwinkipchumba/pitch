from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

# pictch form section
class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    category = SelectField(u'Pitch Category', choices=[('life', 'life'), ('coding', 'coding'), ('funny', 'funny')])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')

# comment form section
class CommentForm(FlaskForm):
    
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')

# update profile

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')