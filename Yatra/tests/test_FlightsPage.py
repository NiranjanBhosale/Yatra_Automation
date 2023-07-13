import time

from pages.FlightsPage import Flights_Page

# verify total travellers count of different travellers and combined as well

class Test_FlightsPage:

    def test_adult_travellers_count(self):

        add_travellers = {"adult": 4, "child": 3}
        remove_travellers = {"adult": 3, "child": 2}

        flightPage_Obj = Flights_Page(self.driver)

        flightPage_Obj.nav_to_flights_page()

        flightPage_Obj.select_trip_type("one way")

        flightPage_Obj.select_origin_city("New York", "JFK")

        flightPage_Obj.select_arrival_city("New Delhi", "DEL")

        flightPage_Obj.select_deprature_date("12/06/2023")

        # never make adult and child count same
        added_travellers = flightPage_Obj.add_travellers(add_travellers)

        removed_travellers = flightPage_Obj.remove_travellers(remove_travellers)

        for traveller in removed_travellers.keys():
            if traveller == "adult":
                assert added_travellers[traveller] == add_travellers[traveller]+1
            else:
                assert added_travellers[traveller] == add_travellers[traveller]
            assert added_travellers[traveller]-removed_travellers[traveller] == remove_travellers[traveller]


    def test_search_premium_flights(self):
        add_travellers = {"adult": 4, "child": 1, "infant": 2}

        flightPage_Obj = Flights_Page(self.driver)

        flightPage_Obj.nav_to_flights_page()

        flightPage_Obj.select_trip_type("one way")

        flightPage_Obj.select_origin_city("New Delhi", "DEL")

        flightPage_Obj.select_arrival_city("New York", "JFK")

        flightPage_Obj.select_deprature_date("10/06/2023")

        # never make adult and child count same
        flightPage_Obj.add_travellers(add_travellers)

        flightPage_Obj.select_flight_type("premium economy")

        flightPage_Obj.search_flights()
        time.sleep(10)
