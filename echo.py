import logging

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


logger = logging.getLogger(name=__name__)


class EchoServer(ApplicationSession):
    async def onJoin(self, details):
        logger.info("Successfully connected to the router.")

        def log_callee(value):
            logger.info(f"Received as a callee: {value}")

        def log_subscriber(value):
            logger.info(f"Received as a subscriber: {value}")

        await self.register(log_callee, "com.echo.log")
        await self.subscribe(log_subscriber, "com.echo.log")


if __name__ == '__main__':
    runner = ApplicationRunner(url="ws://localhost:8080/ws", realm="echo")
    runner.run(EchoServer)
