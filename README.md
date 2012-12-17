# SelfTrack
SelfTrack is a Python application, that runs in the background of your Linux box (sorry, no Windows or OS X) and pushes a few metrics to Cosm.

## Collected Metrics
* Number of browser tabs (Firefox only)
* loadavg
* CPU temperature
* Number of running processes
* Used memory
* Used swap space

## Usage
1. Copy `config.py.example` to `config.py`.
2. Create Cosm account (if applicable) and a new feed.
3. Enter an API key, the feed ID and the location of your `sessionstore.js` (for browser tabs) in `config.py`.
4. Run `python selftrack.py &`.

## Demo
Take a look at https://cosm.com/feeds/63631

## License
Licensed under MIT license. See LICENSE for details.