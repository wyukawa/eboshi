#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command

import requests
import os.path
from eboshi.session import Session
from eboshi.project import Project

class Schedule(Command):
    "schedule azkaban job"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Schedule, self).get_parser(prog_name)
        parser.add_argument('--url', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--project', required=True)
        parser.add_argument('--flow', required=True)
        return parser

    def take_action(self, parsed_args):
        url = parsed_args.url
        username = parsed_args.username
        password = parsed_args.password
        session = Session(url, username, password)
        session_id = session.get_session_id()
        project = parsed_args.project
        flow = parsed_args.flow
        p = Project()
        project_id = p.get_project_id(url, session_id, project)
        params = {"ajax":"scheduleFlow"}
        params["session.id"] = session_id
        params["projectName"] = project
        params["projectId"] = project_id
        params["flow"] = flow
        params["scheduleDate"] = "10/28/2014"
        params["scheduleTime"] = "14,53,PM,JST"
        params["is_recurring"] = "on"
        params["period"] = "1d"
        params["failureAction"] = "finishPossible"
        r = requests.post(url + "/schedule", data=params)
        jc = r.json()
        if jc.get("status") == 'success':
            print("schedule succeeded. message=%s" % (jc["message"]))
        if jc.get("status") == 'error':
            raise Exception("schedule failed. message=%s" % (jc["message"]))
