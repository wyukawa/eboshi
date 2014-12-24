#!/usr/bin/env python
# encoding: utf-8

import requests
from eboshi.session import Session

class Schedule:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def list_schedules(self):
        session = Session(self.url, self.username, self.password)
        session_id = session.get_session_id()
        params = {"ajax":"loadFlow"}
        params["session.id"] = session_id
        r = requests.get(self.url + "/schedule", params=params)
        jc = r.json()
        return jc.get("items", []) 
