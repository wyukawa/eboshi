#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command

import requests
from eboshi.schedule import Schedule

class Get_Schedule(Command):
    "get schedule azkaban job"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Get_Schedule, self).get_parser(prog_name)
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
        project = parsed_args.project
        flow = parsed_args.flow
        schedule = Schedule(url, username, password)
        sc = schedule.get_schedule(project, flow)
        if sc is None:
            raise Exception("no such shedule")
        print "firstSchedTime:%s, submitUser:%s, period:%s, scheduleId:%s, nextExecTime:%s" % (sc["firstSchedTime"], sc["submitUser"], sc["period"], sc["scheduleId"], sc["nextExecTime"])
