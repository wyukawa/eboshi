#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command

import requests
import os.path
from eboshi.session import Session
from eboshi.project import Project

class Exec(Command):
    "exec azkaban job"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Exec, self).get_parser(prog_name)
        parser.add_argument('--url', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--project', required=True)
        parser.add_argument('--flow', required=True)
        parser.add_argument('--flowOverride', nargs='*', default=[])
        parser.add_argument('--disabled')
        parser.add_argument('--successEmails')
        parser.add_argument('--failureEmails')
        parser.add_argument('--successEmailsOverride')
        parser.add_argument('--failureEmailsOverride')
        parser.add_argument('--notifyFailureFirst')
        parser.add_argument('--notifyFailureLast')
        parser.add_argument('--failureAction')
        parser.add_argument('--concurrentOption')
        return parser

    def take_action(self, parsed_args):
        url = parsed_args.url
        username = parsed_args.username
        password = parsed_args.password
        session = Session(url, username, password)
        session_id = session.get_session_id()
        project = parsed_args.project
        flow = parsed_args.flow
        params = {"ajax":"executeFlow"}
        params["session.id"] = session_id
        params["project"] = project
        params["flow"] = flow
        params["disabled"] = parsed_args.disabled
        params["successEmails"] = parsed_args.successEmails
        params["failureEmails"] = parsed_args.failureEmails
        params["successEmailsOverride"] = parsed_args.successEmailsOverride
        params["failureEmailsOverride"] = parsed_args.failureEmailsOverride
        params["notifyFailureFirst"] = parsed_args.notifyFailureFirst
        params["notifyFailureLast"] = parsed_args.notifyFailureLast
        params["failureAction"] = parsed_args.failureAction
        params["concurrentOption"] = parsed_args.concurrentOption

        for item in parsed_args.flowOverride:
            pair = item.split("=")
            params["flowOverride[%s]" % pair[0]] = pair[1]

        r = requests.get(url + "/executor", params=params)
        jc = r.json()
        if jc.get("execid") is None:
            raise Exception("exec failed. project=%s. flow=%s. message=%s. error=%s" % (jc.get("project"), jc.get("flow"), jc.get("message"), jc.get("error")))
        else:
            print "exec succeeded. execid=%s. project=%s. flow=%s. message=%s" % (jc.get("execid"), jc.get("project"), jc.get("flow"), jc.get("message"))
