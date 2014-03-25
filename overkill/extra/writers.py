##
#    This file is part of Overkill-writers.
#
#    Overkill-writers is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Overkill-writers is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Overkill-writers.  If not, see <http://www.gnu.org/licenses/>.
##

from ..base import Subprocess
import subprocess

class Writer:
    def write(self, line):
        raise NotImplementedError()

class StdoutWriter:
    def write(self, line):
        print(line)

class PipeWriter(Subprocess, Writer):
    stdin = subprocess.PIPE

    def write(self, line):
        with self._state_lock:
            if not self.running:
                raise RuntimeError("Not Running")
            self.proc.stdin.write((line+'\n').encode("utf-8"))
            self.proc.stdin.flush()

