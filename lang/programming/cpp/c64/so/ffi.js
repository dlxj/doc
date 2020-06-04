var FFI = require('ffi');
var hi = new FFI.Library('./libtest', {
   'test': [
      'void', []
   ]
});
console.log ( hi.test() );
