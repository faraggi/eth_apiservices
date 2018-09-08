import sys
import json
import requests
import datetime
import environ
import pytz

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from django.conf import settings

from ...models import Transaction

env = environ.Env()
tz = pytz.timezone(settings.TIME_ZONE)

GNOSIS_ADDR = '0x6810e776880c02933d47db1b9fc05908e5386b96'
ETHERSCAN_API_TOKEN = env('ETHERSCAN_API_TOKEN', default='')


class Command(BaseCommand):
    help = 'use requests to obtain the last etherscan tx'

    def add_arguments(self, parser):
       parser.add_argument('-A', '--addr', nargs='?', default=GNOSIS_ADDR)

    def handle(self, *args, **options):
        ten_txs = requests.get('https://api.etherscan.io/api?module=account&action=txlist&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&tag=latest&address={}&apikey={}'.format(options['addr'], ETHERSCAN_API_TOKEN))

        data = json.loads(ten_txs.text)

        for tx in data['result']:
            time = tx['timeStamp']
            timestamp = datetime.datetime.fromtimestamp(int(time))
            timestamp = tz.localize(timestamp)

            new_tx = Transaction(
                tx_hash=tx['hash'],
                block_hash=tx['blockHash'],
                timestamp=timestamp,
                from_addr=tx['from'],
                to_addr=tx['to'],
                value=tx['value'],
                gasusedbytx=tx['gasUsed'],
            )
            try:
                new_tx.save()
                print(new_tx.tx_hash)
                print(new_tx.block_hash)
                print(new_tx.timestamp)
            except IntegrityError:
                sys.stderr.write("ERROR: tx already exists\n")

        # for i in ten_txs.text:
        #     print(i)
        #     print('\n')
        # print('\n')

        # for only actual txs:
        # if contractAddress not empty:
        #   get stuff

        # r = requests.get(f'https://api.etherscan.io/api?module=account&action=balance&address={GNOSIS_ADDR}&tag=latest&apikey={ETHERSCAN_API_TOKEN}')
        # print(r.text)

        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
