# Ping CRM

A demo application to illustrate how Inertia.js works with:
- Server-side adapter: [inertia-masonite](https://github.com/girardinsamuel/inertia-masonite.git) for [MasoniteFramework](https://github.com/MasoniteFramework/masonite)
- Client-side adapter: [inertia.js]() for [Vue.js](https://github.com/vuejs/vue)

> ![](https://raw.githubusercontent.com/inertiajs/pingcrm/master/screenshot.png)

Disclaimer : the demo is based on the [official Inertia.js demo](https://github.com/inertiajs/pingcrm.git) (for the Vue part)

## Installation

Clone the repo locally:

```sh
https://github.com/girardinsamuel/pingcrm-masonite.git pingcrm
cd pingcrm
```

Install Python dependencies:

```sh
pip install -r requirements.txt
```

Install NPM dependencies:

```sh
npm ci
```

Build assets:

```sh
npm run dev
```

Setup configuration:

```sh
cp .env.example .env
```

Generate application key and add it to `APP_KEY` in `.env` file:

```sh
python craft key
```

Create an SQLite database. You can also use another database (MySQL, Postgres), simply update your configuration accordingly.

```sh
touch database/database.sqlite
```

Run database migrations:

```sh
python craft migrate
```

Run database seeder:

```sh
python craft seed ?
```

Run the dev server (the output will give the address):

```sh
python craft serve
```

You're ready to go! Visit Ping CRM in your browser, and login with:

- **Username:** johndoe@example.com
- **Password:** secret

## Running tests

There is no tests yet for this demo of Ping CRM.

