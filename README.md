# ethereum_apiservices
## Etherum API services using DRF

Just a simple test project for sotring eth txs in a lcoal database and having rest endpoints getting the info

This is only for testing purposes, but if anyone wants to try it out, the inital command for importing 10 txs from an address is a custom management command:

- makemirgations
- migrate
- `./manage.py get_last_etherscan_tx [optional -A addr]` # where addr is an eth address

after this, the endpoints for the API are;

- `/transactions` for a list of all txs
- `/transactions/new` for a creation form
