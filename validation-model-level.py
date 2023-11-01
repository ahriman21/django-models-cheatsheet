# to validate data input, you can implement it in model-level validation in order to check what data is valid to be saved in tables.
# 1. create your validation function 
# 2. specify 'validators' attribute in your desired field. after that, put name of the function in that as a list
# EXAMPLE :

def validate_usernames(value):
  forbiden = ['admin', 'superuser']
  for i in forbiden:
    if i == value
      raise ValidationError("This username is not allowed.")


class User(models.Model):
  username = CharField(validators=[validate_username])
