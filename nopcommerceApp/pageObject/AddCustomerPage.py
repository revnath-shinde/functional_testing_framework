import time
from selenium.webdriver.common.by import By


class AddCustomer:

    # lnkuCustomer_menu_xpath="//a[@href='#']//span[contains(text(), 'customers')]"
    # lnkuCustomer_menu_xpath="// a[ @class ='nav-link active'] // p[text()=' Customers ']"
    lnkCustomer_menu_xpath = "//a[@class='nav-link active']"
    # lnkCustomer_menuitem_xpath="//span[@class='menu-item-title'][contains(text(),'Customers')]"
    lnkCustomer_menuitem_linktext="Customers"
    #"//a[@class='nav-link active']//p[text()=' Customers ']"
    expbtn_xpath="//*[@class='btn btn-success']"
    btnAddnew_xpath="//a[@class='btn btn-primary']"
    txtEmail_xpath="//*[@class='form-control text-box single-line']"
    txtPassword_xpath="//*[@id='Password']"
    txtfirstName_xpath="//*[@id='SearchFirstName']"
    txtlastName_xpath="//*[@name='SearchLastName']"
    # dropdown_xpath="//*[@id='SearchMonthOfBirth']"
    # rdbtn_xpath="//*[@id='Gender_Male']"
    # txtDob_xpath="//*[@id='DateOfBirth']"
    # txtCompanyName_xpath="//*[@id='Company']"
    # txtnewsletter_xpatg="//*[@type='search']"
    lstitemAdminstractor_xpath="//li[contains(text(), ''Administractors')]"
    lstitemForumModerato_xpath="//li[contains(text(), 'Forum Moderator')]"
    lstitemRegistred_xpath="//li[contains(text(), 'Registered'')]"
    lstitemGuests_xpath="//li[contains(text(), 'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(), 'Vendors')]"
    txtmanageVendor_xpath="//*[@class='select2-search__field']"
    txtaddcomment_xpath="//*[@id='AdminComment']"
    btnSave_xpath="//*[@class='btn btn-primary']"


    def __init__(self, driver):
        self.driver = driver


    def clickonCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickonCustomerItemMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkCustomer_menuitem_linktext).click()

    def clickonExportbtn(self):
        self.driver.find_element(By.XPATH, self.expbtn_xpath).click()

    def clickAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email ):
        self.driver.find_element(By.XPATH, self. txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self. txtPassword_xpath).send_Keys(password)

    def setFirstName(self, Fname):
        self.driver.find_element(By.XPATH, self.txtfirstName_xpath).send_keys(Fname)

    def setLirstName(self, Lname):
        self.driver.find_element(By.XPATH, self.txtlastName_xpath).send_keys(Lname)

    def setCustomerRole(self, role):
        self.driver.find_element(By.XPATH, lstitemAdminstractor_xpath).click()
        time.sleep(3)

    # if role =='Registered':
    #     self.listitem=self.driver.find_element(By.XPATH, self.lstitemAdminstractor_xpath)
    # else:
    #     self.listitem=self.driver.find_element(By.XPATH,self,lstitemGuests_xpath)
    # time.sleep(3)

    def clickbtnSave(self):
        self.driver.find_element(By.XPATH,  btnSave_xpath).click()

        #// span[contains(text(), 'Customers')]
