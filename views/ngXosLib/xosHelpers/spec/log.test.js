/**
 * © OpenCORD
 *
 * Created by teone on 4/18/16.
 */

// TODO write tests for log

(function () {
  'use strict';

  xdescribe('The xos.helper module', function(){

    let log;

    // beforeEach(module('xos.helpers'));

    var mockLog;

    beforeEach(function() {
      mockLog = jasmine.createSpyObj('logMock', ['info']);
    });

    beforeEach(function() {
      angular.mock.module('xos.helpers', function($injector, $provide) {
        $provide.value('$log', mockLog);
        $provide.decorator('$log', $injector.get('logDecorator'));
      });
    });

    // beforeEach(inject(($log) => {
    //   log = $log;
    //   log.reset();
    // }));

    describe('The log decorator', () => {
      it('should not print anything', inject(($log) => {
        // spyOn(log, 'info');
        $log.info('test');
        // expect(mockLog.info).not.toHaveBeenCalled();
      }));

      xdescribe('if logging is enabled', () => {
        beforeEach(() => {
          window.location.href += '?debug=true'
        });

        it('should should log', () => {
          log.info('test');
          console.log(log.info.logs);
        });
      });
    });
  });
})();
