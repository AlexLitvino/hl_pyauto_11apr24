"""
CREATE TABLE Vendors(vendor_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL);
INSERT INTO Vendors(name, item, deal, price) VALUES
('Johny', 'Train', 3, 32.4),
('James', 'Plane', 2, 101.12),
('John', 'Plane', 1, 56),
('Andrew', 'Car', 6, 34),
('Anna', 'Helicopter', 3, 345)
;
"""
from abc import ABC, abstractmethod
import sqlite3

class Vendor:

    def __init__(self, name, item, deal, price):
        self.name = name
        self.item = item
        self.deal = deal
        self.price = price

    def __repr__(self):
        return f"Vendor({self.name}, {self.item}, {self.deal}, {self.price})"


class BaseRepository(ABC):
    
    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path)
        self._cursor = self._connection.cursor()

    @abstractmethod
    def get_all(self):
        pass

    def close(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()


class VendorRepository(BaseRepository):

    def __init__(self, db_path):
        super().__init__(db_path)
        self._cursor.execute('CREATE TABLE IF NOT EXISTS Vendors(vendor_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL);')

    def add_vendor(self, vendor: Vendor):
        self._cursor.execute(f"INSERT INTO Vendors(name, item, deal, price) VALUES ('{vendor.name}', '{vendor.item}', {vendor.deal}, {vendor.price})")
        self._connection.commit()

    def get_all(self):
        self._cursor.execute('SELECT * FROM Vendors;')
        return VendorRepository._rows2obj(self._cursor.fetchall())

    def get_vendor_by_deal(self, deal):
        self._cursor.execute('SELECT * FROM Vendors WHERE deal=?;', (deal,))
        return VendorRepository._rows2obj(self._cursor.fetchall())

    @staticmethod
    def _row2obj(row):
        return Vendor(*row[1:])

    @staticmethod
    def _rows2obj(rows):
        objects = []
        for row in rows:
            objects.append(VendorRepository._row2obj(row))
        return objects


vendor_repo = VendorRepository('venodr.db')
print(vendor_repo.get_all())
print(vendor_repo.get_vendor_by_deal(5))
print(vendor_repo.get_vendor_by_deal(4))
# vendor1 = Vendor('Julia', 'Car', 4, 23)
# vendor_repo.add_vendor(vendor1)
# print(vendor_repo.get_all())
