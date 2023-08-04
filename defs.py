import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import simpledialog

class ShiftScraper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.username = None
        self.password = None
        
    def get_credentials(self):   #with tkinter creates little window and asks for users username and password
        root = tk.Tk()
        root.withdraw()
        self.username = simpledialog.askstring("Input", "Enter your username:")
        self.password = simpledialog.askstring("Input", "Enter your password:", show="*")
        root.destroy()

    def login(self):
        self.driver.get("https://mcd.vuorolistat.fi/Default.aspx?ReturnUrl=/usershifts.aspx")  #opens finnish mcd shift website and logins into it

        try:
            self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(self.username)
            self.driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(self.password)
            self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
            self.driver.find_element(By.CSS_SELECTOR, 'input[value="<"]').click()   #input[value="?"] can be < if you want to add previus "listajakso" shifts
                                                                                    #nothing if now ongoing ones and > if if you want to add shifts in future
        except:
            print("ERROR: Sisäänkirjautuminen epäonnistui")

    def get_shifts(self):
        time.sleep(1)  #scrapes all shifts from website and returns list on 21 days where -1 value represents days where are no shifts
                        #and if there is any other value is timestamp of the shift

        try:
            all_shifts = self.driver.find_elements(By.CLASS_NAME, 'shifts')
        except:
            print("shifts not found")
            self.driver.quit()
            return None

        shift_list = []
        for week in all_shifts:
            try:
                days = week.find_elements(By.XPATH, ".//td")
                for shift in days:
                    try:
                        shift_list.append(shift.find_element(By.XPATH, ".//a").text)
                    except:
                        shift_list.append(-1)
            except:
                print("weeks not found")

        return shift_list

    def get_dates(self):
        time.sleep(1)       #scrapes all dates from website and returns list of them

        try:
            period = self.driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_cphMain_cphMain_wlblCurrentPeriod']").text
        except:
            print("start date no found")
            self.driver.quit()
            return None

        full_date = period.split(" - ")
        start_date = full_date[0]

        def next_20(start):
            date_format = "%d.%m.%Y"
            star_date_obj = datetime.strptime(start, date_format)
            next_20_list = [star_date_obj + timedelta(days=i) for i in range(21)]
            return [day.strftime(date_format) for day in next_20_list]

        days_list = next_20(start_date)

        return days_list
    
    def quit(self):  #method for closing website
        self.driver.quit()
    
    @staticmethod
    def change_format(date):   #changes date format
        date = datetime.strptime(date, "%d.%m.%Y")
        return date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    scraper = ShiftScraper()
    scraper.get_credentials()
    scraper.login()
    shifts = scraper.get_shifts()
    dates = scraper.get_dates()
    scraper.quit()
    
    print(shifts)
    print(dates)
