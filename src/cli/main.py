import click
from book_requests import get_book, get_books_by_topic, buy_book

@click.group()
def bookstore():
    click.echo("Welcome to the World's Smallest Book Store!")

@click.command()
@click.argument("item_number", required=True)
def lookup(item_number: int):
    click.echo(f"Looking up item number {item_number}...")
    try:
        book = get_book(item_number)
    except Exception as e:
        click.echo(str(e), err=True)
        return
    click.echo(book)

@click.command()
@click.option("--topic", required=True, help="The topic of the books to search for.")
def search(topic: str):
    click.echo(f"Searching for all the books related to topic {topic}...")
    try:
        books = get_books_by_topic(topic)
    except Exception as e:
        click.echo(str(e), err=True)
        return
    click.echo(books)
    

@click.command()
@click.argument("item_number", required=True)
def buy(item_number: int):
    click.echo(f"Looking up item number {item_number}...")
    try:
        book = buy_book(item_number)
    except Exception as e:
        click.echo(str(e), err=True)
        return
    click.echo("Hooray! You bought the book.")
    click.echo(book)

bookstore.add_command(lookup)
bookstore.add_command(search)
bookstore.add_command(buy)

if __name__ == '__main__':
    bookstore()

