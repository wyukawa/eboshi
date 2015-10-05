#!/usr/bin/env python
# encoding: utf-8

import logging
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class Eboshi(App):

    log = logging.getLogger(__name__)

    logging.getLogger("requests").setLevel(logging.WARNING)

    def __init__(self):
        super(Eboshi, self).__init__(
            description='Azkaban CLI',
            version='0.0.9',
            command_manager=CommandManager('eboshi'),
            )

    def initialize_app(self, argv):
        self.log.debug('initialize_app')

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    app = Eboshi()
    return app.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
