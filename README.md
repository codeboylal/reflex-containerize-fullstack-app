# Customer Data App

This app is used to showcase and edit tabular data live in an app. It links up with a persistent database, such as [Neon](https://neon.tech). 

## Usage 

First clone the repo locally.
```bash
git clone https://github.com/codeboylal/reflex-containerize-fullstack-app/tree/main
```
Then set up a virtual environment as outlined in our documentation. After this run `pip install -r requirements.txt`.

Next run the following reflex commands in your terminal:

```bash
reflex init
```

```bash
reflex db migrate
```

```bash
reflex run
```

The `init` command initializes the app. The `db migrate` command migrates your database. The `run` command runs your app.


## Setting an external Database

It is also possibe to set an external database so that your data is not lost every time the app closes and so you can deploy your app and maintain data. 

In the `rxconfig.py` file we accept a `DATABASE_URL` environment variable. 

To set one run the following command in your terminal:

```bash
export DATABASE_URL="<YOUR URL KEY>"
```

## Host Application in Docker

You may host your application with just simple docker command.

First clone the repo locally.
```bash
git clone https://github.com/codeboylal/reflex-containerize-fullstack-app/tree/main
```

Run the following commands
```bash
cd reflex-containerize-fullstack-app
```

```bash
docker-compose up --build
```

To see docker images

```bash
docker images
```

To list running processes
```bash
docker ps
```

Access your application
- Frontend:
```bash
[Frontend] (http://localhost:3000)
```

- Backend:
```bash
[Backend] (http://localhost:8000)
```





