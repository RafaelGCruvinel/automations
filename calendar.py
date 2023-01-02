import click
import os

from open_browser.google_utils import get_google_id


# SBF
# https://calendar.google.com/calendar/u/1/r?pli=1&authuser=0 padrão
# https://calendar.google.com/calendar/u/1/r?pli=1&authuser=2 angular
# https://calendar.google.com/calendar/u/1/r?pli=1&authuser=#ID_DESTINO#

# ANGULAR
# https://calendar.google.com/calendar/u/2/r?pli=1&authuser=0 padrão
# https://calendar.google.com/calendar/u/2/r?pli=1&authuser=1 sbf

# PADRÃO
# https://calendar.google.com/calendar/u/0/r?pli=1&authuser=1 sbf
# https://calendar.google.com/calendar/u/0/r?pli=1&authuser=2 angular

@click.command()
@click.option("--enterprise", help="Number of greetings.")
def calendar(enterprise):

    google_id = get_google_id(enterprise)

    url = f'https://calendar.google.com/calendar/u/{google_id}/r'

    os.system(f'start {url}')

    click.echo(f"Abrindo calendário [{enterprise.capitalize()}] {url}!")

main = calendar

if __name__ == '__main__':
    import sys

    print(sys.argv)
    main()
