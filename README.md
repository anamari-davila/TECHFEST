![logo](/assets/Logo.png)

# World of Cinema

World of Cinema is a Python desktop application built with **Flet** that simulates a fictional movie theater. The program displays movies currently playing in theaters using data from the TMDB API and allows users to browse films, choose screening dates and times, and select seats.

This project was created for **Techfest**, a school technology festival. Techfest is the event where the project was developed and presented; it is not the name of the program.

## Features

- Browse currently playing movies from TMDB.
- View movie information in a graphical interface.
- Select screening dates and times.
- Choose seats for a screening.
- Display ticket pricing information, with pricing logic still in development.
  
## Requirements 

Before running the project, make sure you have:

- Python 3.10 or newer installed.
- `flet` version 0.26.x or 0.27.x installed.
- `python-dotenv` installed.
- A TMDB account and API Read Access Token.

## Installation

Install the required dependencies:

```bash
pip install flet==0.27.6
pip install python-dotenv
```

## TMDB API setup

### 1. Create a TMDB account
Create an account at [TMDB](https://www.themoviedb.org)

### 2. Get your API token
Go to your account settings page and then select 'API':

https://www.themoviedb.org/settings/api

and keep following the steps shown there till you get your "API Read Access Token" generated

### 3. Create a `.env` file
In the same folder as your main Python file, create a file named `.env.`.

Example:

```env
TMDB_API_TOKEN = here your read access token
```

## Running the program

After setting up the `.env` file, run the application from the project folder:

```bash
python main.py
```
PD: For now it has a different name but the main file will be changed to main.py

## Notes

- This app uses Flet for the graphical user interface.
- Use Flet `0.26.x` or `0.27.x`, since newer versions or older might introduce compatibility changes regarding controls.
- Ticket pricing is currently a work in progress and will be updated in the future.


## Disclaimers

This project uses the TMDB API but is not endorsed or certified by TMDB. This repository is intended for educational and non-commercial use only. Users are responsible for complying with TMDB’s Terms of Use and attribution requirements.

<img width="200" height="150" alt="image" src="https://github.com/user-attachments/assets/cd495b7b-5ce7-4f9b-829c-8a32ce8db984" />  


