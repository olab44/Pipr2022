class EmptyCityError(Exception):
    def __init__(self, city):
        super().__init__('you have to give some city')


class OutOfRangeCityError(Exception):
    def __init__(self, city):
        super().__init__('your city is not within our range')


cities = ['Warszawa', 'Radom', 'Siedlce']


class Hospital:
    def __init__(self, hcity, covid_beds, resp_cov, non_covid_beds, oiom_n_cov):
        if not hcity:
            raise EmptyCityError(hcity)
        if hcity not in cities:
            raise OutOfRangeCityError(hcity)
        self.city = hcity
        self.resp_cov = resp_cov
        self.oiom_n_cov = oiom_n_cov
        self.covid_beds = covid_beds
        self.non_covid_beds = non_covid_beds

    def avaiable_resp_covbeds(self, occupied_beds=0):
        return max(0, self.resp_cov - occupied_beds)

    def avaiable_oiom_n_cov(self, occupied_beds=0):
        return max(0, self.oiom_n_cov - occupied_beds)

    def avaiable_covid_beds(self, occupied_beds=0):
        return max(0, self.covid_beds - occupied_beds)

    def avaiable_non_covid_beds(self, occupied_beds=0):
        return max(0, self.non_covid_beds - occupied_beds)


class Patient:
    def __init__(self, city, covid, status):
        if not city:
            raise EmptyCityError(city)
        if city not in cities:
            raise OutOfRangeCityError(city)
        self.city = str(city)
        self.covid = str(covid)
        self.status = str(status)

    def __str__(self):
        return f'patient from {self.city}, has {self.covid} covid test, his status is {self.status}'

    def is_critical(self):
        if self.status == 'critical':
            return True
        else:
            return False

    def has_covid(self):
        if self.covid == 'positive':
            return True
        else:
            return False


class WhereToGo(Hospital, Patient):
    def __init__(self, hcity, city, covid, status, destination):
        super().__init__(hcity)
        super().__init__(self, city, covid, status)
        self._destination = None

    warszawa = Hospital('Warszawa', 1800, 400, 2200, 200)
    siedlce = Hospital('Siedlce', 335, 110, 455, 40)
    radom = Hospital('Radom', 300, 90, 200, 25)

    def check_city(self):
        if self.hcity == self.city:
            super().has_covid()
            super().is_critical()
            if self.has_covid() is True:
                if self.avaiable_covid_beds() > 0:
                    pass

