# 🎵 Spotify Songs Analysis

A Python script to analyze and explore music data from Spotify's API. This project creates a .csv file and a .json file with the ID of the artist, name of the artist, ID of the albums, name of the albums and name of the songs of an artist that is introduced by script.

## 📁 Project Structure
* canciones.py (the main Python script)
* README.md (the documentation)

### ¡Important! Set up Spotify API credentials

You must create a file named variables.py and add there your own credentials in this way:
    id="your_client_id"
    secret="your_secret"
    uri="the_uri"

## 📁 The script will:

- Authenticate with Spotify API
- Ask you to insert the name of an artist
- Generate the artist´s albums and the songs
- Save the artist´s id and name, the album´s id and name and the song´s names into a .csv file and a .json file

Note: Remember to keep your Spotify API credentials secure and never commit them to version control.
