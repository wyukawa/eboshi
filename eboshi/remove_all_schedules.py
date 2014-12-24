#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command

import requests
from eboshi.schedule import Schedule

class Remove_All_Schedules(Command):
    "remove all schedules azkaban job"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Remove_All_Schedules, self).get_parser(prog_name)
        parser.add_argument('--url', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        return parser

    def take_action(self, parsed_args):
        url = parsed_args.url
        username = parsed_args.username
        password = parsed_args.password
        schedule = Schedule(url, username, password)
        schedule.remove_all_schedules()
