def init_api(api):
    base_url = '/suppliers'

    from . import resources
    api.add_resource(resources.SupplierResource, f'{base_url}')
