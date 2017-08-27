# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from mock import Mock
import random

class Object:
    objects = Mock()
    def __init__(self, **kwargs):
        for (k,v) in kwargs.items():
            setattr(self,k,v)

        setattr(self, 'save', Mock())
        setattr(self, 'delete', Mock())
        setattr(self, 'backend_code', 0)
        setattr(self, 'id', 98052)

    def tologdict(self):
        return {}

class ONOSService(Object):
    pass

class ONOSTenant(Object):
    pass

class ModelAccessor:
    def check_db_connection_ok(self):
        return True

    def fetch_pending(self, model, deleted = False):
        num = random.randint(1,5)
        object_list = []

        for i in range(num):
            if isinstance(model, list):
                model = model[0]

            try:
                obj = model()
            except:
                import pdb
                pdb.set_trace()

            obj.name = "Opinionated Berry %d"%i
            object_list.append(obj)
        
        return object_list

model_accessor = ModelAccessor()

#####
# DO NOT MODIFY THE CLASSES BELOW. THEY ARE AUTOGENERATED.
# 

class XOSBase(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "Provisioning in progress"
    backend_code = 0
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    
    leaf_model_name = "XOSBase"
class User(Object):
    email = None
    username = "Something"
    password = "Something"
    last_login = None
    firstname = None
    lastname = None
    phone = None
    user_url = None
    site = None
    public_key = None
    is_active = True
    is_admin = False
    is_staff = True
    is_readonly = False
    is_registering = False
    is_appuser = False
    login_page = None
    created = None
    updated = None
    enacted = None
    policed = None
    backend_status = "Provisioning in progress"
    backend_need_delete = False
    backend_need_reap = False
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    timezone = "America/New_York"
    dashboards = None
    policy_status = "0 - Policy in process"
    
    leaf_model_name = "User"
class Privilege(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    accessor_id = None
    accessor_type = None
    controller_id = None
    object_id = None
    object_type = None
    permission = "all"
    granted = None
    expires = None
    
    leaf_model_name = "Privilege"
class AddressPool(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    addresses = None
    gateway_ip = None
    gateway_mac = None
    cidr = None
    inuse = None
    service = None
    
    leaf_model_name = "AddressPool"
class Controller(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    backend_type = None
    version = None
    auth_url = None
    admin_user = None
    admin_password = None
    admin_tenant = None
    domain = None
    rabbit_host = None
    rabbit_user = None
    rabbit_password = None
    deployment = None
    
    leaf_model_name = "Controller"
class ControllerDashboardView(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    controller = None
    dashboardView = None
    enabled = True
    url = None
    
    leaf_model_name = "ControllerDashboardView"
class ControllerImages(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    image = None
    controller = None
    glance_image_id = None
    
    leaf_model_name = "ControllerImages"
class ControllerNetwork(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    network = None
    controller = None
    subnet = None
    start_ip = None
    stop_ip = None
    net_id = None
    router_id = None
    subnet_id = None
    gateway = None
    segmentation_id = None
    
    leaf_model_name = "ControllerNetwork"
class ControllerRole(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    role = None
    
    leaf_model_name = "ControllerRole"
class ControllerSite(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    site = None
    controller = None
    tenant_id = None
    
    leaf_model_name = "ControllerSite"
class ControllerPrivilege(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    controller = None
    privilege = None
    role_id = None
    
    leaf_model_name = "ControllerPrivilege"
class ControllerSitePrivilege(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    controller = None
    site_privilege = None
    role_id = None
    
    leaf_model_name = "ControllerSitePrivilege"

class ControllerSlice(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    controller = None
    slice = None
    tenant_id = None
    
    leaf_model_name = "ControllerSlice"
class ControllerSlicePrivilege(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    controller = None
    slice_privilege = None
    role_id = None
    
    leaf_model_name = "ControllerSlicePrivilege"
class ControllerUser(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    user = None
    controller = None
    kuser_id = None
    
    leaf_model_name = "ControllerUser"
class DashboardView(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    url = None
    enabled = True
    icon = "default-icon.png"
    icon_active = "default-icon-active.png"
    controllers = None
    deployments = None
    
    leaf_model_name = "DashboardView"
class Deployment(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    accessControl = "allow all"
    
    leaf_model_name = "Deployment"
class DeploymentPrivilege(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    user = None
    deployment = None
    role = None
    
    leaf_model_name = "DeploymentPrivilege"
class DeploymentRole(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    role = None
    
    leaf_model_name = "DeploymentRole"
class Diag(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    
    leaf_model_name = "Diag"
class Flavor(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    description = None
    flavor = None
    
    leaf_model_name = "Flavor"
class Image(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    kind = "vm"
    disk_format = None
    container_format = None
    path = None
    tag = None
    
    leaf_model_name = "Image"
class ImageDeployments(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    image = None
    deployment = None
    
    leaf_model_name = "ImageDeployments"
class Instance(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    instance_id = None
    instance_uuid = None
    name = None
    instance_name = None
    ip = None
    image = None
    creator = None
    slice = None
    deployment = None
    node = None
    numberCores = 0
    flavor = None
    userData = None
    isolation = "vm"
    volumes = None
    parent = None
    
    leaf_model_name = "Instance"
class Network(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    template = None
    subnet = None
    start_ip = None
    end_ip = None
    ports = None
    labels = None
    owner = None
    permit_all_slices = False
    autoconnect = True
    permitted_slices = None
    slices = None
    instances = None
    
    leaf_model_name = "Network"
class NetworkParameter(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    parameter = None
    value = None
    content_type = None
    object_id = None
    
    leaf_model_name = "NetworkParameter"
class NetworkParameterType(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    description = None
    
    leaf_model_name = "NetworkParameterType"
class NetworkSlice(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    network = None
    slice = None
    
    leaf_model_name = "NetworkSlice"
class NetworkTemplate(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    description = None
    visibility = "private"
    translation = "none"
    access = None
    shared_network_name = None
    shared_network_id = None
    topology_kind = "bigswitch"
    controller_kind = None
    vtn_kind = "PRIVATE"
    
    leaf_model_name = "NetworkTemplate"
class Node(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    site_deployment = None
    
    leaf_model_name = "Node"
class NodeLabel(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    node = None
    
    leaf_model_name = "NodeLabel"
class Port(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    network = None
    instance = None
    ip = None
    port_id = None
    mac = None
    xos_created = False
    
    leaf_model_name = "Port"
class Role(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    role_type = None
    role = None
    description = None
    
    leaf_model_name = "Role"
class Service(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    description = None
    enabled = True
    kind = "generic"
    name = None
    versionNumber = None
    published = True
    view_url = None
    icon_url = None
    public_key = None
    private_key_fn = None
    service_specific_id = None
    service_specific_attribute = None
    
    leaf_model_name = "Service"
class ServiceAttribute(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    value = None
    service = None
    
    leaf_model_name = "ServiceAttribute"
class ServiceDependency(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    provider_service = None
    subscriber_service = None
    connect_method = "none"
    
    leaf_model_name = "ServiceDependency"
class ServiceMonitoringAgentInfo(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    service = None
    target_uri = None
    
    leaf_model_name = "ServiceMonitoringAgentInfo"
class ServicePrivilege(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    user = None
    service = None
    role = None
    
    leaf_model_name = "ServicePrivilege"
class ServiceRole(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    role = None
    
    leaf_model_name = "ServiceRole"
class Site(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    site_url = None
    enabled = True
    hosts_nodes = True
    hosts_users = True
    longitude = None
    latitude = None
    login_base = None
    is_public = True
    abbreviated_name = None
    deployments = None
    
    leaf_model_name = "Site"
class SiteDeployment(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    site = None
    deployment = None
    controller = None
    availability_zone = None
    
    leaf_model_name = "SiteDeployment"
class SitePrivilege(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    user = None
    site = None
    role = None
    
    leaf_model_name = "SitePrivilege"
class SiteRole(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    role = None
    
    leaf_model_name = "SiteRole"
class Slice(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    enabled = True
    description = None
    slice_url = None
    site = None
    max_instances = 10
    service = None
    network = None
    exposed_ports = None
    creator = None
    default_flavor = None
    default_image = None
    default_node = None
    mount_data_sets = "GenBank"
    default_isolation = "vm"
    
    leaf_model_name = "Slice"
class SlicePrivilege(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    user = None
    slice = None
    role = None
    
    leaf_model_name = "SlicePrivilege"
class SliceRole(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    role = None
    
    leaf_model_name = "SliceRole"
class Tag(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    service = None
    name = None
    value = None
    content_type = None
    object_id = None
    
    leaf_model_name = "Tag"
class InterfaceType(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    direction = None
    
    leaf_model_name = "InterfaceType"
class ServiceInterface(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    service = None
    interface_type = None
    
    leaf_model_name = "ServiceInterface"
class ServiceInstance(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    owner = None
    service_specific_id = None
    service_specific_attribute = None
    
    leaf_model_name = "ServiceInstance"
class ServiceInstanceLink(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    provider_service_instance = None
    provider_service_interface = None
    subscriber_service_instance = None
    subscriber_service = None
    subscriber_network = None
    
    leaf_model_name = "ServiceInstanceLink"
class ServiceInstanceAttribute(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    value = None
    service_instance = None
    
    leaf_model_name = "ServiceInstanceAttribute"
class TenantWithContainer(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    owner = None
    service_specific_id = None
    service_specific_attribute = None
    instance = None
    creator = None
    external_hostname = None
    external_container = None
    
    leaf_model_name = "TenantWithContainer"
class XOS(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = "XOS"
    
    leaf_model_name = "XOS"
class XOSGuiExtension(Object):
    created = None
    updated = "now()"
    enacted = None
    policed = None
    backend_register = "{}"
    backend_need_delete = False
    backend_need_reap = False
    backend_status = "0 - Provisioning in progress"
    deleted = False
    write_protect = False
    lazy_blocked = False
    no_sync = False
    no_policy = False
    policy_status = "0 - Policy in process"
    leaf_model_name = None
    name = None
    files = None
    
    leaf_model_name = "XOSGuiExtension"


