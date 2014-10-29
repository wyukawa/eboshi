#!/usr/bin/env python
# encoding: utf-8

import requests

class Project:

    def get_project_id(self, url, session_id, project):
        params = {"ajax":"fetchprojectflows"}
        params["session.id"] = session_id
        params["project"] = project
        r = requests.get(url + "/manager", params=params)
        jc = r.json()
        
        project_id = jc.get("projectId")
        return project_id
