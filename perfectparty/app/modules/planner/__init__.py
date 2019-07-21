def init_api(api):
    base_url = '/planners'

    from . import resources
    api.add_resource(resources.PlannerResource, f'{base_url}')
