def init_api(api):
    base_url = '/loanprovider'

    from . import resources
    api.add_resource(resources.LoanProviderResource, f'{base_url}')
