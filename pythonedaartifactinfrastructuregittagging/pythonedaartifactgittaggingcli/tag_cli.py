"""
pythonedaartifactinfrastructuregittagging/pythonedaartifactgittaggingcli/tag_cli.py

This file performs the tagging of git repositories from the cli.

Copyright (C) 2023-today rydnr's pythoneda-artifact-infrastructure/git-tagging

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.primary_port import PrimaryPort
from pythonedaartifacteventgittagging.tag_requested import TagRequested

import argparse
import logging


class TagCli(PrimaryPort):

    """
    A PrimaryPort that performs the tagging specified from the command line.
    """
    def priority(self) -> int:
        return 100

    async def accept(self, app):
        """
        Processes the command specified from the command line.
        :param app: The PythonEDA instance.
        :type app: PythonEDA
        """
        parser = argparse.ArgumentParser(
            description="Tags given repository"
        )
        parser.add_argument("repository_url", help="The url of the repository")
        parser.add_argument("branch", help="The branch to tag")
        args, unknown_args = parser.parse_known_args()

        event = TagRequested(args.repository_url, args.branch)
        logging.getLogger(__name__).debug(f"Requesting the tagging of repository {event.repository_url}/{event.branch}")
        await app.accept(event)
