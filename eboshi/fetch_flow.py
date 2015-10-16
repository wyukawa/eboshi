#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command
import requests

from eboshi.session import Session

class Fetch_Flow(Command):
    "fetch flow azkaban job"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Fetch_Flow, self).get_parser(prog_name)
        parser.add_argument('--url', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--execid', required=True)
        return parser

    def take_action(self, parsed_args):
        url = parsed_args.url
        username = parsed_args.username
        password = parsed_args.password
        execid = parsed_args.execid
        session = Session(url, username, password)
        session_id = session.get_session_id()
        params = {"ajax":"fetchexecflow"}
        params["session.id"] = session_id
        params["execid"] = execid
        r = requests.get(url + "/executor", params=params)
        jc = r.json()
        if jc.get("error") is None:
            print jc.get("status")
        else:
            raise Exception("fetch flow failed. error=%s" % (jc.get("error")))
