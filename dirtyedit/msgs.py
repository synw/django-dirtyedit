# -*- coding: utf-8 -


class Msgs():
    """
    A class to handle application messages
    """

    def ok(self, msg):
        """
        Prints an error message
        """
        err = "[" + self.style.SUCCESS("Ok") + "] " + msg
        self.stdout.write(err)

    def error(self, msg):
        """
        Prints an error message
        """
        err = "[" + self.style.ERROR("Error") + "] " + msg
        self.stdout.write(err)

    def status(self, msg):
        """
        Prints an info message
        """
        err = "[" + self.style.HTTP_NOT_FOUND("Status") + "] " + msg
        self.stdout.write(err)

    def info(self, msg):
        """
        Prints an info message
        """
        err = "[" + self.style.HTTP_NOT_MODIFIED("Info") + "] " + msg
        self.stdout.write(err)
