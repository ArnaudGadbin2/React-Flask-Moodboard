# React-Flask-Moodboard

## Description

Backend and Frontend describing a small moodboard project, where you can add texts and images, and drag them where you want.
Text and Images are saved in a postgres DB in a docker image.
The images will be different on reload because I use a random image url, the texts will be the same.

## Running the Front

1 - Go to front folder:

```bash
$ cd front/moodboard/
```

2 - Install dependencies:

```bash
$ npm i
```

3 - Launch App:

```bash
$ npm start
```

4 - Open App:

The app is available at http://localhost:3000

## Running the Back

1 - Go to back folder:

```bash
$ cd back/
```

2 - Launch Docker:

```bash
$ docker compose up --build
```

3 - Availability:

The api is available at http://localhost:8080
