def init_api(api):
    base_url = '/event'

    from . import resources
    api.add_resource(resources.EventResource, f'{base_url}')
    api.add_resource(resources.SpecificEventResource, f'{base_url}/<event_id>')
