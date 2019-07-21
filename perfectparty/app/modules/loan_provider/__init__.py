def init_api(api):
    base_url = '/loanprovider'

    from . import resources
    api.add_resource(resources.LPResource, f'{base_url}')
