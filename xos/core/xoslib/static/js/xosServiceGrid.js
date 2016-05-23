"use strict";angular.module("xos.serviceGrid",["ngResource","ngCookies","ui.router","xos.helpers"]).config(["$stateProvider",function(e){e.state("serviceGrid",{url:"/",template:"<service-grid></service-grid>"}).state("serviceGraph",{url:"/graph",template:"<service-graph></service-graph>"})}]).config(["$httpProvider",function(e){e.interceptors.push("NoHyperlinks")}]).directive("serviceGrid",function(){return{restrict:"E",scope:{},bindToController:!0,controllerAs:"vm",templateUrl:"templates/service-grid.tpl.html",controller:["Services","ToscaEncoder","_",function(e,t,n){var r=this;this.tableConfig={columns:[{label:"Status",prop:"status",type:"icon",formatter:function(e){var t=parseInt(e.backend_status.match(/^[0-9]/)[0]);switch(t){case 0:return"time";case 1:return"ok";case 2:return"remove"}}},{label:"Name",prop:"name",link:function(e){return""+e.view_url.replace(/\$[a-z]+\$/,e.id)}},{label:"Kind",prop:"kind"},{label:"Enabled",prop:"enabled",type:"boolean"}],filter:"field",order:{field:"name"},actions:[{label:"export",icon:"export",cb:function(e){r.tosca="",t.serviceToTosca(e).then(function(e){r.showFeedback=!0,r.tosca=e})}}]},e.query().$promise.then(function(e){r.services=n.map(e,function(e){return e.status=0!==parseInt(e.backend_status.match(/^[0-9]/)[0]),e})})["catch"](function(e){throw new Error(e)})}]}}),function(){angular.module("xos.serviceGrid").service("ToscaEncoder",["$q","_","ArchiveManager","ServiceEncoder","SlicesEncoder",function(e,t,n,r,o){var i=this,a={tosca_definitions_version:"tosca_simple_yaml_1_0",description:"",imports:["custom_types/xos.yaml"],topology_template:{node_templates:{}}};this.toYml=function(e){return jsyaml.dump(e).replace(/'/g,"")},this["export"]=function(e){n.download(e.name);var t=i.toYml(a);return t},this.serviceToTosca=function(t){n.createArchive(),a.topology_template.node_templates={},a.description="Just enough Tosca to get the "+t.humanReadableName+" service up and running";var s=e.defer();return r.formatServiceProperties(t,a).then(function(e){return o.getServiceSlices(t,e)}).then(function(e){return r.getServiceRequirements(t,e)}).then(function(e){n.addFile(t.name+"_service.yaml",i.toYml(e)),i["export"](t),s.resolve(i.toYml(e))})["catch"](function(e){s.reject(e)}),s.promise}}])}(),angular.module("xos.serviceGrid").run(["$templateCache",function(e){e.put("templates/service-graph.tpl.html",'<div class="row">\n  <div class="col-sm-10">\n    <h1>Graph</h1>\n  </div>\n  <div class="col-sm-2">\n    <a href="/admin/core/service/add" class="btn btn-success btn-block">\n      <i class="glyphicon glyphicon-plus"></i>\n      Add Service\n    </a>\n    <a href="#/" class="btn btn-default btn-block">\n      Service List\n    </a>\n  </div>\n</div>\n<xos-side-panel config="vm.panelConfig" show="vm.panelShow">\n  <h1>\n    {{vm.selectedNode.name}}\n    <small>\n      <i class="glyphicon glyphicon-{{vm.selectedNode.icon}}"></i>\n    </small>\n  </h1>\n  <table class="table">\n    <tr>\n      <td>Kind:</td>\n      <td>{{vm.selectedNode.kind}}</td>\n    </tr>\n    <tr>\n      <td>Enabled:</td>\n      <td>{{vm.selectedNode.enabled}}</td>\n    </tr>\n    <tr>\n      <td>Status:</td>\n      <td>{{vm.selectedNode.backend_status}}</td>\n    </tr>\n  </table>\n  <a ng-click="vm.exportToTosca(vm.selectedNode)" class="btn btn-primary">\n    Export to TOSCA\n    <i class="glyphicon glyphicon-export"></i>\n  </a>\n</xos-side-panel>'),e.put("templates/service-grid.tpl.html",'<div class="row">\n  <div class="col-md-10 table-responsive">\n    <xos-table config="vm.tableConfig" data="vm.services"></xos-table>\n  </div>\n  <div class="col-md-2">\n    <a href="/admin/core/service/add" class="btn btn-success btn-block">\n      <i class="glyphicon glyphicon-plus"></i>\n      Add Service\n    </a>\n    <a href="#/graph" class="btn btn-default btn-block">\n      Tenancy Graph\n    </a>\n  </div>\n</div>\n\n<div class="row">\n  <div class="col-xs-12">\n    <div class="alert alert-info" ng-show="vm.showFeedback">\n      Remember that you should copy any key artifact inside the container in <pre>/opt/xos/tosca</pre>!\n    </div>\n  </div>\n</div>\n\n<pre ng-show="vm.tosca">\n{{vm.tosca}}\n</pre>')}]);var _slicedToArray=function(){function e(e,t){var n=[],r=!0,o=!1,i=void 0;try{for(var a,s=e[Symbol.iterator]();!(r=(a=s.next()).done)&&(n.push(a.value),!t||n.length!==t);r=!0);}catch(c){o=!0,i=c}finally{try{!r&&s["return"]&&s["return"]()}finally{if(o)throw i}}return n}return function(t,n){if(Array.isArray(t))return t;if(Symbol.iterator in Object(t))return e(t,n);throw new TypeError("Invalid attempt to destructure non-iterable instance")}}();!function(){angular.module("xos.serviceGrid").service("SlicesEncoder",["$q","_","Slices","SiteEncoder","ImageEncoder","NetworkEncoder",function(e,t,n,r,o,i){var a=this;this.buildTosca=function(n,a,s){var c={},l=e.defer();return n=t.reduce(n,function(e,t){if(e[t.name]={type:"tosca.nodes.Slice",properties:{network:t.network},requirements:[{management:{node:"management",relationship:"tosca.relationships.ConnectsToNetwork"}}]},angular.isDefined(s)){var n={};n[s+"_service"]={node:"service#"+s,relationship:"tosca.relationships.MemberOfService"},e[t.name].requirements.push(n)}return angular.isDefined(t.description)&&(e[t.name].description=t.description),angular.isDefined(t.site)&&(c[t.name+"#site"]=r.buildTosca(t.site,a)),angular.isDefined(t.default_image)&&(c[t.name+"#image"]=o.buildTosca(t.default_image,a)),angular.isDefined(t.networks)&&t.networks.length>0&&(c[t.name+"#management"]=i.getSliceNetworks(t,a)),e},{}),Object.keys(c).length>0?!function(){var t={site:"tosca.relationships.MemberOfSite",image:"tosca.relationships.DefaultImage"};a.topology_template.node_templates.management={type:"tosca.nodes.network.Network.XOS",properties:{"no-create":!0,"no-delete":!0,"no-update":!0}},e.all(c).then(function(e){var r=!0,o=!1,i=void 0;try{for(var s,c=Object.keys(e)[Symbol.iterator]();!(r=(s=c.next()).done);r=!0){var u=s.value,d=u.split("#"),p=_slicedToArray(d,2),v=p[0],m=p[1];if(angular.isDefined(t[m])){n[v].requirements||(n[v].requirements=[]);var f=_slicedToArray(e[u],2),h=f[0],g=f[1],y={},b=void 0;b="site"===m?g.name:m+"#"+g.name,y[m]={node:b,relationship:t[m]},n[v].requirements.push(y),angular.extend(a,h)}}}catch(_){o=!0,i=_}finally{try{!r&&c["return"]&&c["return"]()}finally{if(o)throw i}}angular.extend(a.topology_template.node_templates,n),l.resolve(a)})["catch"](function(e){throw new Error(e)})}():(angular.extend(a.topology_template.node_templates,n),l.resolve(a)),l.promise},this.getServiceSlices=function(t,r){var o=e.defer();return n.query({service:t.id}).$promise.then(function(e){return a.buildTosca(e,r,t.name)}).then(function(e){o.resolve(e)}),o.promise}}])}(),function(){angular.module("xos.serviceGrid").service("SiteEncoder",["$q","Sites",function(e,t){this.buildTosca=function(n,r){var o=e.defer();return t.get({id:n}).$promise.then(function(e){var t={};t[""+e.name]={type:"tosca.nodes.Site"},angular.extend(r.topology_template.node_templates,t),o.resolve([r,e])})["catch"](o.reject),o.promise}}])}(),function(){angular.module("xos.uiComponents").directive("xosSidePanel",function(){return{restrict:"E",scope:{config:"=",show:"="},template:'\n        <div class="xos-side-panel-content {{vm.classes.join(\' \')}}">\n          <div class="row">\n            <div class="col-xs-12">\n              <button type="button" class="close" ng-click="vm.dismiss()">\n                <span aria-hidden="true">&times;</span>\n              </button>\n            </div>\n          </div>\n          <div class="row">\n            <div class="col-xs-12" ng-transclude></div>\n          </div>\n        </div>\n      ',transclude:!0,bindToController:!0,controllerAs:"vm",controller:["$scope","$timeout","_",function(e,t,n){var r=this;console.log(this.show),this.classes=[],this.classes.push(this.config.position),this.dismiss=function(){r.show=!1,r.classes=r.toggleClass(r.classes),t(function(){return n.remove(r.classes,function(e){return"out"===e})},500)},this.toggleClass=function(e){return e.indexOf("in")>-1?(n.remove(r.classes,function(e){return"in"===e}),r.classes.push("out"),e):(n.remove(r.classes,function(e){return"out"===e}),r.classes.push("in"),e)},e.$watch(function(){return r.show},function(e){angular.isDefined(e)&&e&&e===!0&&(r.classes=r.toggleClass(r.classes))})}]}})}(),function(){angular.module("xos.serviceGrid").service("ServiceEncoder",["$q","ArchiveManager","Tenants","Services",function(e,t,n,r){var o={fabric:"tosca.nodes.FabricService",onos:"tosca.nodes.ONOSService",vCPE:"tosca.nodes.VSGService",vOLT:"tosca.nodes.VOLTService",vROUTER:"tosca.nodes.VRouterService",VTN:"tosca.nodes.VTNService",vTR:"tosca.nodes.Service"};this.formatServiceProperties=function(n,r){var i=e.defer(),a="service#"+n.name;r.topology_template.node_templates[a]={},r.topology_template.node_templates[a].type=o[n.kind]||"tosca.nodes.Service";var s={properties:{kind:n.kind}};return angular.isDefined(n.view_url)&&(s.properties.view_url=n.view_url),angular.isDefined(n.icon_url)&&(s.properties.icon_url=n.icon_url),angular.isDefined(n.private_key_fn)&&(s.properties.private_key_fn=n.private_key_fn),angular.isDefined(n.public_key)&&(t.addFile(n.name+"_rsa.pub",n.public_key),s.properties.public_key="{ get_artifact: [ SELF, pubkey, LOCAL_FILE] }",s.artifacts={pubkey:"/opt/xos/tosca/"+n.name+"/"+n.name+"_rsa.pub"},r.topology_template.node_templates[a].artifacts=s.artifacts),r.topology_template.node_templates[a].properties=s.properties,i.resolve(r),i.promise},this.getServiceRequirements=function(t,o){var i=e.defer();return n.query({subscriber_service:t.id}).$promise.then(function(t){var n=[];return t=_.uniqBy(t,"provider_service"),_.forEach(t,function(e){n.push(r.get({id:e.provider_service}).$promise)}),e.all(n)}).then(function(e){var n=_.reduce(e,function(e,t){return e.concat(t.name)},[]);if(n=_.reduce(n,function(e,t){var n=t+"_tenant",r={};return r[n]={node:"service#"+t,relationship:"tosca.relationships.TenantOfService"},e.concat(r)},[]),n.length>0){_.forEach(n,function(e){var t=e[Object.keys(e)[0]].node;o.topology_template.node_templates[t]={type:"tosca.nodes.Service",properties:{"no-create":!0,"no-delete":!0,"no-update":!0}}});var r="service#"+t.name;o.topology_template.node_templates[r].requirements=n}i.resolve(o)}),i.promise}}])}();var _slicedToArray=function(){function e(e,t){var n=[],r=!0,o=!1,i=void 0;try{for(var a,s=e[Symbol.iterator]();!(r=(a=s.next()).done)&&(n.push(a.value),!t||n.length!==t);r=!0);}catch(c){o=!0,i=c}finally{try{!r&&s["return"]&&s["return"]()}finally{if(o)throw i}}return n}return function(t,n){if(Array.isArray(t))return t;if(Symbol.iterator in Object(t))return e(t,n);throw new TypeError("Invalid attempt to destructure non-iterable instance")}}();!function(){angular.module("xos.serviceGrid").service("Graph",["$q","Tenants","Services","Subscribers",function(e,t,n,r){var o=new graphlib.Graph,i=!1,a=function(){var i=e.defer();return e.all([t.query().$promise,n.query().$promise,r.query().$promise]).then(function(e){var t=_slicedToArray(e,3),n=t[0],r=t[1];t[2];r.forEach(function(e){return o.setNode(e.id,angular.extend(e,{type:"service"}))}),n.filter(function(e){return e.subscriber_service&&e.provider_service}).forEach(function(e){return o.setEdge(e.subscriber_service,e.provider_service,e,e.name)}),i.resolve(o)}),i.promise};this.getGraph=function(){var t=e.defer();return i?t.resolve(o):a().then(function(e){i=!0,t.resolve(e)})["catch"](console.log),{$promise:t.promise}}}]).directive("serviceGraph",function(){return{restrict:"E",scope:{},bindToController:!0,controllerAs:"vm",templateUrl:"templates/service-graph.tpl.html",controller:["$scope","$element","GraphService","Graph","ToscaEncoder",function(e,t,n,r,o){var i=void 0,a=t[0],s=void 0,c=void 0,l=this;this.panelConfig={position:"right"};var u=function(e){s.attr("cx",function(e){return e.x}).attr("cy",function(e){return e.y}).attr({transform:function(e){return"translate("+e.x+", "+e.y+")"}}),c.attr("x1",function(e){return e.source.x}).attr("y1",function(e){return e.source.y}).attr("x2",function(e){return v(e)[0]}).attr("y2",function(e){return v(e)[1]})};r.getGraph().$promise.then(function(t){var n=t.edges().map(function(e){return{source:t.node(e.v),target:t.node(e.w)}}),r=t.nodes().map(function(e){return t.node(e)});r.push({name:"XOS",type:"xos",x:a.clientWidth/2,y:a.clientHeight/2,fixed:!0}),d(a),p();var o=d3.layout.force().nodes(r).links(n).charge(-1060).gravity(.1).linkDistance(200).size([a.clientWidth,a.clientHeight]).on("tick",u).start();c=i.selectAll(".link").data(n).enter().insert("line").attr("class","link").attr("marker-end","url(#arrow)"),s=i.selectAll(".node").data(r).enter().append("g").call(o.drag).on("mousedown",function(t){e.$apply(function(){if("XOS"!==t.name){l.panelShow=!0;var e=parseInt(t.backend_status.match(/^[0-9]/)[0]);switch(console.log(e),e){case 0:t.icon="time";break;case 1:t.icon="ok";break;case 2:t.icon="remove"}l.selectedNode=t}}),d3.event.stopPropagation()}),s.append("circle").attr({"class":function(e){return"node "+(e.type||"")},r:10}),s.append("text").attr({"text-anchor":"middle","alignment-baseline":"middle"}).text(function(e){return e.humanReadableName||e.name}),s.select("circle").attr({r:function(e){var t=d3.select(this).node().parentNode,n=d3.select(t).select("text").node().getBBox(),r=n.width/2+10;return e.nodeWidth=2*r,r}})});var d=function(e){d3.select(e).select("svg").remove(),i=d3.select(e).append("svg").style("width",e.clientWidth+"px").style("height",e.clientHeight+"px")},p=function(){i.append("svg:defs").selectAll("marker").data(["arrow"]).enter().append("svg:marker").attr("id",String).attr("viewBox","0 -5 10 10").attr("refX",10).attr("refY",0).attr("markerWidth",6).attr("markerHeight",6).attr("orient","auto").append("svg:path").attr("d","M0,-5L10,0L0,5")},v=function(e){var t=e.target.nodeWidth/2,n=e.target.x-e.source.x,r=e.target.y-e.source.y,o=Math.atan2(r,n),i=e.target.x-Math.cos(o)*t,a=e.target.y-Math.sin(o)*t;return[i,a]};this.exportToTosca=function(e){o.serviceToTosca(e)}}]}})}();var _slicedToArray=function(){function e(e,t){var n=[],r=!0,o=!1,i=void 0;try{for(var a,s=e[Symbol.iterator]();!(r=(a=s.next()).done)&&(n.push(a.value),!t||n.length!==t);r=!0);}catch(c){o=!0,i=c}finally{try{!r&&s["return"]&&s["return"]()}finally{if(o)throw i}}return n}return function(t,n){if(Array.isArray(t))return t;if(Symbol.iterator in Object(t))return e(t,n);throw new TypeError("Invalid attempt to destructure non-iterable instance")}}();!function(){angular.module("xos.serviceGrid").service("NetworkEncoder",["$q","Networks","NetworkTemplateEncoder",function(e,t,n){var r=this;this.buildTosca=function(t,r){var o=angular.copy(t),i={},a=e.defer();try{t=_.reduce(t,function(e,t){return e["network#"+t.name]={type:"tosca.nodes.network.Network.XOS",requirements:[]},angular.isDefined(t.slices)&&(_.forEach(t.slices,function(n){var r={owner:{node:n.name,relationship:"tosca.relationships.MemberOfSlice"}},o={connection:{node:n.name,relationship:"tosca.relationships.ConnectsToSlice"}};e["network#"+t.name].requirements.push(r,o)}),angular.isDefined(t.template)&&(i[t.name]=n.buildTosca(t.template,r))),e},{}),Object.keys(i).length>0?e.all(i).then(function(e){if(e){var n=!0,i=!1,s=void 0;try{for(var c,l=Object.keys(e)[Symbol.iterator]();!(n=(c=l.next()).done);n=!0){var u=c.value,d=_slicedToArray(e[u],2),p=d[0],v=d[1];t["network#"+u].requirements.push({network_template:{node:"network_template#"+v.name,relationship:"tosca.relationships.UsesNetworkTemplate"}}),angular.extend(r,p)}}catch(m){i=!0,s=m}finally{try{!n&&l["return"]&&l["return"]()}finally{if(i)throw s}}}angular.extend(r.topology_template.node_templates,t),a.resolve([r,o])})["catch"](function(e){throw new Error(e)}):(angular.extend(r.topology_template.node_templates,t),a.resolve([r,o]))}catch(s){a.reject(s)}return a.promise},this.getSliceNetworks=function(n,o){var i=e.defer();return t.query({owner:n.id}).$promise.then(function(e){e=_.filter(e,function(e){return-1!==n.networks.indexOf(e.id)}),e=e.map(function(e){var t=e.slices.indexOf(n.id);return e.slices[t]=n,e}),r.buildTosca(e,o).then(i.resolve)["catch"](i.reject)}),i.promise}}])}(),function(){angular.module("xos.serviceGrid").service("NetworkTemplateEncoder",["$q","Networkstemplates",function(e,t){this.buildTosca=function(n,r){var o=e.defer();return t.get({id:n}).$promise.then(function(e){var t={};t["network_template#"+e.name]={type:"tosca.nodes.NetworkTemplate"},angular.extend(r.topology_template.node_templates,t),o.resolve([r,e])})["catch"](function(e){o.reject(e)}),o.promise}}])}(),function(){angular.module("xos.serviceGrid").service("ImageEncoder",["$q","Images",function(e,t){this.buildTosca=function(n,r){var o=e.defer();return t.get({id:n}).$promise.then(function(e){var t={};t["image#"+e.name]={type:"tosca.nodes.Image"},angular.extend(r.topology_template.node_templates,t),o.resolve([r,e])})["catch"](o.reject),o.promise}}])}(),function(){angular.module("xos.serviceGrid").service("ArchiveManager",function(){var e=this;this.createArchive=function(){e.archive=new JSZip},this.addFile=function(t,n){e.archive.file(t,n)},this.download=function(t){console.log(e.archive),e.archive.generateAsync({type:"blob"}).then(function(e){saveAs(e,t+".zip")})["catch"](function(e){console.log(e)})}})}(),angular.module("xos.serviceGrid").run(["$location",function(e){e.path("/")}]);