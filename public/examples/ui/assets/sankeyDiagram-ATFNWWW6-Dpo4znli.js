var t,n,e;import{_ as i,d as r,g as s,s as o,b as a,c as l,q as c,p as h,t as u,e as f,o as y,P as d}from"./mermaid-BezMJi2d.js";import{s as p}from"./transform-C6EuPmuu.js";import{o as g}from"./ordinal-DDUp3AbE.js";import{c as _}from"./colors-bszWmPJw.js";import"./index-BDIgmJj6.js";import"./step-DY8hpDjU.js";import"./init-DLRA0X12.js";const m=_("4e79a7f28e2ce1575976b7b259a14fedc949af7aa1ff9da79c755fbab0ab");function x(t,n){return t<n?-1:t>n?1:t>=n?0:NaN}var k,v;function b(t,n){var e,i,r=t.length,s=-1;if(null==n){for(;++s<r;)if(null!=(e=t[s])&&e>=e)for(i=e;++s<r;)null!=(e=t[s])&&e>i&&(i=e)}else for(;++s<r;)if(null!=(e=n(t[s],s,t))&&e>=e)for(i=e;++s<r;)null!=(e=n(t[s],s,t))&&e>i&&(i=e);return i}function w(t,n){var e,i,r=t.length,s=-1;if(null==n){for(;++s<r;)if(null!=(e=t[s])&&e>=e)for(i=e;++s<r;)null!=(e=t[s])&&i>e&&(i=e)}else for(;++s<r;)if(null!=(e=n(t[s],s,t))&&e>=e)for(i=e;++s<r;)null!=(e=n(t[s],s,t))&&i>e&&(i=e);return i}function S(t,n){var e,i=t.length,r=-1,s=0;if(null==n)for(;++r<i;)(e=+t[r])&&(s+=e);else for(;++r<i;)(e=+n(t[r],r,t))&&(s+=e);return s}function E(t){return t.target.depth}function L(t,n){return t.sourceLinks.length?t.depth:n-1}function A(t){return function(){return t}}function M(t,n){return T(t.source,n.source)||t.index-n.index}function I(t,n){return T(t.target,n.target)||t.index-n.index}function T(t,n){return t.y0-n.y0}function N(t){return t.value}function P(t){return t.index}function j(t){return t.nodes}function O(t){return t.links}function C(t,n){const e=t.get(n);if(!e)throw new Error("missing: "+n);return e}function D({nodes:t}){for(const n of t){let t=n.y0,e=t;for(const i of n.sourceLinks)i.y0=t+i.width/2,t+=i.width;for(const i of n.targetLinks)i.y1=e+i.width/2,e+=i.width}}function $(){let t,n,e,i=0,r=0,s=1,o=1,a=24,l=8,c=P,h=L,u=j,f=O,y=6;function d(){const d={nodes:u.apply(null,arguments),links:f.apply(null,arguments)};return function({nodes:t,links:n}){for(const[e,r]of t.entries())r.index=e,r.sourceLinks=[],r.targetLinks=[];const i=new Map(t.map(((n,e)=>[c(n,e,t),n])));for(const[e,r]of n.entries()){r.index=e;let{source:t,target:n}=r;"object"!=typeof t&&(t=r.source=C(i,t)),"object"!=typeof n&&(n=r.target=C(i,n)),t.sourceLinks.push(r),n.targetLinks.push(r)}if(null!=e)for(const{sourceLinks:r,targetLinks:s}of t)r.sort(e),s.sort(e)}(d),function({nodes:t}){for(const n of t)n.value=void 0===n.fixedValue?Math.max(S(n.sourceLinks,N),S(n.targetLinks,N)):n.fixedValue}(d),function({nodes:t}){const n=t.length;let e=new Set(t),i=new Set,r=0;for(;e.size;){for(const t of e){t.depth=r;for(const{target:n}of t.sourceLinks)i.add(n)}if(++r>n)throw new Error("circular link");e=i,i=new Set}}(d),function({nodes:t}){const n=t.length;let e=new Set(t),i=new Set,r=0;for(;e.size;){for(const t of e){t.height=r;for(const{source:n}of t.targetLinks)i.add(n)}if(++r>n)throw new Error("circular link");e=i,i=new Set}}(d),function(e){const c=function({nodes:t}){const e=b(t,(t=>t.depth))+1,r=(s-i-a)/(e-1),o=new Array(e);for(const n of t){const t=Math.max(0,Math.min(e-1,Math.floor(h.call(null,n,e))));n.layer=t,n.x0=i+t*r,n.x1=n.x0+a,o[t]?o[t].push(n):o[t]=[n]}if(n)for(const i of o)i.sort(n);return o}(e);t=Math.min(l,(o-r)/(b(c,(t=>t.length))-1)),function(n){const e=w(n,(n=>(o-r-(n.length-1)*t)/S(n,N)));for(const i of n){let n=r;for(const r of i){r.y0=n,r.y1=n+r.value*e,n=r.y1+t;for(const t of r.sourceLinks)t.width=t.value*e}n=(o-n+t)/(i.length+1);for(let t=0;t<i.length;++t){const e=i[t];e.y0+=n*(t+1),e.y1+=n*(t+1)}v(i)}}(c);for(let t=0;t<y;++t){const n=Math.pow(.99,t),e=Math.max(1-n,(t+1)/y);g(c,n,e),p(c,n,e)}}(d),D(d),d}function p(t,e,i){for(let r=1,s=t.length;r<s;++r){const s=t[r];for(const t of s){let n=0,i=0;for(const{source:e,value:s}of t.targetLinks){let r=s*(t.layer-e.layer);n+=E(e,t)*r,i+=r}if(!(i>0))continue;let r=(n/i-t.y0)*e;t.y0+=r,t.y1+=r,k(t)}void 0===n&&s.sort(T),_(s,i)}}function g(t,e,i){for(let r=t.length-2;r>=0;--r){const s=t[r];for(const t of s){let n=0,i=0;for(const{target:e,value:s}of t.sourceLinks){let r=s*(e.layer-t.layer);n+=$(t,e)*r,i+=r}if(!(i>0))continue;let r=(n/i-t.y0)*e;t.y0+=r,t.y1+=r,k(t)}void 0===n&&s.sort(T),_(s,i)}}function _(n,e){const i=n.length>>1,s=n[i];x(n,s.y0-t,i-1,e),m(n,s.y1+t,i+1,e),x(n,o,n.length-1,e),m(n,r,0,e)}function m(n,e,i,r){for(;i<n.length;++i){const s=n[i],o=(e-s.y0)*r;o>1e-6&&(s.y0+=o,s.y1+=o),e=s.y1+t}}function x(n,e,i,r){for(;i>=0;--i){const s=n[i],o=(s.y1-e)*r;o>1e-6&&(s.y0-=o,s.y1-=o),e=s.y0-t}}function k({sourceLinks:t,targetLinks:n}){if(void 0===e){for(const{source:{sourceLinks:t}}of n)t.sort(I);for(const{target:{targetLinks:n}}of t)n.sort(M)}}function v(t){if(void 0===e)for(const{sourceLinks:n,targetLinks:e}of t)n.sort(I),e.sort(M)}function E(n,e){let i=n.y0-(n.sourceLinks.length-1)*t/2;for(const{target:r,width:s}of n.sourceLinks){if(r===e)break;i+=s+t}for(const{source:t,width:r}of e.targetLinks){if(t===n)break;i-=r}return i}function $(n,e){let i=e.y0-(e.targetLinks.length-1)*t/2;for(const{source:r,width:s}of e.targetLinks){if(r===n)break;i+=s+t}for(const{target:t,width:r}of n.sourceLinks){if(t===e)break;i-=r}return i}return d.update=function(t){return D(t),t},d.nodeId=function(t){return arguments.length?(c="function"==typeof t?t:A(t),d):c},d.nodeAlign=function(t){return arguments.length?(h="function"==typeof t?t:A(t),d):h},d.nodeSort=function(t){return arguments.length?(n=t,d):n},d.nodeWidth=function(t){return arguments.length?(a=+t,d):a},d.nodePadding=function(n){return arguments.length?(l=t=+n,d):l},d.nodes=function(t){return arguments.length?(u="function"==typeof t?t:A(t),d):u},d.links=function(t){return arguments.length?(f="function"==typeof t?t:A(t),d):f},d.linkSort=function(t){return arguments.length?(e=t,d):e},d.size=function(t){return arguments.length?(i=r=0,s=+t[0],o=+t[1],d):[s-i,o-r]},d.extent=function(t){return arguments.length?(i=+t[0][0],s=+t[1][0],r=+t[0][1],o=+t[1][1],d):[[i,r],[s,o]]},d.iterations=function(t){return arguments.length?(y=+t,d):y},d}1===(k=x).length&&(v=k,k=function(t,n){return x(v(t),n)});var z=Math.PI,F=2*z,U=1e-6,W=F-U;function G(){this._x0=this._y0=this._x1=this._y1=null,this._=""}function X(){return new G}function q(t){return function(){return t}}function V(t){return t[0]}function Q(t){return t[1]}G.prototype=X.prototype={constructor:G,moveTo:function(t,n){this._+="M"+(this._x0=this._x1=+t)+","+(this._y0=this._y1=+n)},closePath:function(){null!==this._x1&&(this._x1=this._x0,this._y1=this._y0,this._+="Z")},lineTo:function(t,n){this._+="L"+(this._x1=+t)+","+(this._y1=+n)},quadraticCurveTo:function(t,n,e,i){this._+="Q"+ +t+","+ +n+","+(this._x1=+e)+","+(this._y1=+i)},bezierCurveTo:function(t,n,e,i,r,s){this._+="C"+ +t+","+ +n+","+ +e+","+ +i+","+(this._x1=+r)+","+(this._y1=+s)},arcTo:function(t,n,e,i,r){t=+t,n=+n,e=+e,i=+i,r=+r;var s=this._x1,o=this._y1,a=e-t,l=i-n,c=s-t,h=o-n,u=c*c+h*h;if(r<0)throw new Error("negative radius: "+r);if(null===this._x1)this._+="M"+(this._x1=t)+","+(this._y1=n);else if(u>U)if(Math.abs(h*a-l*c)>U&&r){var f=e-s,y=i-o,d=a*a+l*l,p=f*f+y*y,g=Math.sqrt(d),_=Math.sqrt(u),m=r*Math.tan((z-Math.acos((d+u-p)/(2*g*_)))/2),x=m/_,k=m/g;Math.abs(x-1)>U&&(this._+="L"+(t+x*c)+","+(n+x*h)),this._+="A"+r+","+r+",0,0,"+ +(h*f>c*y)+","+(this._x1=t+k*a)+","+(this._y1=n+k*l)}else this._+="L"+(this._x1=t)+","+(this._y1=n);else;},arc:function(t,n,e,i,r,s){t=+t,n=+n,s=!!s;var o=(e=+e)*Math.cos(i),a=e*Math.sin(i),l=t+o,c=n+a,h=1^s,u=s?i-r:r-i;if(e<0)throw new Error("negative radius: "+e);null===this._x1?this._+="M"+l+","+c:(Math.abs(this._x1-l)>U||Math.abs(this._y1-c)>U)&&(this._+="L"+l+","+c),e&&(u<0&&(u=u%F+F),u>W?this._+="A"+e+","+e+",0,1,"+h+","+(t-o)+","+(n-a)+"A"+e+","+e+",0,1,"+h+","+(this._x1=l)+","+(this._y1=c):u>U&&(this._+="A"+e+","+e+",0,"+ +(u>=z)+","+h+","+(this._x1=t+e*Math.cos(r))+","+(this._y1=n+e*Math.sin(r))))},rect:function(t,n,e,i){this._+="M"+(this._x0=this._x1=+t)+","+(this._y0=this._y1=+n)+"h"+ +e+"v"+ +i+"h"+-e+"Z"},toString:function(){return this._}};var R=Array.prototype.slice;function Y(t){return t.source}function B(t){return t.target}function K(t,n,e,i,r){t.moveTo(n,e),t.bezierCurveTo(n=(n+i)/2,e,n,r,i,r)}function Z(){return function(t){var n=Y,e=B,i=V,r=Q,s=null;function o(){var o,a=R.call(arguments),l=n.apply(this,a),c=e.apply(this,a);if(s||(s=o=X()),t(s,+i.apply(this,(a[0]=l,a)),+r.apply(this,a),+i.apply(this,(a[0]=c,a)),+r.apply(this,a)),o)return s=null,o+""||null}return o.source=function(t){return arguments.length?(n=t,o):n},o.target=function(t){return arguments.length?(e=t,o):e},o.x=function(t){return arguments.length?(i="function"==typeof t?t:q(+t),o):i},o.y=function(t){return arguments.length?(r="function"==typeof t?t:q(+t),o):r},o.context=function(t){return arguments.length?(s=null==t?null:t,o):s},o}(K)}function H(t){return[t.source.x1,t.y0]}function J(t){return[t.target.x0,t.y1]}var tt=function(){var t=i((function(t,n,e,i){for(e=e||{},i=t.length;i--;e[t[i]]=n);return e}),"o"),n=[1,9],e=[1,10],r=[1,5,10,12],s={trace:i((function(){}),"trace"),yy:{},symbols_:{error:2,start:3,SANKEY:4,NEWLINE:5,csv:6,opt_eof:7,record:8,csv_tail:9,EOF:10,"field[source]":11,COMMA:12,"field[target]":13,"field[value]":14,field:15,escaped:16,non_escaped:17,DQUOTE:18,ESCAPED_TEXT:19,NON_ESCAPED_TEXT:20,$accept:0,$end:1},terminals_:{2:"error",4:"SANKEY",5:"NEWLINE",10:"EOF",11:"field[source]",12:"COMMA",13:"field[target]",14:"field[value]",18:"DQUOTE",19:"ESCAPED_TEXT",20:"NON_ESCAPED_TEXT"},productions_:[0,[3,4],[6,2],[9,2],[9,0],[7,1],[7,0],[8,5],[15,1],[15,1],[16,3],[17,1]],performAction:i((function(t,n,e,i,r,s,o){var a=s.length-1;switch(r){case 7:const t=i.findOrCreateNode(s[a-4].trim().replaceAll('""','"')),n=i.findOrCreateNode(s[a-2].trim().replaceAll('""','"')),e=parseFloat(s[a].trim());i.addLink(t,n,e);break;case 8:case 9:case 11:this.$=s[a];break;case 10:this.$=s[a-1]}}),"anonymous"),table:[{3:1,4:[1,2]},{1:[3]},{5:[1,3]},{6:4,8:5,15:6,16:7,17:8,18:n,20:e},{1:[2,6],7:11,10:[1,12]},t(e,[2,4],{9:13,5:[1,14]}),{12:[1,15]},t(r,[2,8]),t(r,[2,9]),{19:[1,16]},t(r,[2,11]),{1:[2,1]},{1:[2,5]},t(e,[2,2]),{6:17,8:5,15:6,16:7,17:8,18:n,20:e},{15:18,16:7,17:8,18:n,20:e},{18:[1,19]},t(e,[2,3]),{12:[1,20]},t(r,[2,10]),{15:21,16:7,17:8,18:n,20:e},t([1,5,10],[2,7])],defaultActions:{11:[2,1],12:[2,5]},parseError:i((function(t,n){if(!n.recoverable){var e=new Error(t);throw e.hash=n,e}this.trace(t)}),"parseError"),parse:i((function(t){var n=this,e=[0],r=[],s=[null],o=[],a=this.table,l="",c=0,h=0,u=o.slice.call(arguments,1),f=Object.create(this.lexer),y={yy:{}};for(var d in this.yy)Object.prototype.hasOwnProperty.call(this.yy,d)&&(y.yy[d]=this.yy[d]);f.setInput(t,y.yy),y.yy.lexer=f,y.yy.parser=this,void 0===f.yylloc&&(f.yylloc={});var p=f.yylloc;o.push(p);var g=f.options&&f.options.ranges;function _(){var t;return"number"!=typeof(t=r.pop()||f.lex()||1)&&(t instanceof Array&&(t=(r=t).pop()),t=n.symbols_[t]||t),t}"function"==typeof y.yy.parseError?this.parseError=y.yy.parseError:this.parseError=Object.getPrototypeOf(this).parseError,i((function(t){e.length=e.length-2*t,s.length=s.length-t,o.length=o.length-t}),"popStack"),i(_,"lex");for(var m,x,k,v,b,w,S,E,L={};;){if(x=e[e.length-1],this.defaultActions[x]?k=this.defaultActions[x]:(null==m&&(m=_()),k=a[x]&&a[x][m]),void 0===k||!k.length||!k[0]){var A="";for(b in E=[],a[x])this.terminals_[b]&&b>2&&E.push("'"+this.terminals_[b]+"'");A=f.showPosition?"Parse error on line "+(c+1)+":\n"+f.showPosition()+"\nExpecting "+E.join(", ")+", got '"+(this.terminals_[m]||m)+"'":"Parse error on line "+(c+1)+": Unexpected "+(1==m?"end of input":"'"+(this.terminals_[m]||m)+"'"),this.parseError(A,{text:f.match,token:this.terminals_[m]||m,line:f.yylineno,loc:p,expected:E})}if(k[0]instanceof Array&&k.length>1)throw new Error("Parse Error: multiple actions possible at state: "+x+", token: "+m);switch(k[0]){case 1:e.push(m),s.push(f.yytext),o.push(f.yylloc),e.push(k[1]),m=null,h=f.yyleng,l=f.yytext,c=f.yylineno,p=f.yylloc;break;case 2:if(w=this.productions_[k[1]][1],L.$=s[s.length-w],L._$={first_line:o[o.length-(w||1)].first_line,last_line:o[o.length-1].last_line,first_column:o[o.length-(w||1)].first_column,last_column:o[o.length-1].last_column},g&&(L._$.range=[o[o.length-(w||1)].range[0],o[o.length-1].range[1]]),void 0!==(v=this.performAction.apply(L,[l,h,c,y.yy,k[1],s,o].concat(u))))return v;w&&(e=e.slice(0,-1*w*2),s=s.slice(0,-1*w),o=o.slice(0,-1*w)),e.push(this.productions_[k[1]][0]),s.push(L.$),o.push(L._$),S=a[e[e.length-2]][e[e.length-1]],e.push(S);break;case 3:return!0}}return!0}),"parse")},o=function(){return{EOF:1,parseError:i((function(t,n){if(!this.yy.parser)throw new Error(t);this.yy.parser.parseError(t,n)}),"parseError"),setInput:i((function(t,n){return this.yy=n||this.yy||{},this._input=t,this._more=this._backtrack=this.done=!1,this.yylineno=this.yyleng=0,this.yytext=this.matched=this.match="",this.conditionStack=["INITIAL"],this.yylloc={first_line:1,first_column:0,last_line:1,last_column:0},this.options.ranges&&(this.yylloc.range=[0,0]),this.offset=0,this}),"setInput"),input:i((function(){var t=this._input[0];return this.yytext+=t,this.yyleng++,this.offset++,this.match+=t,this.matched+=t,t.match(/(?:\r\n?|\n).*/g)?(this.yylineno++,this.yylloc.last_line++):this.yylloc.last_column++,this.options.ranges&&this.yylloc.range[1]++,this._input=this._input.slice(1),t}),"input"),unput:i((function(t){var n=t.length,e=t.split(/(?:\r\n?|\n)/g);this._input=t+this._input,this.yytext=this.yytext.substr(0,this.yytext.length-n),this.offset-=n;var i=this.match.split(/(?:\r\n?|\n)/g);this.match=this.match.substr(0,this.match.length-1),this.matched=this.matched.substr(0,this.matched.length-1),e.length-1&&(this.yylineno-=e.length-1);var r=this.yylloc.range;return this.yylloc={first_line:this.yylloc.first_line,last_line:this.yylineno+1,first_column:this.yylloc.first_column,last_column:e?(e.length===i.length?this.yylloc.first_column:0)+i[i.length-e.length].length-e[0].length:this.yylloc.first_column-n},this.options.ranges&&(this.yylloc.range=[r[0],r[0]+this.yyleng-n]),this.yyleng=this.yytext.length,this}),"unput"),more:i((function(){return this._more=!0,this}),"more"),reject:i((function(){return this.options.backtrack_lexer?(this._backtrack=!0,this):this.parseError("Lexical error on line "+(this.yylineno+1)+". You can only invoke reject() in the lexer when the lexer is of the backtracking persuasion (options.backtrack_lexer = true).\n"+this.showPosition(),{text:"",token:null,line:this.yylineno})}),"reject"),less:i((function(t){this.unput(this.match.slice(t))}),"less"),pastInput:i((function(){var t=this.matched.substr(0,this.matched.length-this.match.length);return(t.length>20?"...":"")+t.substr(-20).replace(/\n/g,"")}),"pastInput"),upcomingInput:i((function(){var t=this.match;return t.length<20&&(t+=this._input.substr(0,20-t.length)),(t.substr(0,20)+(t.length>20?"...":"")).replace(/\n/g,"")}),"upcomingInput"),showPosition:i((function(){var t=this.pastInput(),n=new Array(t.length+1).join("-");return t+this.upcomingInput()+"\n"+n+"^"}),"showPosition"),test_match:i((function(t,n){var e,i,r;if(this.options.backtrack_lexer&&(r={yylineno:this.yylineno,yylloc:{first_line:this.yylloc.first_line,last_line:this.last_line,first_column:this.yylloc.first_column,last_column:this.yylloc.last_column},yytext:this.yytext,match:this.match,matches:this.matches,matched:this.matched,yyleng:this.yyleng,offset:this.offset,_more:this._more,_input:this._input,yy:this.yy,conditionStack:this.conditionStack.slice(0),done:this.done},this.options.ranges&&(r.yylloc.range=this.yylloc.range.slice(0))),(i=t[0].match(/(?:\r\n?|\n).*/g))&&(this.yylineno+=i.length),this.yylloc={first_line:this.yylloc.last_line,last_line:this.yylineno+1,first_column:this.yylloc.last_column,last_column:i?i[i.length-1].length-i[i.length-1].match(/\r?\n?/)[0].length:this.yylloc.last_column+t[0].length},this.yytext+=t[0],this.match+=t[0],this.matches=t,this.yyleng=this.yytext.length,this.options.ranges&&(this.yylloc.range=[this.offset,this.offset+=this.yyleng]),this._more=!1,this._backtrack=!1,this._input=this._input.slice(t[0].length),this.matched+=t[0],e=this.performAction.call(this,this.yy,this,n,this.conditionStack[this.conditionStack.length-1]),this.done&&this._input&&(this.done=!1),e)return e;if(this._backtrack){for(var s in r)this[s]=r[s];return!1}return!1}),"test_match"),next:i((function(){if(this.done)return this.EOF;var t,n,e,i;this._input||(this.done=!0),this._more||(this.yytext="",this.match="");for(var r=this._currentRules(),s=0;s<r.length;s++)if((e=this._input.match(this.rules[r[s]]))&&(!n||e[0].length>n[0].length)){if(n=e,i=s,this.options.backtrack_lexer){if(!1!==(t=this.test_match(e,r[s])))return t;if(this._backtrack){n=!1;continue}return!1}if(!this.options.flex)break}return n?!1!==(t=this.test_match(n,r[i]))&&t:""===this._input?this.EOF:this.parseError("Lexical error on line "+(this.yylineno+1)+". Unrecognized text.\n"+this.showPosition(),{text:"",token:null,line:this.yylineno})}),"next"),lex:i((function(){var t=this.next();return t||this.lex()}),"lex"),begin:i((function(t){this.conditionStack.push(t)}),"begin"),popState:i((function(){return this.conditionStack.length-1>0?this.conditionStack.pop():this.conditionStack[0]}),"popState"),_currentRules:i((function(){return this.conditionStack.length&&this.conditionStack[this.conditionStack.length-1]?this.conditions[this.conditionStack[this.conditionStack.length-1]].rules:this.conditions.INITIAL.rules}),"_currentRules"),topState:i((function(t){return(t=this.conditionStack.length-1-Math.abs(t||0))>=0?this.conditionStack[t]:"INITIAL"}),"topState"),pushState:i((function(t){this.begin(t)}),"pushState"),stateStackSize:i((function(){return this.conditionStack.length}),"stateStackSize"),options:{"case-insensitive":!0},performAction:i((function(t,n,e,i){switch(e){case 0:return this.pushState("csv"),4;case 1:return 10;case 2:return 5;case 3:return 12;case 4:return this.pushState("escaped_text"),18;case 5:return 20;case 6:return this.popState("escaped_text"),18;case 7:return 19}}),"anonymous"),rules:[/^(?:sankey-beta\b)/i,/^(?:$)/i,/^(?:((\u000D\u000A)|(\u000A)))/i,/^(?:(\u002C))/i,/^(?:(\u0022))/i,/^(?:([\u0020-\u0021\u0023-\u002B\u002D-\u007E])*)/i,/^(?:(\u0022)(?!(\u0022)))/i,/^(?:(([\u0020-\u0021\u0023-\u002B\u002D-\u007E])|(\u002C)|(\u000D)|(\u000A)|(\u0022)(\u0022))*)/i],conditions:{csv:{rules:[1,2,3,4,5,6,7],inclusive:!1},escaped_text:{rules:[6,7],inclusive:!1},INITIAL:{rules:[0,1,2,3,4,5,6,7],inclusive:!0}}}}();function a(){this.yy={}}return s.lexer=o,i(a,"Parser"),a.prototype=s,s.Parser=a,new a}();tt.parser=tt;var nt=tt,et=[],it=[],rt=new Map,st=i((()=>{et=[],it=[],rt=new Map,u()}),"clear"),ot=(i(t=class{constructor(t,n,e=0){this.source=t,this.target=n,this.value=e}},"SankeyLink"),t),at=i(((t,n,e)=>{et.push(new ot(t,n,e))}),"addLink"),lt=(i(n=class{constructor(t){this.ID=t}},"SankeyNode"),n),ct=i((t=>{t=f.sanitizeText(t,r());let n=rt.get(t);return void 0===n&&(n=new lt(t),rt.set(t,n),it.push(n)),n}),"findOrCreateNode"),ht=i((()=>it),"getNodes"),ut=i((()=>et),"getLinks"),ft=i((()=>({nodes:it.map((t=>({id:t.ID}))),links:et.map((t=>({source:t.source.ID,target:t.target.ID,value:t.value})))})),"getGraph"),yt={nodesMap:rt,getConfig:i((()=>r().sankey),"getConfig"),getNodes:ht,getLinks:ut,getGraph:ft,addLink:at,findOrCreateNode:ct,getAccTitle:s,setAccTitle:o,getAccDescription:a,setAccDescription:l,getDiagramTitle:c,setDiagramTitle:h,clear:st},dt=(i(e=class{static next(t){return new e(t+ ++e.count)}constructor(t){this.id=t,this.href=`#${t}`}toString(){return"url("+this.href+")"}},"Uid"),e.count=0,e),pt={left:function(t){return t.depth},right:function(t,n){return n-1-t.height},center:function(t){return t.targetLinks.length?t.depth:t.sourceLinks.length?w(t.sourceLinks,E)-1:0},justify:L},gt={draw:i((function(t,n,e,s){const{securityLevel:o,sankey:a}=r(),l=y.sankey;let c;"sandbox"===o&&(c=p("#i"+n));const h=p("sandbox"===o?c.nodes()[0].contentDocument.body:"body"),u="sandbox"===o?h.select(`[id="${n}"]`):p(`[id="${n}"]`),f=(null==a?void 0:a.width)??l.width,_=(null==a?void 0:a.height)??l.width,x=(null==a?void 0:a.useMaxWidth)??l.useMaxWidth,k=(null==a?void 0:a.nodeAlignment)??l.nodeAlignment,v=(null==a?void 0:a.prefix)??l.prefix,b=(null==a?void 0:a.suffix)??l.suffix,w=(null==a?void 0:a.showValues)??l.showValues,S=s.db.getGraph(),E=pt[k];$().nodeId((t=>t.id)).nodeWidth(10).nodePadding(10+(w?15:0)).nodeAlign(E).extent([[0,0],[f,_]])(S);const L=g(m);u.append("g").attr("class","nodes").selectAll(".node").data(S.nodes).join("g").attr("class","node").attr("id",(t=>(t.uid=dt.next("node-")).id)).attr("transform",(function(t){return"translate("+t.x0+","+t.y0+")"})).attr("x",(t=>t.x0)).attr("y",(t=>t.y0)).append("rect").attr("height",(t=>t.y1-t.y0)).attr("width",(t=>t.x1-t.x0)).attr("fill",(t=>L(t.id)));const A=i((({id:t,value:n})=>w?`${t}\n${v}${Math.round(100*n)/100}${b}`:t),"getText");u.append("g").attr("class","node-labels").attr("font-family","sans-serif").attr("font-size",14).selectAll("text").data(S.nodes).join("text").attr("x",(t=>t.x0<f/2?t.x1+6:t.x0-6)).attr("y",(t=>(t.y1+t.y0)/2)).attr("dy",(w?"0":"0.35")+"em").attr("text-anchor",(t=>t.x0<f/2?"start":"end")).text(A);const M=u.append("g").attr("class","links").attr("fill","none").attr("stroke-opacity",.5).selectAll(".link").data(S.links).join("g").attr("class","link").style("mix-blend-mode","multiply"),I=(null==a?void 0:a.linkColor)??"gradient";if("gradient"===I){const t=M.append("linearGradient").attr("id",(t=>(t.uid=dt.next("linearGradient-")).id)).attr("gradientUnits","userSpaceOnUse").attr("x1",(t=>t.source.x1)).attr("x2",(t=>t.target.x0));t.append("stop").attr("offset","0%").attr("stop-color",(t=>L(t.source.id))),t.append("stop").attr("offset","100%").attr("stop-color",(t=>L(t.target.id)))}let T;switch(I){case"gradient":T=i((t=>t.uid),"coloring");break;case"source":T=i((t=>L(t.source.id)),"coloring");break;case"target":T=i((t=>L(t.target.id)),"coloring");break;default:T=I}M.append("path").attr("d",Z().source(H).target(J)).attr("stroke",T).attr("stroke-width",(t=>Math.max(1,t.width))),d(void 0,u,0,x)}),"draw")},_t=i((t=>t.replaceAll(/^[^\S\n\r]+|[^\S\n\r]+$/g,"").replaceAll(/([\n\r])+/g,"\n").trim()),"prepareTextForParsing"),mt=nt.parse.bind(nt);nt.parse=t=>mt(_t(t));var xt={parser:nt,db:yt,renderer:gt};export{xt as diagram};
