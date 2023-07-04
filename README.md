# AsyncPGPromise

## Motivation

The creation of AsyncPGPromise was primarily driven by an aspiration to bring the clean API and named arguments support, common in Node.js' `pg-promise``, to the Python ecosystem. The lack of such an approach in Python became more pronounced upon transitioning from Node.js, sparking the motivation to develop a solution. With Python's ultra-fast writing mold being a major encouraging factor, this tiny wrapper, AsyncPGPromise, was brought into existence to fill this gap and to provide a sleek and efficient means of handling PostgreSQL database operations.

## Features

- Simplicity: By using named arguments in your SQL queries, you can keep your code clean and readable.
- Flexibility: All the power of the `asyncpg` library is still at your fingertips, with additional convenience provided by AsyncPGPromise.

## Installation

```bash
pip install asyncpgpromise
```

## Getting Started

You can create a new `AsyncPGPromise` instance with an existing `asyncpg` connection object:

```python
from asyncpgpromise import AsyncPGPromise
import asyncpg

# First create an asyncpg connection
conn = await asyncpg.connect(user='user', password='password', database='database', host='127.0.0.1')

# Then pass it to AsyncPGPromise
pg = AsyncPGPromise(conn)
```

## Usage

### Querying

You can perform SQL queries with named arguments:

```python
rows = await pg.query('SELECT * FROM users WHERE name = $name', name='John')
```

The `query` method returns a list of dictionaries, each representing a row from the SQL query.

### Fetching One Row

If you're only expecting a single row result, you can use the `one` method:

```python
row = await pg.one('SELECT * FROM users WHERE id = $id', id=1)
```

## Note

This is a new project and may still have some rough edges. Contributions are very welcome!

## To-Do

- [ ] Parsing of fields with JSON data

## License

AsyncPGPromise is available under the MIT license. See the LICENSE file for more info.
