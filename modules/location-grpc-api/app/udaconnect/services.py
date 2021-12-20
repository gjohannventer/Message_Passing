import logging
from datetime import datetime
from typing import Dict

from app import db
from app.udaconnect.models import Location
from database import db 

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")


class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        with db.Session() as dbs:
            attr = {"id": location_id}
            location = db.s.first(Location, **attr)
            dbs.close()
            return location


