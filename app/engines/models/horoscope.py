"""
Horoscope Model
Astro Research Lab
"""


class Horoscope:

    def __init__(
        self,
        id=None,
        full_name="",
        gender="",
        birth_date="",
        birth_time="",
        birth_place="",
        latitude=0.0,
        longitude=0.0,
        timezone="",
        ayanamsa="Lahiri",
        notes="",
        created_at="",
    ):

        self.id = id

        self.full_name = full_name

        self.gender = gender

        self.birth_date = birth_date

        self.birth_time = birth_time

        self.birth_place = birth_place

        self.latitude = latitude

        self.longitude = longitude

        self.timezone = timezone

        self.ayanamsa = ayanamsa

        self.notes = notes

        self.created_at = created_at

    def to_dict(self):

        return {

            "id": self.id,

            "full_name": self.full_name,

            "gender": self.gender,

            "birth_date": self.birth_date,

            "birth_time": self.birth_time,

            "birth_place": self.birth_place,

            "latitude": self.latitude,

            "longitude": self.longitude,

            "timezone": self.timezone,

            "ayanamsa": self.ayanamsa,

            "notes": self.notes,

            "created_at": self.created_at,

        }

    @classmethod
    def from_row(cls, row):

        return cls(

            id=row["id"],

            full_name=row["full_name"],

            gender=row["gender"],

            birth_date=row["birth_date"],

            birth_time=row["birth_time"],

            birth_place=row["birth_place"],

            latitude=row["latitude"],

            longitude=row["longitude"],

            timezone=row["timezone"],

            ayanamsa=row["ayanamsa"],

            notes=row["notes"],

            created_at=row["created_at"],

        )

    def __str__(self):

        return f"{self.full_name} ({self.birth_date} {self.birth_time})"