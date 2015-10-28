angular.module("xos.contentProviderApp").run(["$templateCache", function($templateCache) {$templateCache.put("../../static/templates/contentProvider/cp_actions.html","<a href=\"#/\" class=\"btn btn-default\">\n  <i class=\"icon icon-arrow-left\"></i>Back\n</a>\n<a href=\"#/contentProvider/\" class=\"btn btn-success\">\n  <i class=\"icon icon-plus\"></i>Create\n</a>\n<a ng-click=\"vm.deleteCp(vm.id)\" class=\"btn btn-danger\">\n  <i class=\"icon icon-remove\"></i>Remove\n</a>");
$templateCache.put("../../static/templates/contentProvider/cp_cdn_prefix.html","<div class=\"row-fluid\">\n  <div class=\"span6\">\n    <h1>{$ vm.cp.humanReadableName $}</h1>\n  </div>\n  <div class=\"span6 text-right\">\n    <cp-actions id=\"vm.cp.id\"></cp-actions>\n  </div>\n</div>\n<hr>\n<div class=\"row-fluid\">\n  <div class=\"span2\">\n    <div ng-include=\"\'../../static/templates/contentProvider/cp_side_nav.html\'\"></div>\n  </div>\n  <div class=\"span10\">\n    <div ng-repeat=\"item in vm.cp_prf\" class=\"well\">\n      <div class=\"row-fluid\">\n        <div class=\"span4\">\n          {{item.humanReadableName}}\n        </div>\n        <div class=\"span6\">\n          <!-- TODO show the name instead that id -->\n          {{item.defaultOriginServer}}\n        </div>\n        <div class=\"span2\">\n          <a ng-click=\"vm.removePrefix(item)\" class=\"btn btn-danger pull-right\">\n            <i class=\"icon icon-remove\"></i>\n          </a>\n        </div>\n      </div>\n    </div>\n    <hr>\n    <form ng-submit=\"vm.addPrefix(vm.new_prf)\">\n      <div class=\"row-fluid\">\n        <div class=\"span4\">\n          <label>Prefix</label>\n          <input type=\"text\" ng-model=\"vm.new_prf.prefix\" required style=\"max-width: 90%\">\n        </div>\n        <div class=\"span6\">\n          <label>Default Origin Server</label>\n          <select ng-model=\"vm.new_prf.defaultOriginServer\" style=\"max-width: 100%\">\n            <option ng-repeat=\"prf in vm.prf\" ng-value=\"prf.id\">{$ prf.humanReadableName $}</option>\n          </select>\n        </div>\n        <div class=\"span2 text-right\">\n          <button class=\"btn btn-success margin-wells\">\n            <i class=\"icon icon-plus\"></i>\n          </button>\n        </div>\n      </div>\n    </form>\n    <div class=\"alert\" ng-show=\"vm.result\" ng-class=\"{\'alert-success\': vm.result.status === 1,\'alert-error\': vm.result.status === 0}\">\n      {$ vm.result.msg $}\n    </div>\n  </div>\n</div>");
$templateCache.put("../../static/templates/contentProvider/cp_detail.html","<div class=\"row-fluid\">\n  <div class=\"span6\">\n    <h1>{$ vm.cp.humanReadableName $}</h1>\n  </div>\n  <div class=\"span6 text-right\">\n    <cp-actions id=\"vm.cp.id\"></cp-actions>\n  </div>\n</div>\n<hr>\n<div class=\"row-fluid\">\n  <div ng-show=\"vm.cp.id\" class=\"span2\">\n    <div ng-include=\"\'../../static/templates/contentProvider/cp_side_nav.html\'\"></div>\n  </div>\n  <div ng-class=\"{span10: vm.cp.id, span12: !vm.cp.id}\">\n  <!-- TODO hide form on not found -->\n    <form ng-submit=\"vm.saveContentProvider(vm.cp)\">\n      <fieldset>\n        <div class=\"row-fluid\">\n          <div class=\"span6\">\n            <label>Name:</label>\n            <input type=\"text\" ng-model=\"vm.cp.humanReadableName\" required/>\n          </div>\n          <div class=\"span6\">\n            <label class=\"checkbox\">\n              <input type=\"checkbox\" ng-model=\"vm.cp.enabled\" /> Enabled\n            </label>\n          </div>\n        </div>\n        <div class=\"row-fluid\">\n          <div class=\"span12\">\n            <label>Description</label>\n            <textarea style=\"width: 100%\" ng-model=\"vm.cp.description\"></textarea>\n          </div>\n        </div>\n        <div class=\"row-fluid\">\n          <div class=\"span12\">\n            <label>Service provider</label>\n            <select required ng-model=\"vm.cp.serviceProvider\" ng-options=\"sp.id as sp.humanReadableName for sp in vm.sp\"></select>\n          </div>\n        </div>\n        <div class=\"row-fluid\">\n          <div class=\"span12\">\n            <button class=\"btn btn-success\">\n              <span ng-show=\"vm.cp.id\">Save</span>\n              <span ng-show=\"!vm.cp.id\">Create</span>\n            </button>\n          </div>\n        </div>\n      </fieldset>\n    </form>\n    <div class=\"alert\" ng-show=\"vm.result\" ng-class=\"{\'alert-success\': vm.result.status === 1,\'alert-error\': vm.result.status === 0}\">\n      {$ vm.result.msg $}\n    </div>\n  </div>\n</div>");
$templateCache.put("../../static/templates/contentProvider/cp_list.html","<table class=\"table table-striped\" ng-show=\"vm.contentProviderList.length > 0\">\n  <thead>\n    <tr>\n      <th>\n        Name\n      </th>\n      <th>Description</th>\n      <th>Status</th>\n      <th></th>\n    </tr>\n  </thead>\n  <tr ng-repeat=\"item in vm.contentProviderList\">\n    <td>\n      <a href=\"#/contentProvider/{$ item.id $}\">{$ item.humanReadableName $}</a>\n    </td>\n    <td>\n      {$ item.description $}\n    </td>\n    <td>\n      {$ item.enabled $}\n    </td>\n    <td class=\"text-right\">\n      <a ng-click=\"vm.deleteCp(item.id)\" class=\"btn btn-danger\"><i class=\"icon icon-remove\"></i></a></td>\n  </tr>\n</table>\n<div class=\"alert alert-error\" ng-show=\"vm.contentProviderList.length == 0\">\n  No Content Provider defined\n</div>\n\n<div class=\"row\">\n  <div class=\"span12 text-right\">\n    <a class=\"btn btn-success\"href=\"#/contentProvider/\">Create</a>\n  </div>\n</div>");
$templateCache.put("../../static/templates/contentProvider/cp_origin_server.html","<div class=\"row-fluid\">\n  <div class=\"span6\">\n    <h1>{$ vm.cp.humanReadableName $}</h1>\n  </div>\n  <div class=\"span6 text-right\">\n    <cp-actions id=\"vm.cp.id\"></cp-actions>\n  </div>\n</div>\n<hr>\n<div class=\"row-fluid\">\n  <div class=\"span2\">\n    <div ng-include=\"\'../../static/templates/contentProvider/cp_side_nav.html\'\"></div>\n  </div>\n  <div class=\"span10\">\n    <div ng-repeat=\"item in vm.cp_os\" class=\"well\">\n      <div class=\"row-fluid\">\n        <div class=\"span4\">\n          {{item.humanReadableName}}\n        </div>\n        <div class=\"span6\">\n          <!-- TODO shoe the name instead that url -->\n          {{item.defaultOriginServer}}\n        </div>\n        <div class=\"span2\">\n          <a ng-click=\"vm.removeOrigin(item)\" class=\"btn btn-danger pull-right\">\n            <i class=\"icon icon-remove\"></i>\n          </a>\n        </div>\n      </div>\n    </div>\n    <hr>\n    <form ng-submit=\"vm.addOrigin(vm.new_os)\">\n      <div class=\"row-fluid\">\n        <div class=\"span4\">\n          <label>Protocol</label>\n          <select ng-model=\"vm.new_os.protocol\" ng-options=\"k as v for (k,v) in vm.protocols\" style=\"max-width: 100%;\"></select>\n        </div>\n        <div class=\"span6\">\n          <label>Url</label>\n          <input type=\"text\" ng-model=\"vm.new_os.url\" required>\n        </div>\n        <div class=\"span2 text-right\">\n          <button class=\"btn btn-success margin-wells\">\n            <i class=\"icon icon-plus\"></i>\n          </button>\n        </div>\n      </div>\n    </form>\n    <div class=\"alert\" ng-show=\"vm.result\" ng-class=\"{\'alert-success\': vm.result.status === 1,\'alert-error\': vm.result.status === 0}\">\n      {$ vm.result.msg $}\n    </div>\n  </div>\n</div>");
$templateCache.put("../../static/templates/contentProvider/cp_side_nav.html","<ul class=\"nav nav-list\">\n  <li>\n    <a class=\"btn\" ng-class=\"{\'btn-primary\': vm.pageName == \'detail\'}\" href=\"#/contentProvider/{$ vm.cp.id $}\">Details</a>\n  </li>\n  <li>\n    <a class=\"btn\" ng-class=\"{\'btn-primary\': vm.pageName == \'cdn\'}\" href=\"#/contentProvider/{$ vm.cp.id $}/cdn_prefix\">Cdn Prexix</a>\n  </li>\n  <li>\n    <a class=\"btn\" ng-class=\"{\'btn-primary\': vm.pageName == \'server\'}\" href=\"#/contentProvider/{$ vm.cp.id $}/origin_server\">Origin Server</a>\n  </li>\n  <li>\n    <a class=\"btn\" ng-class=\"{\'btn-primary\': vm.pageName == \'user\'}\" href=\"#/contentProvider/{$ vm.cp.id $}/users\">Users</a>\n  </li>\n</ul>");
$templateCache.put("../../static/templates/contentProvider/cp_user.html","<div class=\"row-fluid\">\n  <div class=\"span6\">\n    <h1>{$ vm.cp.humanReadableName $}</h1>\n  </div>\n  <div class=\"span6 text-right\">\n    <cp-actions id=\"vm.cp.id\"></cp-actions>\n  </div>\n</div>\n<hr>\n<div class=\"row-fluid\">\n  <div class=\"span2\">\n    <div ng-include=\"\'../../static/templates/contentProvider/cp_side_nav.html\'\"></div>\n  </div>\n  <div class=\"span10\">\n    <div ng-repeat=\"item in vm.cp.users\" class=\"well\">\n      <div class=\"row-fluid\">\n        <div class=\"span3\">\n          {{item.firstname}}\n        </div>\n        <div class=\"span3\">\n          {{item.lastname}}\n        </div>\n        <div class=\"span4\">\n          {{item.email}}\n        </div>\n        <div class=\"span2\">\n          <a ng-click=\"vm.removeUserFromCp(item)\" class=\"btn btn-danger pull-right\">\n            <i class=\"icon icon-remove\"></i>\n          </a>\n        </div>\n      </div>\n    </div>\n    <hr>\n    <form ng-submit=\"vm.saveContentProvider(vm.cp)\">\n      <div class=\"row-fluid\">\n        <div class=\"span8\">\n          <label>Select user:</label>\n          <select ng-model=\"vm.user\" ng-options=\"u as u.username for u in vm.users\" ng-change=\"vm.addUserToCp(vm.user)\"></select>\n        </div>  \n        <div class=\"span4 text-right\">\n          <button class=\"btn btn-success margin-wells\">\n            Save\n          </button>\n        </div>\n      </div>\n    </form>\n    <div class=\"alert\" ng-show=\"vm.result\" ng-class=\"{\'alert-success\': vm.result.status === 1,\'alert-error\': vm.result.status === 0}\">\n      {$ vm.result.msg $}\n    </div>\n  </div>\n</div>");}]);