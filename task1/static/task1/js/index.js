var nodes  = document.querySelectorAll('li'),
    _nodes = [].slice.call(nodes, 0);

var getDirection = function (ev, obj) {
    var w = obj.offsetWidth,
        h = obj.offsetHeight,
        x = (ev.pageX - obj.offsetLeft - (w / 2) * (w > h ? (h / w) : 1)),
        y = (ev.pageY - obj.offsetTop - (h / 2) * (h > w ? (w / h) : 1)),
        d = Math.round( Math.atan2(y, x) / 1.57079633 + 5 ) % 4;
  
    return d;
};

var addClass = function ( ev, obj, state ) {
    var direction = getDirection( ev, obj ),
        class_suffix = "";
    
    obj.className = "";
    
    switch ( direction ) {
        case 0 : class_suffix = '-top';    break;
        case 1 : class_suffix = '-right';  break;
        case 2 : class_suffix = '-bottom'; break;
        case 3 : class_suffix = '-left';   break;
    }
    
    obj.classList.add( state + class_suffix );
};

// bind events
_nodes.forEach(function (el) {
    el.addEventListener('mouseover', function (ev) {
        addClass( ev, this, 'in' );
    }, false);

    el.addEventListener('mouseout', function (ev) {
        addClass( ev, this, 'out' );
    }, false);
});



//For view button
window.requestAnimFrame = (function () {
        return  window.requestAnimationFrame ||
            window.webkitRequestAnimationFrame ||
            window.mozRequestAnimationFrame ||
            window.oRequestAnimationFrame ||
            window.msRequestAnimationFrame ||
            function (callback) {
                window.setTimeout(callback, 1000 / 60);
            };
    })();

    Math.randMinMax = function(min, max, round) {
        var val = min + (Math.random() * (max - min));
        
        if( round ) val = Math.round( val );
        
        return val;
    };
    Math.TO_RAD = Math.PI/180;
    Math.getAngle = function( x1, y1, x2, y2 ) {
        
        var dx = x1 - x2,
            dy = y1 - y2;
        
        return Math.atan2(dy,dx);
    };
    Math.getDistance = function( x1, y1, x2, y2 ) {
        
        var     xs = x2 - x1,
            ys = y2 - y1;       
        
        xs *= xs;
        ys *= ys;
         
        return Math.sqrt( xs + ys );
    };