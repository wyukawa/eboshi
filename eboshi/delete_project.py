#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command

import requests
from eboshi.session import Session

class Delete_Project(Command):
    "delete azkaban project"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Delete_Project, self).get_parser(prog_name)
        parser.add_argument('--url', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--project', required=True)
        return parser

    def take_action(self, parsed_args):
        url = parsed_args.url
        username = parsed_args.username
        password = parsed_args.password
        session = Session(url, username, password)
        session_id = session.get_session_id()

        project = parsed_args.project
        params = {"delete":"true"}
        params["session.id"] = session_id
        params["project"] = project
        r = requests.get(url + "/manager", params=params)
