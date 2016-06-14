"use strict";!function(){angular.module("xos.uiComponents",["chart.js","RecursionHelper"])}();var _typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol?"symbol":typeof e};!function(){angular.module("xos.uiComponents").directive("xosSmartTable",function(){return{restrict:"E",scope:{config:"="},template:'\n        <div class="row" ng-show="vm.data.length > 0">\n          <div class="col-xs-12 text-right">\n            <a href="" class="btn btn-success" ng-click="vm.createItem()">\n              Add\n            </a>\n          </div>\n        </div>\n        <div class="row">\n          <div class="col-xs-12 table-responsive">\n            <xos-table config="vm.tableConfig" data="vm.data"></xos-table>\n          </div>\n        </div>\n        <div class="panel panel-default" ng-show="vm.detailedItem">\n          <div class="panel-heading">\n            <div class="row">\n              <div class="col-xs-11">\n                <h3 class="panel-title" ng-show="vm.detailedItem.id">Update {{vm.config.resource}} {{vm.detailedItem.id}}</h3>\n                <h3 class="panel-title" ng-show="!vm.detailedItem.id">Create {{vm.config.resource}} item</h3>\n              </div>\n              <div class="col-xs-1">\n                <a href="" ng-click="vm.cleanForm()">\n                  <i class="glyphicon glyphicon-remove pull-right"></i>\n                </a>\n              </div>\n            </div>\n          </div>\n          <div class="panel-body">\n            <xos-form config="vm.formConfig" ng-model="vm.detailedItem"></xos-form>\n          </div>\n        </div>\n        <xos-alert config="{type: \'success\', closeBtn: true}" show="vm.responseMsg">{{vm.responseMsg}}</xos-alert>\n        <xos-alert config="{type: \'danger\', closeBtn: true}" show="vm.responseErr">{{vm.responseErr}}</xos-alert>\n      ',bindToController:!0,controllerAs:"vm",controller:["$injector","LabelFormatter","_","XosFormHelpers",function(e,n,o,t){var i=this;this.responseMsg=!1,this.responseErr=!1,this.tableConfig={columns:[],actions:[{label:"delete",icon:"remove",cb:function(e){i.Resource["delete"]({id:e.id}).$promise.then(function(){o.remove(i.data,function(n){return n.id===e.id}),i.responseMsg=i.config.resource+" with id "+e.id+" successfully deleted"})["catch"](function(n){i.responseErr=n.data.detail||"Error while deleting "+i.config.resource+" with id "+e.id})},color:"red"},{label:"details",icon:"search",cb:function(e){i.detailedItem=e}}],classes:"table table-striped table-bordered table-responsive",filter:"field",order:!0,pagination:{pageSize:10}},this.formConfig={exclude:this.config.hiddenFields,fields:{},formName:this.config.resource+"Form",actions:[{label:"Save",icon:"ok",cb:function(e){var n=void 0,o=!0;e.id?(n=e.$update(),o=!1):n=e.$save(),n.then(function(n){o&&i.data.push(angular.copy(n)),delete i.detailedItem,i.responseMsg=i.config.resource+" with id "+e.id+" successfully saved"})["catch"](function(n){i.responseErr=n.data.detail||"Error while saving "+i.config.resource+" with id "+e.id})},"class":"success"}]},this.cleanForm=function(){delete i.detailedItem},this.createItem=function(){i.detailedItem=new i.Resource},this.Resource=e.get(this.config.resource);var r=function(){i.Resource.query().$promise.then(function(e){if(e[0]){var r=e[0],s=Object.keys(r);o.remove(s,function(e){return"id"===e||"validators"===e}),angular.isArray(i.config.hiddenFields)&&(s=o.difference(s,i.config.hiddenFields));var a=s.map(function(e){return n.format(e)});s.forEach(function(e,n){var o={label:a[n],prop:e};"string"!=typeof r[e]&&"undefined"!=typeof r[e]&&(o.type=_typeof(r[e])),i.tableConfig.columns.push(o)}),s.forEach(function(e,o){i.formConfig.fields[e]={label:n.format(a[o]).replace(":",""),type:t._getFieldFormat(r[e])}}),i.data=e}})};r()}]}})}(),function(){angular.module("xos.uiComponents").directive("xosSmartPie",function(){return{restrict:"E",scope:{config:"="},template:'\n        <canvas\n          class="chart chart-pie {{vm.config.classes}}"\n          chart-data="vm.data" chart-labels="vm.labels"\n          chart-legend="{{vm.config.legend}}">\n        </canvas>\n      ',bindToController:!0,controllerAs:"vm",controller:["$injector","$interval","$scope","$timeout","_",function(e,n,o,t,i){var r=this;if(!this.config.resource&&!this.config.data)throw new Error("[xosSmartPie] Please provide a resource or an array of data in the configuration");var s=function(e){return i.groupBy(e,r.config.groupBy)},a=function(e){return i.reduce(Object.keys(e),function(n,o){return n.concat(e[o].length)},[])},l=function(e){return angular.isFunction(r.config.labelFormatter)?r.config.labelFormatter(Object.keys(e)):Object.keys(e)},c=function(e){var n=s(e);r.data=a(n),r.labels=l(n)};this.config.resource?!function(){r.Resource=e.get(r.config.resource);var o=function(){r.Resource.query().$promise.then(function(e){e[0]&&c(e)})};o(),r.config.poll&&n(function(){o()},1e3*r.config.poll)}():o.$watch(function(){return r.config.data},function(e){e&&c(r.config.data)},!0),o.$on("create",function(e,n){console.log("create: "+n.id)}),o.$on("destroy",function(e,n){console.log("destroy: "+n.id)})}]}})}(),function(){angular.module("xos.uiComponents").directive("xosValidation",function(){return{restrict:"E",scope:{field:"=",form:"="},template:'\n        <div ng-cloak>\n          <xos-alert config="vm.config" show="vm.field.$error.required !== undefined && vm.field.$error.required !== false  && (vm.field.$touched || vm.form.$submitted)">\n            Field required\n          </xos-alert>\n          <xos-alert config="vm.config" show="vm.field.$error.email !== undefined && vm.field.$error.email !== false && (vm.field.$touched || vm.form.$submitted)">\n            This is not a valid email\n          </xos-alert>\n          <xos-alert config="vm.config" show="vm.field.$error.minlength !== undefined && vm.field.$error.minlength !== false && (vm.field.$touched || vm.form.$submitted)">\n            Too short\n          </xos-alert>\n          <xos-alert config="vm.config" show="vm.field.$error.maxlength !== undefined && vm.field.$error.maxlength !== false && (vm.field.$touched || vm.form.$submitted)">\n            Too long\n          </xos-alert>\n          <xos-alert config="vm.config" show="vm.field.$error.custom !== undefined && vm.field.$error.custom !== false && (vm.field.$touched || vm.form.$submitted)">\n            Field invalid\n          </xos-alert>\n        </div>\n      ',transclude:!0,bindToController:!0,controllerAs:"vm",controller:function(){this.config={type:"danger"}}}})}(),function(){angular.module("xos.uiComponents").directive("xosPagination",function(){return{restrict:"E",scope:{pageSize:"=",totalElements:"=",change:"="},template:'\n        <div class="row" ng-if="vm.pageList.length > 1">\n          <div class="col-xs-12 text-center">\n            <ul class="pagination">\n              <li\n                ng-click="vm.goToPage(vm.currentPage - 1)"\n                ng-class="{disabled: vm.currentPage == 0}">\n                <a href="" aria-label="Previous">\n                    <span aria-hidden="true">&laquo;</span>\n                </a>\n              </li>\n              <li ng-repeat="i in vm.pageList" ng-class="{active: i === vm.currentPage}">\n                <a href="" ng-click="vm.goToPage(i)">{{i + 1}}</a>\n              </li>\n              <li\n                ng-click="vm.goToPage(vm.currentPage + 1)"\n                ng-class="{disabled: vm.currentPage == vm.pages - 1}">\n                <a href="" aria-label="Next">\n                    <span aria-hidden="true">&raquo;</span>\n                </a>\n              </li>\n            </ul>\n          </div>\n        </div>\n      ',bindToController:!0,controllerAs:"vm",controller:["$scope",function(e){var n=this;this.currentPage=0,this.goToPage=function(e){0>e||e===n.pages||(n.currentPage=e,n.change(e))},this.createPages=function(e){for(var n=[],o=0;e>o;o++)n.push(o);return n},e.$watch(function(){return n.totalElements},function(){n.totalElements&&(n.pages=Math.ceil(n.totalElements/n.pageSize),n.pageList=n.createPages(n.pages))})}]}}).filter("pagination",function(){return function(e,n){return e&&angular.isArray(e)?(n=parseInt(n,10),e.slice(n)):e}})}(),function(){angular.module("xos.uiComponents").directive("xosTable",function(){return{restrict:"E",scope:{data:"=",config:"="},template:'\n          <div ng-show="vm.data.length > 0">\n            <div class="row" ng-if="vm.config.filter == \'fulltext\'">\n              <div class="col-xs-12">\n                <input\n                  class="form-control"\n                  placeholder="Type to search.."\n                  type="text"\n                  ng-model="vm.query"/>\n              </div>\n            </div>\n            <table ng-class="vm.classes" ng-hide="vm.data.length == 0">\n              <thead>\n                <tr>\n                  <th ng-repeat="col in vm.columns">\n                    {{col.label}}\n                    <span ng-if="vm.config.order">\n                      <a href="" ng-click="vm.orderBy = col.prop; vm.reverse = false">\n                        <i class="glyphicon glyphicon-chevron-up"></i>\n                      </a>\n                      <a href="" ng-click="vm.orderBy = col.prop; vm.reverse = true">\n                        <i class="glyphicon glyphicon-chevron-down"></i>\n                      </a>\n                    </span>\n                  </th>\n                  <th ng-if="vm.config.actions">Actions:</th>\n                </tr>\n              </thead>\n              <tbody ng-if="vm.config.filter == \'field\'">\n                <tr>\n                  <td ng-repeat="col in vm.columns">\n                    <input\n                      ng-if="col.type !== \'boolean\'"\n                      class="form-control"\n                      placeholder="Type to search by {{col.label}}"\n                      type="text"\n                      ng-model="vm.query[col.prop]"/>\n                    <select\n                      ng-if="col.type === \'boolean\'"\n                      class="form-control"\n                      ng-model="vm.query[col.prop]">\n                      <option value="">-</option>\n                      <option value="true">True</option>\n                      <option value="false">False</option>\n                    </select>\n                  </td>\n                  <td ng-if="vm.config.actions"></td>\n                </tr>\n              </tbody>\n              <tbody>\n                <tr ng-repeat="item in vm.data | filter:vm.query | orderBy:vm.orderBy:vm.reverse | pagination:vm.currentPage * vm.config.pagination.pageSize | limitTo: (vm.config.pagination.pageSize || vm.data.length) track by $index">\n                  <td ng-repeat="col in vm.columns" link-wrapper>\n                    <span ng-if="!col.type">{{item[col.prop]}}</span>\n                    <span ng-if="col.type === \'boolean\'">\n                      <i class="glyphicon"\n                        ng-class="{\'glyphicon-ok\': item[col.prop], \'glyphicon-remove\': !item[col.prop]}">\n                      </i>\n                    </span>\n                    <span ng-if="col.type === \'date\'">\n                      {{item[col.prop] | date:\'H:mm MMM d, yyyy\'}}\n                    </span>\n                    <span ng-if="col.type === \'array\'">\n                      {{item[col.prop] | arrayToList}}\n                    </span>\n                    <span ng-if="col.type === \'object\'">\n                      <dl class="dl-horizontal">\n                        <span ng-repeat="(k,v) in item[col.prop]">\n                          <dt>{{k}}</dt>\n                          <dd>{{v}}</dd>\n                        </span>\n                      </dl>\n                    </span>\n                    <span ng-if="col.type === \'custom\'">\n                      {{col.formatter(item)}}\n                    </span>\n                    <span ng-if="col.type === \'icon\'">\n                      <i class="glyphicon glyphicon-{{col.formatter(item)}}">\n                      </i>\n                    </span>\n                  </td>\n                  <td ng-if="vm.config.actions">\n                    <a href=""\n                      ng-repeat="action in vm.config.actions"\n                      ng-click="action.cb(item)"\n                      title="{{action.label}}">\n                      <i\n                        class="glyphicon glyphicon-{{action.icon}}"\n                        style="color: {{action.color}};"></i>\n                    </a>\n                  </td>\n                </tr>\n              </tbody>\n            </table>\n            <xos-pagination\n              ng-if="vm.config.pagination"\n              page-size="vm.config.pagination.pageSize"\n              total-elements="vm.data.length"\n              change="vm.goToPage">\n              </xos-pagination>\n          </div>\n          <div ng-show="vm.data.length == 0 || !vm.data">\n             <xos-alert config="{type: \'info\'}">\n              No data to show.\n            </xos-alert>\n          </div>\n        ',bindToController:!0,controllerAs:"vm",controller:["_",function(e){var n=this;if(!this.config)throw new Error('[xosTable] Please provide a configuration via the "config" attribute');if(!this.config.columns)throw new Error("[xosTable] Please provide a columns list in the configuration");this.config.order&&angular.isObject(this.config.order)&&(this.reverse=this.config.order.reverse||!1,this.orderBy=this.config.order.field||"id");var o=e.filter(this.config.columns,{type:"custom"});angular.isArray(o)&&o.length>0&&e.forEach(o,function(e){if(!e.formatter||!angular.isFunction(e.formatter))throw new Error("[xosTable] You have provided a custom field type, a formatter function should provided too.")});var t=e.filter(this.config.columns,{type:"icon"});angular.isArray(t)&&t.length>0&&e.forEach(t,function(e){if(!e.formatter||!angular.isFunction(e.formatter))throw new Error("[xosTable] You have provided an icon field type, a formatter function should provided too.")});var i=e.filter(this.config.columns,function(e){return angular.isDefined(e.link)});angular.isArray(i)&&i.length>0&&e.forEach(i,function(e){if(!angular.isFunction(e.link))throw new Error("[xosTable] The link property should be a function.")}),this.columns=this.config.columns,this.classes=this.config.classes||"table table-striped table-bordered",this.config.actions,this.config.pagination&&(this.currentPage=0,this.goToPage=function(e){n.currentPage=e})}]}}).filter("arrayToList",function(){return function(e){return angular.isArray(e)?e.join(", "):e}}).directive("linkWrapper",function(){return{restrict:"A",transclude:!0,template:'\n          <a ng-if="col.link" href="{{col.link(item)}}">\n            <div ng-transclude></div>\n          </a>\n          <div ng-transclude ng-if="!col.link"></div>\n        '}})}(),function(){angular.module("xos.uiComponents").directive("xosForm",function(){return{restrict:"E",scope:{config:"=",ngModel:"="},template:'\n        <ng-form name="vm.{{vm.config.formName || \'form\'}}">\n          <div class="form-group" ng-repeat="(name, field) in vm.formField">\n            <xos-field name="name" field="field" ng-model="vm.ngModel[name]"></xos-field>\n            <xos-validation field="vm[vm.config.formName || \'form\'][name]" form="vm[vm.config.formName || \'form\']"></xos-validation>\n          </div>\n          <div class="form-group" ng-if="vm.config.actions">\n            <button role="button" href=""\n              ng-repeat="action in vm.config.actions"\n              ng-click="action.cb(vm.ngModel)"\n              class="btn btn-{{action.class}}"\n              title="{{action.label}}">\n              <i class="glyphicon glyphicon-{{action.icon}}"></i>\n              {{action.label}}\n            </button>\n          </div>\n        </ng-form>\n      ',bindToController:!0,controllerAs:"vm",controller:["$scope","$log","_","XosFormHelpers",function(e,n,o,t){var i=this;if(!this.config)throw new Error('[xosForm] Please provide a configuration via the "config" attribute');if(!this.config.actions)throw new Error("[xosForm] Please provide an action list in the configuration");this.excludedField=["id","validators","created","updated","deleted","backend_status"],this.config&&this.config.exclude&&(this.excludedField=this.excludedField.concat(this.config.exclude)),this.formField=[],e.$watch(function(){return i.ngModel},function(e){if(i.formField={},e){var n=o.difference(Object.keys(e),i.excludedField),r=t.parseModelField(n);i.formField=t.buildFormStructure(r,i.config.fields,e)}})}]}})}(),function(){angular.module("xos.uiComponents").directive("xosField",["RecursionHelper",function(e){return{restrict:"E",scope:{name:"=",field:"=",ngModel:"="},template:'\n        <label ng-if="vm.field.type !== \'object\'">{{vm.field.label}}</label>\n            <input\n              ng-if="vm.field.type !== \'boolean\' && vm.field.type !== \'object\' && vm.field.type !== \'select\'"\n              type="{{vm.field.type}}"\n              name="{{vm.name}}"\n              class="form-control"\n              ng-model="vm.ngModel"\n              ng-minlength="vm.field.validators.minlength || 0"\n              ng-maxlength="vm.field.validators.maxlength || 2000"\n              ng-required="vm.field.validators.required || false" />\n              <select class="form-control" ng-if ="vm.field.type === \'select\'"\n                name = "{{vm.name}}"\n                ng-options="item.id as item.label for item in vm.field.options track by item.id"\n                ng-model="vm.ngModel"\n                ng-required="vm.field.validators.required || false">\n                </select>\n            <span class="boolean-field" ng-if="vm.field.type === \'boolean\'">\n              <button\n                class="btn btn-success"\n                ng-show="vm.ngModel"\n                ng-click="vm.ngModel = false">\n                <i class="glyphicon glyphicon-ok"></i>\n              </button>\n              <button\n                class="btn btn-danger"\n                ng-show="!vm.ngModel"\n                ng-click="vm.ngModel = true">\n                <i class="glyphicon glyphicon-remove"></i>\n              </button>\n            </span>\n            <div\n              class="panel panel-default object-field"\n              ng-if="vm.field.type == \'object\' && (!vm.isEmptyObject(vm.ngModel) || !vm.isEmptyObject(vm.field.properties))"\n              >\n              <div class="panel-heading">{{vm.field.label}}</div>\n              <div class="panel-body">\n                <div ng-if="!vm.field.properties" ng-repeat="(k, v) in vm.ngModel">\n                  <xos-field\n                    name="k"\n                    field="{label: vm.formatLabel(k), type: vm.getType(v)}"\n                    ng-model="v">\n                  </xos-field>\n                </div>\n                <div ng-if="vm.field.properties" ng-repeat="(k, v) in vm.field.properties">\n                  <xos-field\n                    name="k"\n                    field="{\n                      label: v.label || vm.formatLabel(k),\n                      type: v.type,\n                      validators: v.validators\n                    }"\n                    ng-model="vm.ngModel[k]">\n                  </xos-field>\n                </div>\n              </div>\n            </div>\n      ',bindToController:!0,controllerAs:"vm",compile:function(n){return e.compile(n)},controller:["$attrs","XosFormHelpers","LabelFormatter",function(e,n,o){if(!this.name)throw new Error("[xosField] Please provide a field name");if(!this.field)throw new Error("[xosField] Please provide a field definition");if(!this.field.type)throw new Error("[xosField] Please provide a type in the field definition");if(!e.ngModel)throw new Error("[xosField] Please provide an ng-model");this.getType=n._getFieldFormat,this.formatLabel=o.format,this.isEmptyObject=function(e){return e?0===Object.keys(e).length:!0}}]}}])}(),function(){angular.module("xos.uiComponents").directive("xosAlert",function(){return{restrict:"E",scope:{config:"=",show:"=?"},template:'\n        <div ng-cloak class="alert alert-{{vm.config.type}}" ng-hide="!vm.show">\n          <button type="button" class="close" ng-if="vm.config.closeBtn" ng-click="vm.dismiss()">\n            <span aria-hidden="true">&times;</span>\n          </button>\n          <p ng-transclude></p>\n        </div>\n      ',transclude:!0,bindToController:!0,controllerAs:"vm",controller:["$timeout",function(e){var n=this;if(!this.config)throw new Error('[xosAlert] Please provide a configuration via the "config" attribute');this.show=this.show!==!1,this.dismiss=function(){n.show=!1},this.config.autoHide&&!function(){var o=e(function(){n.dismiss(),e.cancel(o)},n.config.autoHide)}()}]}})}(),function(){function e(){var e=function(e){return e.split("_").join(" ").trim()},n=function(e){return e.split(/(?=[A-Z])/).map(function(e){return e.toLowerCase()}).join(" ")},o=function(e){return e.slice(0,1).toUpperCase()+e.slice(1)},t=function(t){return t=e(t),t=n(t),t=o(t).replace(/\s\s+/g," ")+":",t.replace("::",":")};return{_formatByUnderscore:e,_formatByUppercase:n,_capitalize:o,format:t}}angular.module("xos.uiComponents").factory("LabelFormatter",e)}();var _typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol?"symbol":typeof e};!function(){angular.module("xos.uiComponents").service("XosFormHelpers",["_","LabelFormatter",function(e,n){var o=this;this._isEmail=function(e){var n=/(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/;return n.test(e)},this._getFieldFormat=function(n){return angular.isArray(n)?"array":e.isDate(n)||!Number.isNaN(Date.parse(n))&&new Date(n).getTime()>6311808e5?"date":"boolean"==typeof n?"boolean":o._isEmail(n)?"email":"string"==typeof n||null===n?"text":"undefined"==typeof n?"undefined":_typeof(n)},this.buildFormStructure=function(t,i,r){return t=angular.extend(t,i),i=i||{},e.reduce(Object.keys(t),function(e,t){return e[t]={label:i[t]&&i[t].label?i[t].label+":":n.format(t),type:i[t]&&i[t].type?i[t].type:o._getFieldFormat(r[t]),validators:i[t]&&i[t].validators?i[t].validators:{},hint:i[t]&&i[t].hint?i[t].hint:""},i[t]&&i[t].options&&(e[t].options=i[t].options),i[t]&&i[t].properties&&(e[t].properties=i[t].properties),"date"===e[t].type&&(r[t]=new Date(r[t])),"number"===e[t].type&&(r[t]=parseInt(r[t],10)),e},{})},this.parseModelField=function(n){return e.reduce(n,function(e,n){return e[n]={},e},{})}}])}(),function(){function e(e,n,o){e.interceptors.push("SetCSRFToken"),n.startSymbol("{$"),n.endSymbol("$}"),o.defaults.stripTrailingSlashes=!1}e.$inject=["$httpProvider","$interpolateProvider","$resourceProvider"],angular.module("bugSnag",[]).factory("$exceptionHandler",function(){return function(e,n){window.Bugsnag?Bugsnag.notifyException(e,{diagnostics:{cause:n}}):console.error(e,n,e.stack)}}),angular.module("xos.helpers",["ngCookies","ngResource","ngAnimate","bugSnag","xos.uiComponents"]).config(e).factory("_",["$window",function(e){return e._}])}(),function(){angular.module("xos.helpers").service("vSG-Collection",["$resource",function(e){return e("/api/service/vsg/")}])}(),function(){angular.module("xos.helpers").service("vOLT-Collection",["$resource",function(e){return e("/api/tenant/cord/volt/:volt_id/",{volt_id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("Login",["$resource",function(e){return e("/api/utility/login/")}]).service("Logout",["$resource",function(e){return e("/api/utility/logout/")}])}(),function(){angular.module("xos.helpers").service("Users",["$resource",function(e){return e("/api/core/users/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("Truckroll",["$resource",function(e){return e("/api/tenant/truckroll/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("Tenants",["$resource",function(e){return e("/api/core/tenants/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("Subscribers",["$resource",function(e){return e("/api/tenant/cord/subscriber/:id/",{id:"@id"},{update:{method:"PUT"},"View-a-Subscriber-Features-Detail":{method:"GET",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/"},"Read-Subscriber-uplink_speed":{method:"GET",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/uplink_speed/"},"Update-Subscriber-uplink_speed":{method:"PUT",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/uplink_speed/"},"Read-Subscriber-downlink_speed":{method:"GET",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/downlink_speed/"},"Update-Subscriber-downlink_speed":{method:"PUT",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/downlink_speed/"},"Read-Subscriber-cdn":{method:"GET",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/cdn/"},"Update-Subscriber-cdn":{method:"PUT",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/cdn/"},"Read-Subscriber-uverse":{method:"GET",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/uverse/"},"Update-Subscriber-uverse":{method:"PUT",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/uverse/"},"Read-Subscriber-status":{method:"GET",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/status/"},"Update-Subscriber-status":{method:"PUT",isArray:!1,url:"/api/tenant/cord/subscriber/:id/features/status/"}})}])}(),function(){angular.module("xos.helpers").service("SlicesPlus",["$http","$q",function(e,n){this.query=function(o){var t=n.defer();return e.get("/api/utility/slicesplus/",{params:o}).then(function(e){t.resolve(e.data)})["catch"](function(e){t.reject(e.data)}),{$promise:t.promise}},this.get=function(o,t){var i=n.defer();return e.get("/api/utility/slicesplus/"+o,{params:t}).then(function(e){i.resolve(e.data)})["catch"](function(e){i.reject(e.data)}),{$promise:i.promise}}}])}(),function(){angular.module("xos.helpers").service("Slices",["$resource",function(e){return e("/api/core/slices/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("Sites",["$resource",function(e){return e("/api/core/sites/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("Services",["$resource",function(e){return e("/api/core/services/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("ONOS-Services-Collection",["$resource",function(e){return e("/api/service/onos/")}])}(),function(){angular.module("xos.helpers").service("ONOS-App-Collection",["$resource",function(e){return e("/api/tenant/onos/app/")}])}(),function(){angular.module("xos.helpers").service("Nodes",["$resource",function(e){return e("/api/core/nodes/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("Networks",["$resource",function(e){return e("/api/core/networks/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("Instances",["$resource",function(e){return e("/api/core/instances/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("Flavors",["$resource",function(e){return e("/api/core/flavors/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("Example-Services-Collection",["$resource",function(e){return e("/api/service/exampleservice/")}])}(),function(){angular.module("xos.helpers").service("Deployments",["$resource",function(e){return e("/api/core/deployments/:id/",{id:"@id"},{update:{method:"PUT"}})}])}(),function(){angular.module("xos.helpers").service("XosUserPrefs",["$cookies",function(e){var n=this,o=e.get("xosUserPrefs")?JSON.parse(e.get("xosUserPrefs")):{};this.getAll=function(){return o=e.get("xosUserPrefs")?JSON.parse(e.get("xosUserPrefs")):{}},this.setAll=function(n){e.put("xosUserPrefs",JSON.stringify(n))},this.getSynchronizerNotificationStatus=function(){var e=arguments.length<=0||void 0===arguments[0]?!1:arguments[0];return e?n.getAll().synchronizers.notification[e]:n.getAll().synchronizers.notification},this.setSynchronizerNotificationStatus=function(){var e=arguments.length<=0||void 0===arguments[0]?!1:arguments[0],o=arguments[1];if(!e)throw new Error("[XosUserPrefs] When updating a synchronizer is mandatory to provide a name.");var t=n.getAll();t.synchronizers||(t.synchronizers={notification:{}}),t.synchronizers.notification[e]=o,n.setAll(t)}}])}(),function(){angular.module("xos.helpers").service("GraphService",["$q","Tenants","Services",function(e,n,o){var t=this;this.loadCoarseData=function(){var t=void 0,i=e.defer();return o.query().$promise.then(function(e){return t=e,n.query({kind:"coarse"}).$promise}).then(function(e){i.resolve({tenants:e,services:t})}),i.promise},this.getCoarseGraph=function(){return t.loadCoarseData().then(function(e){console.log(e)}),"ciao"}}])}(),function(){angular.module("xos.helpers").factory("Notification",function(){return window.Notification}).service("xosNotification",["$q","$log","Notification",function(e,n,o){var t=this;this.checkPermission=function(){var n=e.defer();return o.requestPermission().then(function(e){"granted"===e?n.resolve(e):n.reject(e)}),n.promise},this.sendNotification=function(e,t){var i=new o(e,t);i.onerror=function(e){n.error(e)}},this.notify=function(e,i){"Notification"in window?"granted"!==o.permission?t.checkPermission().then(function(){return t.sendNotification(e,i)}):"granted"===o.permission&&t.sendNotification(e,i):n.info("This browser does not support desktop notification")}}])}(),function(){function e(){return{request:function(e){return-1===e.url.indexOf(".html")&&(e.url+="?no_hyperlinks=1"),e}}}angular.module("xos.helpers").factory("NoHyperlinks",e)}(),angular.module("xos.helpers").config(["$provide",function(e){e.decorator("$log",["$delegate",function(e){var n=function(){return window.location.href.indexOf("debug=true")>=0},o=e.log,t=e.info,i=e.warn,r=e.error,s=e.debug,a=function(o){return function(){if(n()){var t=[].slice.call(arguments),i=new Date;t[0]="["+i.getHours()+":"+i.getMinutes()+":"+i.getSeconds()+"] "+t[0],"function"!=typeof e.reset||e.debug.logs instanceof Array||e.reset(),o.apply(null,t)}}};return e.info=a(t),e.log=a(o),e.warn=a(i),e.error=a(r),e.debug=a(s),e}])}]),function(){function e(){var e=function(e){return e.split("_").join(" ").trim()},n=function(e){return e.split(/(?=[A-Z])/).map(function(e){return e.toLowerCase()}).join(" ")},o=function(e){return e.slice(0,1).toUpperCase()+e.slice(1)},t=function(t){return t=e(t),t=n(t),t=o(t).replace(/\s\s+/g," ")+":",t.replace("::",":")};return{_formatByUnderscore:e,_formatByUppercase:n,_capitalize:o,format:t}}angular.module("xos.uiComponents").factory("LabelFormatter",e)}(),function(){function e(e){return{request:function(n){return"GET"!==n.method&&(n.headers["X-CSRFToken"]=e.get("xoscsrftoken")),n}}}e.$inject=["$cookies"],angular.module("xos.helpers").factory("SetCSRFToken",e)}();