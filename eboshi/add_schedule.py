#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command

import requests
import os.path
from eboshi.session import Session
from eboshi.project import Project
from ast import literal_eval

class Add_Schedule(Command):
    "add schedule azkaban job"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Add_Schedule, self).get_parser(prog_name)
        parser.add_argument('--url', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--project', required=True)
        parser.add_argument('--flow', required=True)
        parser.add_argument('--date', required=True, help='Date of the first run (for example, 08/07/2014).')
        parser.add_argument('--time', required=True, help='Time of the schedule (for example, 10,30,AM,JST).')
        parser.add_argument('--period', required=True, help='Frequency to repeat. Consists of a number and a unit(for example, 1h, 1d, 1m). If not specified the flow will be run only once.')
        parser.add_argument('--option', help='for example,{"failureAction":"finishPossible"}')
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
        params["scheduleDate"] = parsed_args.date
        params["scheduleTime"] = parsed_args.time
        if parsed_args.period:
            params["is_recurring"] = 'on'
            params["period"] = parsed_args.period
        if parsed_args.option:
            params.update(literal_eval(parsed_args.option))
        r = requests.post(url + "/schedule", data=params)
        jc = r.json()
        if jc.get("status") == 'success':
            print("add schedule succeeded. message=%s" % (jc.get("message")))
        elif jc.get("status") == 'error':
            raise Exception("add schedule failed. message=%s. error=%s" % (jc.get("message"), jc.get("error")))
        else:
            raise Exception("add schedule failed. error=%s" % (jc.get("error")))
