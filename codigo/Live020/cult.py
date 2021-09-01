from collections import namedtuple
from pprint import pprint
from selenium import webdriver


class Cult:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.cultcampinas.com.br'
        self.box = 'eventBox'  # class
        self.type = 'typeEventBox'  # class
        self.title_box = 'titleEventBox'  # class
        self.date = 'dateEvent'  # class
        self.place = 'placeEvent'  # class
        self.hour = 'hourEvent'  # class
        self.descr = 'descEventBox'  # class
        self.event = namedtuple('Event',
                                'title type date place hour descr')

    def navigate(self):
        self.driver.get(self.url)

    def _get_boxes(self):
        return self.driver.find_elements_by_class_name(
            self.box)

    def _get_title(self, box):
        return box.find_element_by_class_name(self.title_box)

    def _get_type(self, box):
        return box.find_element_by_class_name(self.type)

    def _get_date(self, box):
        return box.find_element_by_class_name(self.date)

    def _get_place(self, box):
        return box.find_element_by_class_name(self.place)

    def _get_hour(self, box):
        return box.find_element_by_class_name(self.hour)

    def _get_descr(self, box):
        return box.find_element_by_class_name(self.descr)

    def get_all_data(self):
        boxes = self._get_boxes()
        for box in boxes:
            yield self.event(self._get_title(box).text,
                             self._get_type(box).text,
                             self._get_date(box).text,
                             self._get_place(box).text,
                             self._get_hour(box).text,
                             self._get_descr(box).text)


ff = webdriver.Firefox()
c = Cult(ff)
c.navigate()
for event in c.get_all_data():
    pprint(event)
