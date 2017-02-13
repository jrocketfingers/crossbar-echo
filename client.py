import logging

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


logger = logging.getLogger(name=__name__)


class EchoClient(ApplicationSession):
    async def onJoin(self, details):
        logger.info("Successfully connected to the router.")

        await self.call("com.echo.log", "DATA")
        self.publish("com.echo.log", "DATA")


if __name__ == '__main__':
    runner = ApplicationRunner(url="ws://localhost:8080/ws", realm="echo")
    runner.run(EchoClient)
