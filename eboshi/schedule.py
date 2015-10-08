#!/usr/bin/env python
# encoding: utf-8

import requests
from eboshi.session import Session
from eboshi.project import Project

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

    def remove_schedule(self, scheduleId):
        session = Session(self.url, self.username, self.password)
        session_id = session.get_session_id()
        params = {"action":"removeSched"}
        params["session.id"] = session_id
        params["scheduleId"] = scheduleId
        r = requests.post(self.url + "/schedule", data=params)
        jc = r.json()
        if jc.get("status") == 'success':
            print("remove schedule succeeded. message=%s" % (jc.get("message")))
        if jc.get("status") == 'error':
            raise Exception("remove schedule failed. message=%s" % (jc.get("message")))

    def remove_all_schedules(self):
        items = self.list_schedules()
        for item in items:
            scheduleid = item["scheduleid"]
            self.remove_schedule(scheduleid)

    def get_schedule(self, project, flow):
        session = Session(self.url, self.username, self.password)
        session_id = session.get_session_id()
        params = {"ajax":"fetchSchedule"}
        params["session.id"] = session_id
        p = Project()
        project_id = p.get_project_id(self.url, session_id, project)
        params["projectId"] = project_id
        params["flowId"] = flow
        r = requests.get(self.url + "/schedule", params=params)
        jc = r.json()
        return jc.get("schedule") 
