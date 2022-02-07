from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Advertisement','Advertisement'),('Interview','Interview'),('Product','Product'),('Technology','Technology')],validators=[DataRequired()])
    post = TextAreaField('Your Pitch', validators=[DataRequired()])
    submit = SubmitField('Submit Pitch')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [DataRequired()])
    submit = SubmitField('Save')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')