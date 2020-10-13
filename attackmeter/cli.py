import click

@click.command()
@click.option('--requests', '-r', default=500, help='number of requests')
@click.option('--concurrency', '-c', default=1, help='number of concurrent requests')
@click.option('--json-file', '-j', default=None, help='path to output JSON file')
@click.argument('url')
def cli(requests, concurrency, json_file, url):
    print(f'requests: {requests}')
    print(f'concurrency: {concurrency}')
    print(f'json_file: {json_file}')
    print(f'url: {url}')

if __name__ == '__main__':
    cli()

