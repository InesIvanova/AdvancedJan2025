from typing import Dict


class Gallery:
    def __init__(self, gallery_name: str, city: str, area_sq_m: float, open_to_public: bool=True):
        self.gallery_name = gallery_name
        self.city = city
        self.area_sq_m = area_sq_m
        self.open_to_public = open_to_public
        self.exhibitions: Dict[str, int] = {}

    @property
    def gallery_name(self):
        return self.__gallery_name

    @gallery_name.setter
    def gallery_name(self, value):
        if not value.strip().isalnum():
            raise ValueError("Gallery name can contain letters and digits only!")
        self.__gallery_name = value.strip()

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if not value or not value[0].isalpha():
            raise ValueError("City name must start with a letter!")
        self.__city = value

    @property
    def area_sq_m(self):
        return self.__area_sq_m

    @area_sq_m.setter
    def area_sq_m(self, value):
        if value <= 0.0:
            raise ValueError("Gallery area must be a positive number!")
        self.__area_sq_m = value

    def add_exhibition(self, exhibition_name: str, year: int):
        if exhibition_name in self.exhibitions:
            return f'Exhibition "{exhibition_name}" already exists.'
        self.exhibitions[exhibition_name] = year
        return f'Exhibition "{exhibition_name}" added for the year {year}.'

    def remove_exhibition(self, exhibition_name: str):
        if exhibition_name not in self.exhibitions:
            return f'Exhibition "{exhibition_name}" not found.'
        del self.exhibitions[exhibition_name]
        return f'Exhibition "{exhibition_name}" removed.'

    def list_exhibitions(self):
        if self.open_to_public:
            return '\n'.join(f"{name}: {year}" for name, year in self.exhibitions.items())
        return f'Gallery {self.gallery_name} is currently closed for public! Check for updates later on.'

