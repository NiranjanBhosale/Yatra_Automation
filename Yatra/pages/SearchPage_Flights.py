from selenium.webdriver.common.by import By
from base.base import Base

class FlightsSearchPage(Base):

    ################ ID ################
    from_input_box = "origin_0"
    to_input_box = "destination_0"
    depart_date_input = "flight_depart_date_0"
    arrival_date_input = "arrivalDate_0"

    ################ XPATH ################
    top_right_cancel_btn = "//span[contains(@class, 'ytfi-cancel')]"
    travellers_dropdown_icon = "//span/following-sibling::i[contains(@class,'ytfi-angle-')]"
    add_travellers_icon = "//span[contains(normalize-space(),'{}')]/following-sibling::div//span[@class='plus']"
    remove_travellers_icon = "//span[contains(normalize-space(),'{}')]/following-sibling::div//span[@class='minus']"
    traveller = {
        'adult': 'Adult',
        'child': 'Child',
        'infant': 'Infant'
    }
    flight_class_radio_btn = "//label[normalize-space()='{}']"
    flight_class = {
        'economy': 'Economy',
        'premium economy': 'Premium Economy',
        'business': 'Business',
        'first class': 'First Class'
    }
    confirm_travellers_btn = "//input[@value='Done']"

    search_again_btn = "//span[text()='Search Again']"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

