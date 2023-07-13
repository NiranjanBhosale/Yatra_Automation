import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base import Base
from typing import List

class Flights_Page(Base):

    ############ ID ############
    nav_bar_flights_button = "booking_engine_flights"
    from_input_box = "BE_flight_origin_city"
    to_input_box = "BE_flight_arrival_city"
    depart_date_input_box = "BE_flight_origin_date"

    select_flight_offer = "{}_offer"
    flight_offer = {
        'student':'special_student',
        'army': 'armedforces',
        'senior': 'seniorcitizen'
    }

    ############ XPATH ############
    trip_way_button = "//a[contains(text(),'{}')]"
    way = {
        'one way': 'One Way',
        'round trip': 'Round Trip',
        'multi city': 'Multi-City'
    }

    all_dates = "//div[@id='monthWrapper']//td[@id!='']"

    all_city_suggestions = "//p[@class='ac_cityname']"
    current_city_suggestions = "//li//p[contains(normalize-space(),'{} ({})')]"

    select_travellers_doprdown = "//span[contains(@class,'flight_passengerBox')]"
    add_traveller_icon = "//span[@id='{}']//parent::span/following-sibling::div//span[@class='ddSpinnerPlus']"
    remove_traveller_icon = "//span[@id='{}']//parent::span/following-sibling::div//span[contains(@class,'ddSpinnerMinus')]"
    traveller_count = "//span[@id='{}']/preceding-sibling::span"
    traveller = {
        'adult': 'adultPax',
        'child': 'childPax',
        'infant': 'infantPax'
    }

    select_flight_class = "//span[text()='{}']"
    flight_class = {
        'economy': 'Economy',
        'premium economy': 'Premium Economy',
        'business': 'Business'
    }

    select_non_stop_flight = "//a[contains(normalize-space(),'Non Stop Flights')]"
    search_flights_button = "//input[@value='Search Flights']"

    ############ CLASS NAME ############
    swap_cities_button = "beSwapCity"
    back_button = "view-return"

    ############ CSS SELECTORS ############



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def nav_to_flights_page(self):
        self.wait_until_element_is_clickable(By.ID, self.nav_bar_flights_button).click()

    def select_trip_type(self, trip_type):
        self.wait_until_element_is_clickable(By.XPATH, self.trip_way_button.format(self.way[trip_type.lower()])).click()

    def select_origin_city(self, city_name, airport):
        origin_textbox = self.wait_until_element_is_clickable(By.ID, self.from_input_box)
        origin_textbox.click()
        time.sleep(3)
        origin_textbox.send_keys(city_name)
        # print(self.wait_until_presence_of_all_elements(By.XPATH, self.all_city_suggestions))
        self.wait_until_element_is_clickable(By.XPATH,self.current_city_suggestions.format(city_name, airport)).click()

    def select_arrival_city(self, city_name, airport):
        arrival_city = self.wait_until_element_is_clickable(By.ID, self.to_input_box)
        arrival_city.click()
        time.sleep(3)
        arrival_city.send_keys(city_name)
        self.wait_until_element_is_clickable(By.XPATH, self.current_city_suggestions.format(city_name, airport)).click()

    def toggle_origin_arrival_city(self):
        self.wait_until_element_is_clickable(By.CLASS_NAME, self.swap_cities_button).click()

    def select_deprature_date(self, date):
        self.wait_until_element_is_clickable(By.ID, self.depart_date_input_box).click()
        all_dates = self.wait_until_presence_of_all_elements(By.XPATH, self.all_dates)

        for curr_date in all_dates:
            if curr_date.get_attribute("id") == date:
                curr_date.click()
                break

    def add_travellers(self, travellers: dict):
        self.wait_until_element_is_clickable(By.XPATH, self.select_travellers_doprdown).click()
        all_travellers = dict()

        for traveller, number in travellers.items():
            num_of_trav = number
            while num_of_trav > 0:
                self.wait_until_element_is_clickable(By.XPATH, self.add_traveller_icon.format(
                    self.traveller[traveller])).click()
                num_of_trav -= 1
            all_travellers[traveller] = int(self.driver.find_element(By.XPATH, self.traveller_count.format(
                self.traveller[traveller])).text)

        self.wait_until_element_is_clickable(By.XPATH, self.select_travellers_doprdown).click()
        return all_travellers

    def remove_travellers(self, travellers: dict):

        self.wait_until_element_is_clickable(By.XPATH, self.select_travellers_doprdown).click()
        all_travellers = dict()

        for traveller, number in travellers.items():
            num_of_trav = number
            while num_of_trav>0:
                self.wait_until_element_is_clickable(By.XPATH, self.remove_traveller_icon.format(
                    self.traveller[traveller])).click()
                num_of_trav-=1
            all_travellers[traveller] = int(self.driver.find_element(By.XPATH, self.traveller_count.format(
                self.traveller[traveller])).text)

        self.wait_until_element_is_clickable(By.XPATH, self.select_travellers_doprdown).click()

        return all_travellers

    def select_flight_type(self, flight_type):
        self.wait_until_element_is_clickable(By.XPATH, self.select_travellers_doprdown).click()
        self.wait_until_element_is_clickable(By.XPATH, self.select_flight_class.format(self.flight_class[flight_type])).click()
        self.wait_until_element_is_clickable(By.XPATH, self.select_travellers_doprdown).click()

    def select_offer_type(self, offer):
        if "Non Stop Flights" in offer:
            self.wait_until_element_is_clickable(By.XPATH, self.select_non_stop_flight).click()
        else:
            self.wait_until_element_is_clickable(By.ID, self.select_flight_offer.format(self.flight_offer[offer])).click()

    def search_flights(self):
        self.wait_until_element_is_clickable(By.XPATH, self.search_flights_button).click()