def init_api(api):
    base_url = '/supply'

    from . import resources
    api.add_resource(resources.SupplyResource, f'{base_url}')
    api.add_resource(resources.SpecificSupplyResource, f'{base_url}/<int:item_id>')
