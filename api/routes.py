"""
API Routes
"""
from .principles_api import PrincipleResource, PrinciplesResource
from .core_values_api import CoreValueResource, CoreValuesResource
from api import api

api.add_resource(PrinciplesResource, "/principles")
api.add_resource(PrincipleResource, "/principles/<principle_id>")
api.add_resource(CoreValuesResource, "/values")
api.add_resource(CoreValueResource, "/values/<value_id>")