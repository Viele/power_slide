import abc


def execute(callbacks):
    for foo in callbacks:
        print(foo)


class AbstractCallback(abc.ABC):
    name = "Abstract Callback"

    def execute(self):
        pass


class SetText(AbstractCallback):
    name = "Set Text"


class PlayVideo(AbstractCallback):
    name = "Play Video"


class PauseVideo(AbstractCallback):
    name = "Pause Video"


class ExecuteScript(AbstractCallback):
    name = "Execute Script"
