class NationalPark:

    all = []

    def __init__(self, name):
        if (isinstance(name, str) and 3 <= len(name)):
            self._name = name
            NationalPark.all.append(self)
        else:
            raise Exception

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (not hasattr(self, '_name')):
            if (isinstance(name, str) and 3 <= len(name)):
                self._name = name
            else:
                raise Exception
        else:
            raise Exception

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park is self]))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        if (len(self.trips())):
            visitor_dict = {}
            for visit in self.trips():
                if (visit.visitor in visitor_dict):
                    visitor_dict[visit.visitor] += 1
                else:
                    visitor_dict[visit.visitor] = 1
            visitors = list(visitor_dict.keys())
            visits = list(visitor_dict.values())
            return visitors[visits.index(max(visits))]
        return 0

    @classmethod
    def most_visited(cls):
        if (len(cls.all)):
            visits = []
            for park in cls.all:
                visits.append(len(park.trips()))
            return cls.all[visits.index(max(visits))]
        return None


class Trip:

    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        if (isinstance(visitor, Visitor)):
            self._visitor = visitor
            if (isinstance(national_park, NationalPark)):
                self._national_park = national_park
                if (isinstance(start_date, str) and len(start_date) >= 7):
                    self._start_date = start_date
                    if (isinstance(end_date, str) and len(end_date) >= 7):
                        self._end_date = end_date
                        Trip.all.append(self)
                    else:
                        raise Exception
                else:
                    raise Exception
            else:
                raise Exception
        else:
            raise Exception

    @property
    def national_park(self):
        return self._national_park

    @property
    def visitor(self):
        return self._visitor

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if (isinstance(start_date, str) and len(start_date) >= 7):
            self._start_date = start_date
        else:
            raise Exception

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if (isinstance(end_date, str) and len(end_date) >= 7):
            self._end_date = end_date
        else:
            raise Exception


class Visitor:

    all = []

    def __init__(self, name):
        if (isinstance(name, str) and 1 < len(name) < 15):
            self._name = name
            Visitor.all.append(self)
        else:
            raise Exception

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (isinstance(name, str) and 1 < len(name) < 15):
            self._name = name
        else:
            raise Exception

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor is self]))

    def total_visits_at_park(self, park):
        return len([trip for trip in Trip.all if trip.visitor is self and trip.national_park == park])
