"""
Astro Research Lab

Database Manager
"""

import sqlite3
from pathlib import Path
from datetime import datetime


class DatabaseManager:

    DATABASE_NAME = "astro_research_lab.db"

    connection = None

    # ---------------------------------------------------------

    @classmethod
    def initialize(cls):

        database_path = Path(cls.DATABASE_NAME)

        cls.connection = sqlite3.connect(database_path)

        cls.connection.row_factory = sqlite3.Row

        cls.create_tables()

    # ---------------------------------------------------------

    @classmethod
    def cursor(cls):

        return cls.connection.cursor()

    # ---------------------------------------------------------

    @classmethod
    def commit(cls):

        cls.connection.commit()

    # ---------------------------------------------------------

    @classmethod
    def create_tables(cls):

        cursor = cls.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS horoscopes(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                full_name TEXT NOT NULL,

                gender TEXT,

                birth_date TEXT,

                birth_time TEXT,

                birth_place TEXT,

                latitude REAL,

                longitude REAL,

                timezone TEXT,

                ayanamsa TEXT,

                notes TEXT,

                created_at TEXT

            )
            """
        )

        cls.commit()

    # ---------------------------------------------------------

    @classmethod
    def add_horoscope(
        cls,
        full_name,
        gender,
        birth_date,
        birth_time,
        birth_place,
        latitude,
        longitude,
        timezone,
        ayanamsa,
        notes,
    ):

        cursor = cls.cursor()

        cursor.execute(
            """
            INSERT INTO horoscopes(

                full_name,
                gender,
                birth_date,
                birth_time,
                birth_place,
                latitude,
                longitude,
                timezone,
                ayanamsa,
                notes,
                created_at

            )

            VALUES(?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                full_name,
                gender,
                birth_date,
                birth_time,
                birth_place,
                latitude,
                longitude,
                timezone,
                ayanamsa,
                notes,
                datetime.now().isoformat(),
            ),
        )

        cls.commit()

    # ---------------------------------------------------------

    @classmethod
    def get_all_horoscopes(cls):

        cursor = cls.cursor()

        cursor.execute(
            """
            SELECT *
            FROM horoscopes
            ORDER BY full_name
            """
        )

        return cursor.fetchall()

    # ---------------------------------------------------------

    @classmethod
    def search_horoscopes(cls, keyword):

        cursor = cls.cursor()

        cursor.execute(
            """
            SELECT *

            FROM horoscopes

            WHERE

                full_name LIKE ?

                OR birth_place LIKE ?

                OR gender LIKE ?

                OR ayanamsa LIKE ?

            ORDER BY full_name
            """,
            (
                f"%{keyword}%",
                f"%{keyword}%",
                f"%{keyword}%",
                f"%{keyword}%",
            ),
        )

        return cursor.fetchall()

    # ---------------------------------------------------------

    @classmethod
    def delete_horoscope(cls, horoscope_id):

        cursor = cls.cursor()

        cursor.execute(
            """
            DELETE

            FROM horoscopes

            WHERE id=?
            """,
            (horoscope_id,),
        )

        cls.commit()

    # ---------------------------------------------------------

    @classmethod
    def total_horoscopes(cls):

        cursor = cls.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM horoscopes
            """
        )

        return cursor.fetchone()[0]

    # ---------------------------------------------------------

    @classmethod
    def close(cls):

        if cls.connection:

            cls.connection.close()