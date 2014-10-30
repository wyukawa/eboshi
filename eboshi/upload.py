#!/usr/bin/env python
# encoding: utf-8

import logging

from cliff.command import Command

import requests
import os.path
from eboshi.session import Session

class Upload(Command):
    "upload azkaban job zip file"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Upload, self).get_parser(prog_name)
        parser.add_argument('--url', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--project', required=True)
        parser.add_argument('--filename', required=True)
        return parser

    def take_action(self, parsed_args):
        url = parsed_args.url
        username = parsed_args.username
        password = parsed_args.password
        session = Session(url, username, password)
        session_id = session.get_session_id()

        project = parsed_args.project
        filename = parsed_args.filename
        data = {"ajax":"upload"}
        data["session.id"] = session_id
        data["project"] = project
        files = {'file': (os.path.basename(filename), open(filename), 'application/zip')}
        r = requests.post(url + "/manager", data=data, files=files)
        jc = r.json()
        
        if jc.get("error") is None:
            print "upload succeeded."
        else:
            raise Exception("upload failed. error=%s" % (jc.get("error")))
