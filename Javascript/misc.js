
/* Quine */
// (function(){print("("+arguments.callee.toString().replace(/\s/g,'')+")()");})()
// f=_=>`f=${f};f()`;f()