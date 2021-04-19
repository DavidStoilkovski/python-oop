class DVD:

    def __init__(self, name, _id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def convert_date(date):
        date = date.split('.')
        creation_month = months[date[1]]
        creation_year = date[2]
        return creation_year, creation_month


    @classmethod
    def from_date(cls, _id, name, date, age_restrictions):
        creation_year, creation_month = DVD.convert_date(date)
        return cls(name, _id, int(creation_year), creation_month, age_restrictions)


    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"


months = {
    '01': "January",
    '02': "February",
    '03': "March",
    '04': "April",
    '05': "May",
    '06': "June",
    '07': "July",
    '08': "August",
    '09': "September",
    '10': "October",
    '11': "November",
    '12': "December"
}