from ..base import Runnable
import subprocess

class Writer:
    def write(self, line):
        raise NotImplementedError()

class StdoutWriter:
    def write(self, line):
        print(line)

class PipeWriter(Runnable, Writer):
    def __init__(self):
        super().__init__()
        self.__starting = False
        self.proc = None

    def start(self):
        with self._state_lock:
            if self.__starting:
                return False
            else:
                self.__starting = True
        status = False
        self.proc = subprocess.Popen(self.cmd, stdin=subprocess.PIPE)
        status = super().start()
        if not self.running:
            self.stop()
            status = False
        return status

    def stop(self):
        if super().stop():
            try:
                self.proc.terminate()
            except:
                pass
            return True
        return False

    def restart(self):
        if not self.running:
            return
        try:
            self.proc.termintate()
        except:
            pass
        self.proc = subprocess.Popen(self.cmd, stdin=subprocess.PIPE)

    def wait(self):
        with self._state_lock:
            if not self.running:
                raise RuntimeError("Not Running")
            self.proc.wait()

    def write(self, line):
        with self._state_lock:
            if not self.running:
                raise RuntimeError("Not Running")
            self.proc.stdin.write((line+'\n').encode("utf-8"))
            self.proc.stdin.flush()

