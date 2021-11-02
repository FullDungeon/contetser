import logging

#? how to use
#> from logger.logger import Logger
#>
#> l = Logger()
#> l.Log("message")

class Logger:
    logger = logging.getLogger(__name__)

    def StartLog(self):
        self.logger.error("\n___________________LOG___________________\n")

    def EndLog(self):
        self.logger.error("\n___________________END___________________\n") 

    def Log(self, message):
        self.logger.error(message)

    def SingleLog(self, message):
        self.StartLog()
        self.logger.error(message)
        self.EndLog()