from selenium import webdriver


def __init__(self, env):
    self.driver = webdriver.Firefox()
    self.driver.maximize_window()

    if env == 'Staging':
        self.driver.get("https://")
    elif env == 'QE':
        self.driver.get("http://")
    else:
        print("Environment is not available", env)
        print("\n Supported Environments are Staging and QE")
        self.driver.quit()
        raise SystemExit("Program Exited")

    with open('config.json','r') as user_credentials:
            config = json.load(user_credentials)
    self.driver.find_element_by_id('username').send_keys(config['user']['name'])
    self.driver.find_element_by_id('password').send_keys(config['user']['password'])
    self.driver.find_element_by_id("signIn").click()
    try:
        self.driver.find_element_by_xpath('')
        print("Login Not successful")
        self.driver.quit()
        raise SystemExit("Program Exited")
    except NoSuchElementException:
        print("Login Successful")

        
def addnewlinearpackage(self, title, enddate_days_from_today):
    try:
        # Select Manage
        self.driver.find_element_by_xpath("").click()

        # Creating new Linear Package
        self.driver.find_element_by_id("linearpublishing").click()
        self.driver.find_element_by_id("linpub").click()
        self.driver.find_element_by_id("addLinearPackage").click()
        self.driver.find_element_by_id("linearpackageTitle").send_keys(title)
        self.driver.find_element_by_id('tempPackageId').send_keys(
            datetime.strftime(datetime.now(), '%Y%m%d%H%M'))
        self.driver.find_element_by_id("").click()

        start_time = self.driver.find_element_by_id('startDate')
        execute = start_time.find_element_by_xpath("")
        self.driver.execute_script("arguments[0].click();", execute)
        time.sleep(7)

        end_time = self.driver.find_element_by_id('endDate')
        end_time.find_element_by_xpath("").click()
        end_date = (datetime.now() + timedelta(days=enddate_days_from_today)).strftime('%m/%d/%Y')
        self.driver.find_element_by_xpath("*//td[@data-day='" + end_date + "']").click()
        time.sleep(7)

    except NoSuchElementException as exp:
        print(exp)
        self.driver.quit()
        raise SystemExit("Program Exited")

        
def addlinearservice(self, serviceId):
    try:
        self.driver.find_element_by_id("linearServiceSection").click()
        time.sleep(10)

        self.driver.find_element_by_id("publishLinearPackageBtn").click()
        time.sleep(30)

        self.driver.find_element_by_class_name("sorting_1")

        linear_service_found = False

        # Searching existing linear service
        if linear_service_found == False:

            try:# Search in first page
                self.driver.find_element_by_xpath("").click()

                if self.driver.find_element_by_link_text(serviceId).is_displayed():
                    self.driver.find_element_by_xpath("" + serviceId + "").click()
                    linear_service_found = True
                    print("Linear service found")

            except NoSuchElementException:
                print("No such Element found in page 1")

            try:

                while linear_service_found == False:  # loop to navigate to next page till finding the service ID

                    try:  # Search till last page is reached and next button is disabled

                        self.driver.find_element_by_xpath("")
                        print('No further Page available to search')
                        break

                    except NoSuchElementException:

                        try:
                            self.driver.find_element_by_xpath('').click()
                            if self.driver.find_element_by_link_text(serviceId).is_displayed():
                                # click the checkbox of Service ID
                                self.driver.find_element_by_xpath("" + serviceId + "").click()
                                linear_service_found = True
                                print("Linear Service found")
                                break

                        except NoSuchElementException:
                            print("No such Element found in current page")

            except NoSuchElementException:
                print("No such Element found")

            if linear_service_found == True:
                time.sleep(10)
                #Click on Save button
                self.driver.find_element_by_xpath('').click()
                time.sleep(10)

    except NoSuchElementException as exp:
        print(exp)
        self.driver.quit()
        raise SystemExit("Program Exited")

        
def publish(self):
    try:
        self.driver.find_element_by_xpath('//button[contains(text(), "Publish")]').click()
        time.sleep(5)

        self.driver.find_element_by_xpath('').click()
        time.sleep(10)

        try:
            self.driver.find_element_by_xpath('//*[@id="appSuccessMsg"]')
            print("Linear Package Published Successfully")
        except NoSuchElementException:
            print("Linear Package NOT PUBLISHED.. check the Error Message in Service console webpage")
            time.sleep(60)
            self.driver.quit()
            raise SystemExit("Program Exited")

    except NoSuchElementException as exp:
            print(exp)
            self.driver.quit()
            raise SystemExit("Program Exited")

            
def exit(self):
    print("Exiting.....")
    time.sleep(5)
    self.driver.quit()
    
