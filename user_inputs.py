from validate_email import validate_email

VALID_COLORS = ["red", "green", "orange", "blue"]

class UserInputs:
    """User inputs"""

    def __init__(self, name, year, email, color):
        "create user input object with name, email, year, and color"
        self.name = name
        self.year = year
        self.email = email
        self.color = color
        self.valid_colors = VALID_COLORS

    def __repr__(self):
        return f"<UserInputs {self.name} {self.year} {self.email} {self.color}>"

    def serialize(self):
        return {
            'name' : self.name,
            'year' : self.year,
            'email' : self.email,
            'color' : self.color
        }
    
    def validate_color(self):
        if self.color == "":
            return "This field is required"
        elif self.color not in self.valid_colors:
            return "Invalid value, must be one of: red, green, orange, blue."
        else:
            return True

    def validate_year(self):
        if self.year == "":
            return "This field is required"
        try:
            int_val = int(self.year)  
            if (int_val >= 1900 and int_val <= 2000 )== False:
                return "Invalid value, must be a number between 1900 and 2000 (inclusive)"
            # elif (self.year)) != int:
            #     return "Invalid value, must be a number"
            else:
                return True
        except:
            return "Invalid value, must be a number"

        if self.year != "" and (int(self.year) >= 1900 and int(self.year) <= 2000 ) == True:
            return True
        
        
    def validate_email(self):
        if self.email == "":
            return "This field is required"
        elif validate_email(self.email) == False:
            return "Invalid email"
        else:
            return True

    def validate_name(self):
        if self.name == "":
            return "This field is required"
        else:
            return True


def error_response(inputs):

    error_response = {"errors" : {}}

    color_validation = inputs.validate_color()
    if color_validation != True:
        error_response["errors"]["color"] = inputs.validate_color()
    
    year_validation = inputs.validate_year()
    if year_validation != True:
        error_response["errors"]["year"] = inputs.validate_year()

    email_validation = inputs.validate_email()
    if email_validation != True:
        error_response["errors"]["email"] = inputs.validate_email()

    name_validation = inputs.validate_name()
    if name_validation != True:
        error_response["errors"]["name"] = inputs.validate_name()

    return error_response
