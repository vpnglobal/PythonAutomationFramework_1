#create class
class LoginPage():
#create constructors. This is function that will always be called when ever you will create object for class
    def __init__(self,driver):
        self.driver = driver
    #create locators/Objects
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    #Create function or action methonds
    def enter_username(self,username):
        self.driver.find_element_by_id ( self.username_textbox_id ).clear()
        self.driver.find_element_by_id ( self.username_textbox_id ).send_keys ( username )
        
    def enter_password(self,password):
        self.driver.find_element_by_id ( self.password_textbox_id).clear()
        self.driver.find_element_by_id ( self.password_textbox_id ).send_keys ( password )

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()