#!/usr/bin/env python3
import datetime

import pydantricks

header = (
    f"## {pydantricks.__version__} - "
    f"Released on {datetime.datetime.now().date().isoformat()}"
)
with open("CHANGELOG.md.new", "w") as changelog:
    changelog.write(header)
    changelog.write("\n")
    changelog.write("* please write here \n\n")
