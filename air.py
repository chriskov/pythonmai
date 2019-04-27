
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup

class park(ABC):
    @property
    @abstractmethod
    def company_name(self):
        pass

    @property
    def about_aircrafts(self):
        return self._about_aircrafts


class S7(park):
    def __init__(self):
        r = requests.get('https://www.s7.ru/about/ourfleet.dot')
        if (r.status_code != 200):
            self.__about_aircrafts = None
            return
        content_tree = BeautifulSoup(r.text, 'html.parser')
        maint_content = content_tree.find('div', class_='company-main-cont')
        aircraft_names = maint_content.find_all('h3')

        lines = []
        for aircraft_name in aircraft_names:
            lines.append(aircraft_name.string)
            aircraft_block = aircraft_name.find_parent('div')
            info = aircraft_block.find_all('div', class_='col-md-14 no-padding-left')
            #print(craft.prettify())
            for i in info:
                if (i.string is not None):
                    lines.append('\t' + i.string)
            lines.append('\n')
        self._about_aircrafts = ''.join(map(lambda l: l + '\n', lines))

    @property
    def company_name(self):
        return 'S7'


class Utair(park):
    def __init__(self):
        r = requests.get('https://www.utair.ru/about/aircrafts/')
        if (r.status_code != 200):
            self.__about_aircrafts = None
            return
        content_tree = BeautifulSoup(r.text, 'html.parser')
        aircraft_blocks = content_tree.find_all('div', class_='airship-block-left')

        lines = []
        for block in aircraft_blocks:
            name = block.find('a').string
            lines.append(name)
            info = block.find_all('p')
            for i in info:
                if (i.find('b') is None):
                    lines.append('\t' + i.string)
        self._about_aircrafts = ''.join(map(lambda l: l + '\n', lines))

    @property
    def company_name(self):
        return 'Utair'


class Russia(park):
    def __init__(self):
        r = requests.get('https://www.rossiya-airlines.com/about/about_us/fleet/aircraft/')
        if (r.status_code != 200):
            self.__about_aircrafts = None
            return
        content_tree = BeautifulSoup(r.text, 'html.parser')
        main_content = content_tree.find_all('table')
        aircraft_blocks = main_content[1].find_all('tr')

        lines = []
        for block in aircraft_blocks:
            aircraft = block.find_all('td')[0]
            info = aircraft.find_all('span')
            for i in info:
                if (i.string is None):
                    continue
                if (i.find_parent('h2') is not None):
                    lines.append(i.string)
                else:
                    lines.append(i.string)
            lines.append('\n')
        self._about_aircrafts = ''.join(lines)

    @property
    def company_name(self):
        return 'Russia'


class Nordstar(park):
    def __init__(self) -> object:
        r = requests.get('https://www.nordstar.ru/about/park/')
        if (r.status_code != 200):
            self.__about_aircrafts = None
            return
        content_tree = BeautifulSoup(r.text, 'html.parser')
        aircraft_blocks = content_tree.find_all('div', class_='col-sm-6 col-xs-12 vs')

        lines = []
        for block in aircraft_blocks:
            name = block.find('h2').string
            lines.append(name)
            info = block.find_all('p', recursive=False)[1:]
            for i in info:
                if (not i.find('a')):
                    lines.append('\t' + i.text)
            lines.append('\n')
        self._about_aircrafts = ''.join(map(lambda l: l + '\n', lines))

    @property
    def company_name(self):
        return 'NordStar'


class Ural(park):
    def __init__(self):
        r = requests.get('https://www.uralairlines.ru/passengers-info/about/fleet/')
        if (r.status_code != 200):
            self.__about_aircrafts = None
            return
        content_tree = BeautifulSoup(r.text, 'html.parser')
        aircraft_blocks = content_tree.find_all('div', class_='onePlane')

        lines = []
        for block in aircraft_blocks:
            lines.append(block.find('h6').string)
            info = block.find_all('tr')
            for i in info:
                components = i.find_all('td')
                if (not components):
                    continue
                lines.append('\t' + components[0].string + ': ' + components[1].string)
            lines.append('\n')
        self._about_aircrafts = ''.join(map(lambda l: l + '\n', lines))

    @property
    def company_name(self):
        return 'Ural Airlines'


