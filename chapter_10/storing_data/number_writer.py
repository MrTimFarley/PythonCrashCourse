from pathlib import Path
import json


numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)