from mongoengine import signals
from flask import url_for
import os

from application import db
from utilities.common import utc_now_ts as now


class Networks(db.Document):
    fwip = db.StringField(db_field="f", required=True)
    maskbits = db.StringField(db_field="m", required=True)
    gateway = db.StringField(db_field="g", required=True)
    tag = db.StringField(db_field="t", required=True)
    comment = db.StringField(db_field="c", required=True)
    zone = db.StringField(db_field="z", required=True)

class FireWalls(db.Document):
    firewall_ip = db.StringField(db_field="f", required=True, unique=True)
    ha_pair_id = db.StringField(db_field="h", required=True)
    created = db.IntField(db_field="c", default=now())

class Creds(db.Document):
    fwip = db.StringField(db_field="f", required=True, unique=True)
    username = db.StringField(db_field="u", required=True)
    password = db.StringField(db_field="p", required=True)
