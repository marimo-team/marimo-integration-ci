import{p as t}from"./chunk-RYO7GUH3-VkcPC0x4.js";import{A as e,p as a,q as n,s as i,g as r,c as o,b as s,_ as l,l as p,t as c,d,B as u,G as f,N as m,j as g}from"./mermaid-BezMJi2d.js";import{p as h}from"./gitGraph-YCYPL57B-dD4eYAH1.js";import"./transform-C6EuPmuu.js";import{d as x}from"./arc-y9WbYkJu.js";import{o as y}from"./ordinal-DDUp3AbE.js";import{a as w,t as S,o as $}from"./step-DY8hpDjU.js";import"./index-BDIgmJj6.js";import"./main-cdvIQCIX.js";import"./_baseEach-fmc3zLor.js";import"./_baseUniq-Co9GIZ92.js";import"./min-A9Pie6I4.js";import"./_baseMap-BwqkuE75.js";import"./clone-Cr0ountK.js";import"./init-DLRA0X12.js";function A(t,e){return e<t?-1:e>t?1:e>=t?0:NaN}function b(t){return t}var T=e.pie,j={sections:new Map,showData:!1,config:T},v=j.sections,C=j.showData,D=structuredClone(T),k={getConfig:l((()=>structuredClone(D)),"getConfig"),clear:l((()=>{v=new Map,C=j.showData,c()}),"clear"),setDiagramTitle:a,getDiagramTitle:n,setAccTitle:i,getAccTitle:r,setAccDescription:o,getAccDescription:s,addSection:l((({label:t,value:e})=>{v.has(t)||(v.set(t,e),p.debug(`added new section: ${t}, with value: ${e}`))}),"addSection"),getSections:l((()=>v),"getSections"),setShowData:l((t=>{C=t}),"setShowData"),getShowData:l((()=>C),"getShowData")},M=l(((e,a)=>{t(e,a),a.setShowData(e.showData),e.sections.map(a.addSection)}),"populateDb"),O={parse:l((async t=>{const e=await h("pie",t);p.debug(e),M(e,k)}),"parse")},z=l((t=>`\n  .pieCircle{\n    stroke: ${t.pieStrokeColor};\n    stroke-width : ${t.pieStrokeWidth};\n    opacity : ${t.pieOpacity};\n  }\n  .pieOuterCircle{\n    stroke: ${t.pieOuterStrokeColor};\n    stroke-width: ${t.pieOuterStrokeWidth};\n    fill: none;\n  }\n  .pieTitleText {\n    text-anchor: middle;\n    font-size: ${t.pieTitleTextSize};\n    fill: ${t.pieTitleTextColor};\n    font-family: ${t.fontFamily};\n  }\n  .slice {\n    font-family: ${t.fontFamily};\n    fill: ${t.pieSectionTextColor};\n    font-size:${t.pieSectionTextSize};\n    // fill: white;\n  }\n  .legend text {\n    fill: ${t.pieLegendTextColor};\n    font-family: ${t.fontFamily};\n    font-size: ${t.pieLegendTextSize};\n  }\n`),"getStyles"),R=l((t=>{const e=[...t.entries()].map((t=>({label:t[0],value:t[1]}))).sort(((t,e)=>e.value-t.value));return function(){var t=b,e=A,a=null,n=w(0),i=w(S),r=w(0);function o(o){var s,l,p,c,d,u=(o=$(o)).length,f=0,m=new Array(u),g=new Array(u),h=+n.apply(this,arguments),x=Math.min(S,Math.max(-S,i.apply(this,arguments)-h)),y=Math.min(Math.abs(x)/u,r.apply(this,arguments)),w=y*(x<0?-1:1);for(s=0;s<u;++s)(d=g[m[s]=s]=+t(o[s],s,o))>0&&(f+=d);for(null!=e?m.sort((function(t,a){return e(g[t],g[a])})):null!=a&&m.sort((function(t,e){return a(o[t],o[e])})),s=0,p=f?(x-u*w)/f:0;s<u;++s,h=c)l=m[s],c=h+((d=g[l])>0?d*p:0)+w,g[l]={data:o[l],index:s,value:d,startAngle:h,endAngle:c,padAngle:y};return g}return o.value=function(e){return arguments.length?(t="function"==typeof e?e:w(+e),o):t},o.sortValues=function(t){return arguments.length?(e=t,a=null,o):e},o.sort=function(t){return arguments.length?(a=t,e=null,o):a},o.startAngle=function(t){return arguments.length?(n="function"==typeof t?t:w(+t),o):n},o.endAngle=function(t){return arguments.length?(i="function"==typeof t?t:w(+t),o):i},o.padAngle=function(t){return arguments.length?(r="function"==typeof t?t:w(+t),o):r},o}().value((t=>t.value))(e)}),"createPieArcs"),W={parser:O,db:k,renderer:{draw:l(((t,e,a,n)=>{p.debug("rendering pie chart\n"+t);const i=n.db,r=d(),o=u(i.getConfig(),r.pie),s=18,l=450,c=l,h=f(e),w=h.append("g");w.attr("transform","translate(225,225)");const{themeVariables:S}=r;let[$]=m(S.pieOuterStrokeWidth);$??($=2);const A=o.textPosition,b=Math.min(c,l)/2-40,T=x().innerRadius(0).outerRadius(b),j=x().innerRadius(b*A).outerRadius(b*A);w.append("circle").attr("cx",0).attr("cy",0).attr("r",b+$/2).attr("class","pieOuterCircle");const v=i.getSections(),C=R(v),D=[S.pie1,S.pie2,S.pie3,S.pie4,S.pie5,S.pie6,S.pie7,S.pie8,S.pie9,S.pie10,S.pie11,S.pie12],k=y(D);w.selectAll("mySlices").data(C).enter().append("path").attr("d",T).attr("fill",(t=>k(t.data.label))).attr("class","pieCircle");let M=0;v.forEach((t=>{M+=t})),w.selectAll("mySlices").data(C).enter().append("text").text((t=>(t.data.value/M*100).toFixed(0)+"%")).attr("transform",(t=>"translate("+j.centroid(t)+")")).style("text-anchor","middle").attr("class","slice"),w.append("text").text(i.getDiagramTitle()).attr("x",0).attr("y",-200).attr("class","pieTitleText");const O=w.selectAll(".legend").data(k.domain()).enter().append("g").attr("class","legend").attr("transform",((t,e)=>"translate(216,"+(22*e-22*k.domain().length/2)+")"));O.append("rect").attr("width",s).attr("height",s).style("fill",k).style("stroke",k),O.data(C).append("text").attr("x",22).attr("y",14).text((t=>{const{label:e,value:a}=t.data;return i.getShowData()?`${e} [${a}]`:e}));const z=512+Math.max(...O.selectAll("text").nodes().map((t=>(null==t?void 0:t.getBoundingClientRect().width)??0)));h.attr("viewBox",`0 0 ${z} 450`),g(h,l,z,o.useMaxWidth)}),"draw")},styles:z};export{W as diagram};
