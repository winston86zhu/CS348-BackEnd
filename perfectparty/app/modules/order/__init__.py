def init_api(api):
    base_url = '/order'

    from . import resources
    api.add_resource(resources.OrderResource, f'{base_url}')
