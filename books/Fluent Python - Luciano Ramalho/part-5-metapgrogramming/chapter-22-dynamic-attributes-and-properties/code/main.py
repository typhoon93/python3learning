from explore0 import FrozenJSON

import json
raw_feed = json.load(open('data/osconfeed.json'))
feed = FrozenJSON(raw_feed)
print(
len(feed.Schedule.speakers)
)

