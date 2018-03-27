from __future__ import print_function
import os
from django.core.management.base import BaseCommand
from ...utils import read_file
from ...msgs import Msgs
from ...models import FileToEdit


class Command(BaseCommand, Msgs):
    help = 'Populate file instances from a directory for dirtyedit'

    def add_arguments(self, parser):
        parser.add_argument('source', type=str)

    def handle(self, *args, **options):
        source = options["source"]
        # get the files
        self.status("Getting files from " + source)
        filenames = self.get_filenames(source)
        # save instances
        for filename in filenames:
            path = source + filename
            status, msg, filecontent = read_file(path, True)
            if status is True:
                self.status(msg)
            else:
                if status == 'warn':
                    self.error(msg)
                elif status == 'infos':
                    self.info(msg)
                self.error(msg)
            # save instance
            _, created = FileToEdit.objects.get_or_create(
                relative_path=path, content=filecontent)
            if created is False:
                msg = "File " + filename + " already exists in the database"
                self.error(msg)
        self.ok("Done")

    def get_filenames(self, startpath):
        dirfiles = []
        for _, _, files in os.walk(startpath):
            for filename in files:
                print(filename)
                dirfiles.append(filename)
        return dirfiles
