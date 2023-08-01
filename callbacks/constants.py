
CALLBACK_RUN_SCRIPT = 'RUN_SCRIPT'
CALLBACK_SET_TEXT = 'SET_TEXT'
CALLBACK_PLAY_VIDEO = 'PLAY_VIDEO'
CALLBACK_SET_CAMERA = 'SET_CAMERA'
CALLBACK_PLAY_ANIMATION = 'PLAY_ANIMATION'

# used as enum property items
CALLBACK_TYPES = (
    (CALLBACK_RUN_SCRIPT, "Run Script", "Execute the given text"),
    (CALLBACK_SET_TEXT, "Set Text", "Set the text of a text object"),
    (CALLBACK_PLAY_VIDEO, "Play Video", "Play the given video"),
    (CALLBACK_SET_CAMERA, "Set Camera", "Set the active scene camera"),
    (CALLBACK_PLAY_ANIMATION, "Play Animation", "Play the given animation"),
)

# different lists of callbacks that are execute at different points in time
CALLBACK_LISTS = (
    ("on_enter", "On Enter", "Executed before the slide is shown"),
)
