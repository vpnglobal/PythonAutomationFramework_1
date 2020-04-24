class HomePage ():

    # create constructors. This is function that will always be called when ever you will create object for class
    def __init__(self, driver):
        self.driver = driver
    # create locators/Objects
        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"

    # Create function or action methods
    def click_welcome(self):
        self.driver.find_element_by_id ( self.welcome_link_id ).click ()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()
