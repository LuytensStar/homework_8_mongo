import redis

from models import Quote, Author
import connect
from redis import Redis


while True:
    raw_command = input('Command:')

    if ':' in raw_command:
        command, value = raw_command.split(':')
        value= value.strip().lower()
        print(value)
    else:
        command = raw_command.strip()

    if command == 'name':
        author_list = [author.fullname.lower() for author in Author.objects()]
        if value in author_list:
            for quote in Quote.objects(author = Author.objects(fullname__iexact=value).first().id):
                print(quote.quote)
        else:
            print('No quote with this author')
    elif command == 'tag':
        for quote in Quote.objects(tags__in = [value]):
            print(quote.quote)

    elif command == 'tags':
        tags = value.split(',')
        print(tags)
        for quote in Quote.objects(tags__in = tags):
            print(quote.quote)


    elif command == "exit":
        break


