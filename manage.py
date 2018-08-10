from gevent import monkey; monkey.patch_all()

from werkzeug.serving import run_with_reloader
from gevent import pywsgi as wsgi
from TodoAPI.app import app as todoAPI
# from TodoAPI.tests import run as run_tests

import click
import gevent

@click.group()
def cli():
    pass

@cli.command()
@click.option('--reloader/--no-reloader', '-r', default=False)
def serve(reloader):
    def run(): 
        wsgi.WSGIServer(('0.0.0.0', 8080), todoAPI).serve_forever()
    
    if reloader:
        run_with_reloader(run)
    else:
        run()

if __name__ == '__main__':
    cli()