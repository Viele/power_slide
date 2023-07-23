
CALLBACK_RUN_SCRIPT = 'RUN_SCRIPT'
CALLBACK_SET_TEXT = 'SET_TEXT'
CALLBACK_PLAY_VIDEO = 'PLAY_VIDEO'
CALLBACK_SET_CAMERA = 'SET_CAMERA'

# used as enum property items
CALLBACK_TYPES = (
    (CALLBACK_RUN_SCRIPT, "Run Script", "Execute the given text"),
    (CALLBACK_SET_TEXT, "Set Text", "Set the text of a text object"),
    (CALLBACK_PLAY_VIDEO, "Play Video", "Play the given video"),
    (CALLBACK_SET_CAMERA, "Set Camera", "Set the active scene camera"),
)

# different lists of callbacks that are execute at different points in time
CALLBACK_LISTS = (
    ("on_enter", "On Enter", "Executed before the slide is shown"),
    ("on_exit", "On Exit", "Execute just before going to the next slide")
)
