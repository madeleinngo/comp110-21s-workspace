"""Examples of importing modules and global identifiers."""

# Import an entire module
from lessons.helpers import shout, whisper
from lessons import helpers as hp
from lessons import helpers

# Access names in that module following the dot
helpers.shout("This functionality was imported!")
print(helpers.THE_ANSWER)

# Alias a module
hp.whisper("THIS IS AN ALIAS OF HELPERS")

# Import names directly from a module
shout("imported this function!")
