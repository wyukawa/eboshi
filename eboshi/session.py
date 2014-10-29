#!/usr/bin/env python
# encoding: utf-8

import requests

class Session:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def get_session_id(self):
        params = {"action":"login"}
        params["username"] = self.username
        params["password"] = self.password
        
        r = requests.post(self.url, params=params)
        
        jc = r.json()
        if jc.get("status") is None:
            raise Exception("login failed. error=%s" % (jc["error"]))
        
        session_id = jc["session.id"]
        return session_id
