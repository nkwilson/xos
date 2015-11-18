import os
import sys
from django.db.models import Q, F
from helloworldservice.models import HelloWorldService, HelloWorldTenant
from observers.base.SyncInstanceUsingAnsible import SyncInstanceUsingAnsible

parentdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, parentdir)

class SyncHelloWorldServiceTenant(SyncInstanceUsingAnsible):
    provides = [HelloWorldTenant]
    observes = HelloWorldTenant
    requested_interval = 0
    template_name = "sync_helloworldtenant.yaml"
    service_key_name = "/opt/xos/observers/helloworldservice/helloworldservice_private_key"

    def __init__(self, *args, **kwargs):
        super(SyncHelloWorldServiceTenant, self).__init__(*args, **kwargs)

    def fetch_pending(self, deleted):
        if (not deleted):
            objs = HelloWorldTenant.get_tenant_objects().filter(Q(enacted__lt=F('updated')) | Q(enacted=None),Q(lazy_blocked=False))
        else:
            objs = HelloWorldTenant.get_deleted_tenant_objects()

        return objs

    def get_extra_attributes(self, o):
    	return {"display_message": o.display_message}

    def run_playbook(self, o, fields):
        super(SyncHelloWorldServiceTenant, self).run_playbook(o, fields)

    def delete_record(self, m):
        pass
