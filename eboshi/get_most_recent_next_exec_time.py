#!/usr/bin/env python
# encoding: utf-8

import logging
from datetime import datetime

from cliff.command import Command

import requests
from eboshi.schedule import Schedule

class Get_Most_Recent_Next_Exec_Time(Command):
    "get most recent next exec time"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Get_Most_Recent_Next_Exec_Time, self).get_parser(prog_name)
        parser.add_argument('--url', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        return parser

    def take_action(self, parsed_args):
        url = parsed_args.url
        username = parsed_args.username
        password = parsed_args.password
        schedule = Schedule(url, username, password)
        items = schedule.list_schedules()
        most_recent_next_exec_time = None
        for item in items:
            flow = item["flowname"]
            project = item["projectname"]
            sc = schedule.get_schedule(project, flow)
            dt = datetime.strptime(sc["nextExecTime"], '%Y-%m-%d %H:%M:%S')
            if most_recent_next_exec_time is None:
                most_recent_next_exec_time = dt
            if most_recent_next_exec_time > dt:
                most_recent_next_exec_time = dt
        if most_recent_next_exec_time is None:
            raise Exception("schedule is not found")
        print most_recent_next_exec_time.strftime("%Y-%m-%d %H:%M:%S")
