# Space photo repository

Repo consists of few files with different functionality:
* `fetch_spacex_images.py` downloads SpaceX launch images.
* `fetch_nasa_apod_images.py` downloads NASA APOD (Astronomy Picture of the Day) images.
* `fetch_nasa_epic_images.py` downloads NASA EPIC (Earth Polychromatic Imaging Camera) images.
* `publish_image` publish image to Telegram channel.
* `permanent_publication` publish all images from the 'images' folder. One at a time after a time period.
* `download_images.py` contains auxiliary scripts

### How to install

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

#### Requirements to download NASA images

To download NASA images you need to get NASA API token. Go [here](https://api.nasa.gov/), generate your personal NASA API token.

This token you should put to a ```'.env'``` file. Create the file in the directory where the scripts located. Put this to the ``.env`` file:
```
NASA_API_KEY='Put_here_your_token'
```
#### Requirements to publish to Telegram

To publish images to Telegram you need to have your own Telegram channel, and you need a Telegram bot which should be an administrator of the channel.

* [How to create a bot](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram/) manual.
* [How to create a channel](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/) manual.

You should put the bot token and the channel id to the ```'.env'``` file. Create the file in the directory where the scripts located. Put this to the ``.env`` file:
```
TELEGRAM_BOT_TOKEN='Put_here_bot_token'
TELEGRAM_CHANNEL_ID='Put_here_channel_id'
```

### How to use
To execute script use terminal. 

#### Download SpaceX images
You can download images either from the latest launch or from specified launch. 

To download images from the latest launch execute this command from the project directory:
```
python fetch_spacex_images.py
```
Images will be downloaded to an 'images' folder. Keep in mind that there may not be images from the SpaceX launch.

If you want to specify launch, you should type in launch id argument. Like this:
```
python fetch_spacex_images.py --id=5eb87d47ffd86e000604b38a
```

#### Download NASA images
Make sure you've met **Requirements to download NASA images**

To download NASA APOD images run:
```
python fetch_nasa_apod_images.py
```
To download NASA EPIC images run:
```
python fetch_nasa_apod_images.py
```
In both cases images will be downloaded to an 'images' folder.

#### Publish images to telegram
Make sure you've met **Requirements to publish to Telegram.** Also, to publish images you need to have some of them in the "images" folder in the same directory where the scripts located.

To publish a random image from the folder run:
```
python publish_image.py
```
or you can specify local path to the image like this:
```
python publish_image.py --path=images/epic_1b_20230331220339.png
```

To start a permanent publication run:
```
python permanent_publication.py
```
By default, it will publish random image from the "images" folder every 4 hours. If you want to set up publication period, you should put it to the `.env` file in `HH:MM:SS` format. For example, to set up publication to publish an image every 1 hour and 30 minutes this should be in the `.env` file:
```
POSTING_TIME='01:30:00'
```
Also, you can set up publication pause when run the script like this:
```
python permanent_publication.py --pause=00:01:30
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).