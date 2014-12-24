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
            scheduleid = item["scheduleid"]
            stats = item["stats"]
            max = stats["max"]
            average = stats["average"]
            min = stats["min"]
            projectname = item["projectname"]
            period = item["period"]
            length = item["length"]
            time = item["time"]
            history = item["history"]
            print "flowname:%s, scheduleid:%s, max:%s, average:%s, min:%s, projectname:%s, period:%s, length:%s, time:%s, history:%s" % (flowname, scheduleid, max, average, min, projectname, period, length, time, history)

