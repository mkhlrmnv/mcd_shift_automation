import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
import UI


class ShiftScraper:
    def __init__(self):  #opens selenium and right driver for it
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def login(self):  #logins in to a website
        self.driver.get(
            "https://mcd.vuorolistat.fi/Default.aspx?ReturnUrl=/usershifts.aspx")
        
        f = open("secrets.txt", "r+")
        user = f.readline()  #from secret file reads username, password and selecion
        passw = f.readline()
        minne = f.readline()

        try: 
            self.driver.find_element(  #inserts username
                By.CSS_SELECTOR, 'input[type="text"]').send_keys(user)
            self.driver.find_element( #inserts password
                By.CSS_SELECTOR, 'input[type="password"]').send_keys(passw)
            #self.driver.find_element(
                #By.XPATH, '//*[@id="wcmdLogin"]').click()
            
            match minne:  #depending what was selection clicks right button
                case "<": x_path = '//*[@id="wcmdPreviousPeriod"]'
                case "=": x_path = '//*[@id="aspnetForm"]/div[3]/table/tbody/tr/td[2]/div/div/div/button'
                case ">": x_path = '//*[@id="wcmdNextPeriod"]'
              
            self.driver.find_element(By.XPATH, x_path).click()
        except: #prints error if it accured 
            print("ERROR: Sisäänkirjautuminen epäonnistui")
            
        f.truncate(0)  #deletes username, password and selection from secret file
            

    def get_shifts(self):  # gets list of shifts
        time.sleep(1)

        try: #finds all elements with class name shifts
            all_shifts = self.driver.find_elements(By.CLASS_NAME, 'shifts')
        except:
            print("shifts not found")
            self.driver.quit()
            return None

        shift_list = []
        for week in all_shifts: #checks all above found elements for time stamps
            try:                # if there is time stamps saves it into a list if not puts -1 in to a list
                days = week.find_elements(By.XPATH, ".//td")
                for shift in days:
                    try:
                        shift_list.append(
                            shift.find_element(By.XPATH, ".//a").text)
                    except:
                        shift_list.append(-1)
            except:
                print("weeks not found") #prints error if accured

        return shift_list

    def get_dates(self):
        time.sleep(1)

        try:  #find starting date of shifts
            period = self.driver.find_element(
                By.XPATH, "//*[@id='ctl00_ctl00_cphMain_cphMain_wlblCurrentPeriod']").text
        except:
            print("start date no found")
            self.driver.quit()
            return None

        full_date = period.split(" - ")
        start_date = full_date[0]

        def next_20(start): #puts next 20 days after starting date in to a list
            date_format = "%d.%m.%Y"
            star_date_obj = datetime.strptime(start, date_format)
            next_20_list = [star_date_obj +
                            timedelta(days=i) for i in range(21)]
            return [day.strftime(date_format) for day in next_20_list]

        days_list = next_20(start_date)

        return days_list

    def quit(self):
        self.driver.quit()

    @staticmethod
    def change_format(date):  #changes date format from d.m.Y to Y-m-d
        date = datetime.strptime(date, "%d.%m.%Y")
        return date.strftime("%Y-%m-%d")


if __name__ == "__main__":
    scraper = ShiftScraper()
    ui = UI.RegistrationForm()
    ui.run()
    scraper.login()
    shifts = scraper.get_shifts()
    dates = scraper.get_dates()
    scraper.quit()

    print(shifts)
    print(dates)
