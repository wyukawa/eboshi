#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command

import requests
from eboshi.schedule import Schedule

class List_Schedules(Command):
    "list schedules azkaban job"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(List_Schedules, self).get_parser(prog_name)
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
        for item in items:
            flowname = item["flowname"]
            scheduleId = item["scheduleId"]
            projectname = item["projectname"]
            cron = item.get("cron", "")
            period = item["period"]
            time = item["time"]
            history = item["history"]
            print "flowname:%s, scheduleId:%s, projectname:%s, cron:%s, period:%s, time:%s, history:%s" % (flowname, scheduleId, projectname, cron, period, time, history)
