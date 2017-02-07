#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command

import requests
import os.path
from eboshi.session import Session
from eboshi.project import Project
from ast import literal_eval

class Add_Cron_Schedule(Command):
    "add cron schedule azkaban job"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Add_Cron_Schedule, self).get_parser(prog_name)
        parser.add_argument('--url', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--project', required=True)
        parser.add_argument('--flow', required=True)
        parser.add_argument('--cron', required=True, help='crone expression (for example, 0 23/30 5,7-10 ? * 6#3).')
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
        cronExpression = parsed_args.cron

        params = {"ajax":"scheduleCronFlow"}
        params["session.id"] = session_id
        params["projectName"] = project
        params["flow"] = flow
        params["cronExpression"] = cronExpression

        if parsed_args.option:
            params.update(literal_eval(parsed_args.option))
        r = requests.post(url + "/schedule", data=params)
        jc = r.json()
        if jc.get("status") == 'success':
            print("add cron schedule succeeded. scheduleId=%s, message=%s" % (jc.get("scheduleId"), jc.get("message")))
        elif jc.get("status") == 'error':
            raise Exception("add cron schedule failed. message=%s. error=%s" % (jc.get("message"), jc.get("error")))
        else:
            raise Exception("add cron schedule failed. error=%s" % (jc.get("error")))
