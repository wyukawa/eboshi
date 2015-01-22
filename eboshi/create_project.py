#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command

import requests
from eboshi.session import Session

class Create_Project(Command):
    "create azkaban project"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Create_Project, self).get_parser(prog_name)
        parser.add_argument('--url', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--project', required=True)
        parser.add_argument('--description', required=True)
        return parser

    def take_action(self, parsed_args):
        url = parsed_args.url
        username = parsed_args.username
        password = parsed_args.password
        session = Session(url, username, password)
        session_id = session.get_session_id()

        project = parsed_args.project
        description = parsed_args.description
        data = {"action":"create"}
        data["session.id"] = session_id
        data["name"] = project
        data["description"] = description
        r = requests.post(url + "/manager", data=data)
        jc = r.json()
        
        if jc.get("status") == 'success':
            print "create project succeeded. status=%s, path=%s, action=%s" % (jc.get("status"), jc.get("path"), jc.get("action"))
        else:
            raise Exception("create project failed. message=%s, error=%s" % (jc.get("message"), jc.get("error")))
