import subprocess
import time
import json
import unittest


class TestOMDBTapOutput(unittest.TestCase):
    def test_tap_output(self):   
        # Launches the tap process 
        tap_process = subprocess.Popen(['python3', 'tap.py', '-c', '../config.json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # wait 5 seconds for the tap to produce output
        time.sleep(2)

        #gets five lines of subprocess
        lines = []
        for i in range(5):
            lines.append(tap_process.stdout.readline().rstrip())

        # stop tap
        tap_process.kill()

        #prints tap output
        print(str(lines))
        #insert test assertion code

        # Validade that we have received output
        # assertGreaterEqual()unit testing in Python is an which is used in unit testing to check whether
        # the first given value is greater than or equal to the second value or not. 
        self.assertGreaterEqual(len(lines), 1, "No output received from tap process" )

        # Test schema output
        schema_msg = lines[0] #checking the firt position of dictionary
        self.assertEqual(schema_msg.get('type'), 'SCHEMA', "First message is not a schema message. Received type: '{}'".format(schema_msg.get('type')))
        self.assertEqual(schema_msg.get('stream'), 'movies', "Expected stream 'movies' but got: '{}'".format(schema_msg.get('stream')))

        expected_schema = {
            "properties": {
                "Title": {"type": "string"},
                "Year": {"type": "string"},
                "Rated": {"type": "string"},
                "Released": {"type": "string"},
                "Runtime": {"type": "string"},
                "Genre": {"type": "string"},
                "Director": {"type": "string"},
                "Writer": {"type": "string"},
                "Actors": {"type": "string"},
                "Plot": {"type": "string"},
                "Language": {"type": "string"},
                "Country": {"type": "string"},
                "Awards": {"type": "string"},
                "Poster": {"type": "string"},
                "imdbRating": {"type": "string"},
                "imdbVotes": {"type": "string"},
                "imdbID": {"type": "string"},
                "Type": {"type": "string"}
            },
            "type": "object"
        }

        self.assertEqual(schema_msg['schema'], expected_schema)

if __name__ == '__main__':
    unittest.main()        