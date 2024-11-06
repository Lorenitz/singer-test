
import sys
from unittest.mock import patch
from tap import TapIMDB

run_args = [
    "tap.py",
    "-c",
    "../config.json",
]

tap = TapIMDB()

# Run extraction
with patch.object(sys, "argv", run_args):
    tap.run()