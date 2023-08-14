# Tech2335_Final_Book-Suggestions

## Setup

Obtain an [BOOKS API Key](https://developers.google.com/books/docs/v1/using):

```sh
# this is the ".env" file (in the root directory of the repo)

BOOKS_API_KEY="____________"
```

Create a virtual environment:

```sh
conda create -n book_suggestions-env python=3.10
```

```sh
conda activate book_suggestions-env
```

Install third-party packages:

```sh
pip install -r requirements.txt
```

## Usage

Run the book suggestions report:

```sh
python -m app.book_suggestions
```

## Testing

```sh
pytest
```

## [Deployment Guide](/DEPLOYING.md)