import{m as e,c as t,a as n,u as i,s as r,i as a,b as o,p as s,d,e as l,f as c,g as h}from"./chunk-REEJFE46-pDbyExtH.js";import{c as g,a as f,s as p}from"./chunk-NGC4727B-CO3v7Ghw.js";import{_ as u,l as w,d as y,u as b,P as v,Q as m,R as x,v as N,e as E,S,T,V as C}from"./mermaid-BezMJi2d.js";import{s as k}from"./transform-C6EuPmuu.js";import{G as X}from"./graph-S7F5Wm7J.js";import{l as D}from"./layout-BcoO_dxe.js";import{w as B}from"./json-DAxL3yxf.js";import{n as L}from"./step-DY8hpDjU.js";import"./index-BDIgmJj6.js";import"./_baseUniq-Co9GIZ92.js";import"./_baseEach-fmc3zLor.js";import"./min-A9Pie6I4.js";import"./_baseMap-BwqkuE75.js";import"./sortBy-DmmQPxuV.js";import"./clone-Cr0ountK.js";var j={},O={},R={},G=u((()=>{O={},R={},j={}}),"clear"),I=u(((e,t)=>(w.trace("In isDescendant",t," ",e," = ",O[t].includes(e)),!!O[t].includes(e))),"isDescendant"),J=u(((e,t)=>(w.info("Descendants of ",t," is ",O[t]),w.info("Edge is ",e),e.v!==t&&(e.w!==t&&(O[t]?O[t].includes(e.v)||I(e.v,t)||I(e.w,t)||O[t].includes(e.w):(w.debug("Tilt, ",t,",not in descendants"),!1))))),"edgeInCluster"),A=u(((e,t,n,i)=>{w.warn("Copying children of ",e,"root",i,"data",t.node(e),i);const r=t.children(e)||[];e!==i&&r.push(e),w.warn("Copying (nodes) clusterId",e,"nodes",r),r.forEach((r=>{if(t.children(r).length>0)A(r,t,n,i);else{const a=t.node(r);w.info("cp ",r," to ",i," with parent ",e),n.setNode(r,a),i!==t.parent(r)&&(w.warn("Setting parent",r,t.parent(r)),n.setParent(r,t.parent(r))),e!==i&&r!==e?(w.debug("Setting parent",r,e),n.setParent(r,e)):(w.info("In copy ",e,"root",i,"data",t.node(e),i),w.debug("Not Setting parent for node=",r,"cluster!==rootId",e!==i,"node!==clusterId",r!==e));const o=t.edges(r);w.debug("Copying Edges",o),o.forEach((r=>{w.info("Edge",r);const a=t.edge(r.v,r.w,r.name);w.info("Edge data",a,i);try{J(r,i)?(w.info("Copying as ",r.v,r.w,a,r.name),n.setEdge(r.v,r.w,a,r.name),w.info("newGraph edges ",n.edges(),n.edge(n.edges()[0]))):w.info("Skipping copy of edge ",r.v,"--\x3e",r.w," rootId: ",i," clusterId:",e)}catch(o){w.error(o)}}))}w.debug("Removing node",r),t.removeNode(r)}))}),"copy"),M=u(((e,t)=>{const n=t.children(e);let i=[...n];for(const r of n)R[r]=e,i=[...i,...M(r,t)];return i}),"extractDescendants"),P=u(((e,t)=>{w.trace("Searching",e);const n=t.children(e);if(w.trace("Searching children of id ",e,n),n.length<1)return w.trace("This is a valid node",e),e;for(const i of n){const n=P(i,t);if(n)return w.trace("Found replacement for",e," => ",n),n}}),"findNonClusterChild"),F=u((e=>j[e]&&j[e].externalConnections&&j[e]?j[e].id:e),"getAnchorId"),$=u(((e,t)=>{if(!e||t>10)w.debug("Opting out, no graph ");else{w.debug("Opting in, graph "),e.nodes().forEach((function(t){e.children(t).length>0&&(w.warn("Cluster identified",t," Replacement id in edges: ",P(t,e)),O[t]=M(t,e),j[t]={id:P(t,e),clusterData:e.node(t)})})),e.nodes().forEach((function(t){const n=e.children(t),i=e.edges();n.length>0?(w.debug("Cluster identified",t,O),i.forEach((e=>{if(e.v!==t&&e.w!==t){I(e.v,t)^I(e.w,t)&&(w.warn("Edge: ",e," leaves cluster ",t),w.warn("Descendants of XXX ",t,": ",O[t]),j[t].externalConnections=!0)}}))):w.debug("Not a cluster ",t,O)}));for(let t of Object.keys(j)){const n=j[t].id,i=e.parent(n);i!==t&&j[i]&&!j[i].externalConnections&&(j[t].id=i)}e.edges().forEach((function(t){const n=e.edge(t);w.warn("Edge "+t.v+" -> "+t.w+": "+JSON.stringify(t)),w.warn("Edge "+t.v+" -> "+t.w+": "+JSON.stringify(e.edge(t)));let i=t.v,r=t.w;if(w.warn("Fix XXX",j,"ids:",t.v,t.w,"Translating: ",j[t.v]," --- ",j[t.w]),j[t.v]&&j[t.w]&&j[t.v]===j[t.w]){w.warn("Fixing and trixing link to self - removing XXX",t.v,t.w,t.name),w.warn("Fixing and trixing - removing XXX",t.v,t.w,t.name),i=F(t.v),r=F(t.w),e.removeEdge(t.v,t.w,t.name);const a=t.w+"---"+t.v;e.setNode(a,{domId:a,id:a,labelStyle:"",labelText:n.label,padding:0,shape:"labelRect",style:""});const o=structuredClone(n),s=structuredClone(n);o.label="",o.arrowTypeEnd="none",s.label="",o.fromCluster=t.v,s.toCluster=t.v,e.setEdge(i,a,o,t.name+"-cyclic-special"),e.setEdge(a,r,s,t.name+"-cyclic-special")}else if(j[t.v]||j[t.w]){if(w.warn("Fixing and trixing - removing XXX",t.v,t.w,t.name),i=F(t.v),r=F(t.w),e.removeEdge(t.v,t.w,t.name),i!==t.v){const r=e.parent(i);j[r].externalConnections=!0,n.fromCluster=t.v}if(r!==t.w){const i=e.parent(r);j[i].externalConnections=!0,n.toCluster=t.w}w.warn("Fix Replacing with XXX",i,r,t.name),e.setEdge(i,r,n,t.name)}})),w.warn("Adjusted Graph",B(e)),_(e,0),w.trace(j)}}),"adjustClustersAndEdges"),_=u(((e,t)=>{var n,i;if(w.warn("extractor - ",t,B(e),e.children("D")),t>10)return void w.error("Bailing out");let r=e.nodes(),a=!1;for(const o of r){const t=e.children(o);a=a||t.length>0}if(a){w.debug("Nodes = ",r,t);for(const a of r)if(w.debug("Extracting node",a,j,j[a]&&!j[a].externalConnections,!e.parent(a),e.node(a),e.children("D")," Depth ",t),j[a])if(!j[a].externalConnections&&e.children(a)&&e.children(a).length>0){w.warn("Cluster without external connections, without a parent and with children",a,t);let r="TB"===e.graph().rankdir?"LR":"TB";(null==(i=null==(n=j[a])?void 0:n.clusterData)?void 0:i.dir)&&(r=j[a].clusterData.dir,w.warn("Fixing dir",j[a].clusterData.dir,r));const o=new X({multigraph:!0,compound:!0}).setGraph({rankdir:r,nodesep:50,ranksep:50,marginx:8,marginy:8}).setDefaultEdgeLabel((function(){return{}}));w.warn("Old graph before copy",B(e)),A(a,e,o,a),e.setNode(a,{clusterNode:!0,id:a,clusterData:j[a].clusterData,labelText:j[a].labelText,graph:o}),w.warn("New graph after copy node: (",a,")",B(o)),w.debug("Old graph after copy",B(e))}else w.warn("Cluster ** ",a," **not meeting the criteria !externalConnections:",!j[a].externalConnections," no parent: ",!e.parent(a)," children ",e.children(a)&&e.children(a).length>0,e.children("D"),t),w.debug(j);else w.debug("Not a cluster",a,t);r=e.nodes(),w.warn("New list of nodes",r);for(const n of r){const i=e.node(n);w.warn(" Now next level",n,i),i.clusterNode&&_(i.graph,t+1)}}else w.debug("Done, no node has children",e.nodes())}),"extractor"),W=u(((e,t)=>{if(0===t.length)return[];let n=Object.assign(t);return t.forEach((t=>{const i=e.children(t),r=W(e,i);n=[...n,...r]})),n}),"sorter"),H=u((e=>W(e,e.children())),"sortNodesByHierarchy"),q=u(((e,t)=>{w.info("Creating subgraph rect for ",t.id,t);const n=y(),i=e.insert("g").attr("class","cluster"+(t.class?" "+t.class:"")).attr("id",t.id),r=i.insert("rect",":first-child"),a=T(n.flowchart.htmlLabels),o=i.insert("g").attr("class","cluster-label"),s="markdown"===t.labelType?C(o,t.labelText,{style:t.labelStyle,useHtmlLabels:a},n):o.node().appendChild(c(t.labelText,t.labelStyle,void 0,!0));let d=s.getBBox();if(T(n.flowchart.htmlLabels)){const e=s.children[0],t=k(s);d=e.getBoundingClientRect(),t.attr("width",d.width),t.attr("height",d.height)}const l=0*t.padding,g=l/2,f=t.width<=d.width+l?d.width+l:t.width;t.width<=d.width+l?t.diff=(d.width-t.width)/2-t.padding/2:t.diff=-t.padding/2,w.trace("Data ",t,JSON.stringify(t)),r.attr("style",t.style).attr("rx",t.rx).attr("ry",t.ry).attr("x",t.x-f/2).attr("y",t.y-t.height/2-g).attr("width",f).attr("height",t.height+l);const{subGraphTitleTopMargin:p}=S(n);a?o.attr("transform",`translate(${t.x-d.width/2}, ${t.y-t.height/2+p})`):o.attr("transform",`translate(${t.x}, ${t.y-t.height/2+p})`);const u=r.node().getBBox();return t.width=u.width,t.height=u.height,t.intersect=function(e){return h(t,e)},i}),"rect"),z=u(((e,t)=>{const n=e.insert("g").attr("class","note-cluster").attr("id",t.id),i=n.insert("rect",":first-child"),r=0*t.padding,a=r/2;i.attr("rx",t.rx).attr("ry",t.ry).attr("x",t.x-t.width/2-a).attr("y",t.y-t.height/2-a).attr("width",t.width+r).attr("height",t.height+r).attr("fill","none");const o=i.node().getBBox();return t.width=o.width,t.height=o.height,t.intersect=function(e){return h(t,e)},n}),"noteGroup"),Q={rect:q,roundedWithTitle:u(((e,t)=>{const n=y(),i=e.insert("g").attr("class",t.classes).attr("id",t.id),r=i.insert("rect",":first-child"),a=i.insert("g").attr("class","cluster-label"),o=i.append("rect"),s=a.node().appendChild(c(t.labelText,t.labelStyle,void 0,!0));let d=s.getBBox();if(T(n.flowchart.htmlLabels)){const e=s.children[0],t=k(s);d=e.getBoundingClientRect(),t.attr("width",d.width),t.attr("height",d.height)}d=s.getBBox();const l=0*t.padding,g=l/2,f=t.width<=d.width+t.padding?d.width+t.padding:t.width;t.width<=d.width+t.padding?t.diff=(d.width+0*t.padding-t.width)/2:t.diff=-t.padding/2,r.attr("class","outer").attr("x",t.x-f/2-g).attr("y",t.y-t.height/2-g).attr("width",f+l).attr("height",t.height+l),o.attr("class","inner").attr("x",t.x-f/2-g).attr("y",t.y-t.height/2-g+d.height-1).attr("width",f+l).attr("height",t.height+l-d.height-3);const{subGraphTitleTopMargin:p}=S(n);a.attr("transform",`translate(${t.x-d.width/2}, ${t.y-t.height/2-t.padding/3+(T(n.flowchart.htmlLabels)?5:3)+p})`);const u=r.node().getBBox();return t.height=u.height,t.intersect=function(e){return h(t,e)},i}),"roundedWithTitle"),noteGroup:z,divider:u(((e,t)=>{const n=e.insert("g").attr("class",t.classes).attr("id",t.id),i=n.insert("rect",":first-child"),r=0*t.padding,a=r/2;i.attr("class","divider").attr("x",t.x-t.width/2-a).attr("y",t.y-t.height/2).attr("width",t.width+r).attr("height",t.height+r);const o=i.node().getBBox();return t.width=o.width,t.height=o.height,t.diff=-t.padding/2,t.intersect=function(e){return h(t,e)},n}),"divider")},U={},V=u(((e,t)=>{w.trace("Inserting cluster");const n=t.shape||"rect";U[t.id]=Q[n](e,t)}),"insertCluster"),K=u((()=>{U={}}),"clear"),Y=u((async(e,t,n,c,h,g)=>{w.info("Graph in recursive render: XXX",B(t),h);const f=t.graph().rankdir;w.trace("Dir in recursive render - dir:",f);const p=e.insert("g").attr("class","root");t.nodes()?w.info("Recursive render XXX",t.nodes()):w.info("No nodes found for",t),t.edges().length>0&&w.trace("Recursive edges",t.edge(t.edges()[0]));const u=p.insert("g").attr("class","clusters"),y=p.insert("g").attr("class","edgePaths"),b=p.insert("g").attr("class","edgeLabels"),v=p.insert("g").attr("class","nodes");await Promise.all(t.nodes().map((async function(e){const o=t.node(e);if(void 0!==h){const n=JSON.parse(JSON.stringify(h.clusterData));w.info("Setting data for cluster XXX (",e,") ",n,h),t.setNode(h.id,n),t.parent(e)||(w.trace("Setting parent",e,h.id),t.setParent(e,h.id,n))}if(w.info("(Insert) Node XXX"+e+": "+JSON.stringify(t.node(e))),null==o?void 0:o.clusterNode){w.info("Cluster identified",e,o.width,t.node(e));const{ranksep:a,nodesep:s}=t.graph();o.graph.setGraph({...o.graph.graph(),ranksep:a,nodesep:s});const d=await Y(v,o.graph,n,c,t.node(e),g),l=d.elem;i(o,l),o.diff=d.diff||0,w.info("Node bounds (abc123)",e,o,o.width,o.x,o.y),r(l,o),w.warn("Recursive render complete ",l,o)}else t.children(e).length>0?(w.info("Cluster - the non recursive path XXX",e,o.id,o,t),w.info(P(o.id,t)),j[o.id]={id:P(o.id,t),node:o}):(w.info("Node - the non recursive path",e,o.id,o),await a(v,t.node(e),{config:g,dir:f}))}))),t.edges().forEach((async function(e){const n=t.edge(e.v,e.w,e.name);w.info("Edge "+e.v+" -> "+e.w+": "+JSON.stringify(e)),w.info("Edge "+e.v+" -> "+e.w+": ",e," ",JSON.stringify(t.edge(e))),w.info("Fix",j,"ids:",e.v,e.w,"Translating: ",j[e.v],j[e.w]),await o(b,n)})),t.edges().forEach((function(e){w.info("Edge "+e.v+" -> "+e.w+": "+JSON.stringify(e))})),w.info("Graph before layout:",JSON.stringify(B(t))),w.info("#############################################"),w.info("###                Layout                 ###"),w.info("#############################################"),w.info(t),D(t),w.info("Graph after layout:",JSON.stringify(B(t)));let m=0;const{subGraphTitleTotalMargin:x}=S(g);return H(t).forEach((function(e){const n=t.node(e);w.info("Position "+e+": "+JSON.stringify(t.node(e))),w.info("Position "+e+": ("+n.x,","+n.y,") width: ",n.width," height: ",n.height),(null==n?void 0:n.clusterNode)?(n.y+=x,s(n)):t.children(e).length>0?(n.height+=x,V(u,n),j[n.id].node=n):(n.y+=x/2,s(n))})),t.edges().forEach((function(e){const i=t.edge(e);w.info("Edge "+e.v+" -> "+e.w+": "+JSON.stringify(i),i),i.points.forEach((e=>e.y+=x/2));const r=d(y,e,i,j,n,t,c);l(i,r)})),t.nodes().forEach((function(e){const n=t.node(e);w.info(e,n.type,n.diff),"group"===n.type&&(m=n.diff)})),{elem:p,diff:m}}),"recursiveRender"),Z=u((async(i,r,a,o,s)=>{e(i,a,o,s),t(),n(),K(),G(),w.warn("Graph at first:",JSON.stringify(B(r))),$(r),w.warn("Graph after:",JSON.stringify(B(r)));const d=y();await Y(i,r,o,s,void 0,d)}),"render"),ee=u((e=>E.sanitizeText(e,y())),"sanitizeText"),te={dividerMargin:10,padding:5,textHeight:10,curve:void 0},ne=u((function(e,t,n,i){w.info("keys:",[...e.keys()]),w.info(e),e.forEach((function(e){var r,a;const o={shape:"rect",id:e.id,domId:e.domId,labelText:ee(e.id),labelStyle:"",style:"fill: none; stroke: black",padding:(null==(r=y().flowchart)?void 0:r.padding)??(null==(a=y().class)?void 0:a.padding)};t.setNode(e.id,o),ie(e.classes,t,n,i,e.id),w.info("setNode",o)}))}),"addNamespaces"),ie=u((function(e,t,n,i,r){w.info("keys:",[...e.keys()]),w.info(e),[...e.values()].filter((e=>e.parent===r)).forEach((function(e){var n,a;const o=e.cssClasses.join(" "),s=m(e.styles),d=e.label??e.id,l={labelStyle:s.labelStyle,shape:"class_box",labelText:ee(d),classData:e,rx:0,ry:0,class:o,style:s.style,id:e.id,domId:e.domId,tooltip:i.db.getTooltip(e.id,r)||"",haveCallback:e.haveCallback,link:e.link,width:"group"===e.type?500:void 0,type:e.type,padding:(null==(n=y().flowchart)?void 0:n.padding)??(null==(a=y().class)?void 0:a.padding)};t.setNode(e.id,l),r&&t.setParent(e.id,r),w.info("setNode",l)}))}),"addClasses"),re=u((function(e,t,n,i){w.info(e),e.forEach((function(e,r){var a,o;const s=e,d="",l="",c=s.text,h={labelStyle:d,shape:"note",labelText:ee(c),noteData:s,rx:0,ry:0,class:"",style:l,id:s.id,domId:s.id,tooltip:"",type:"note",padding:(null==(a=y().flowchart)?void 0:a.padding)??(null==(o=y().class)?void 0:o.padding)};if(t.setNode(s.id,h),w.info("setNode",h),!s.class||!i.has(s.class))return;const g=n+r,f={id:`edgeNote${g}`,classes:"relation",pattern:"dotted",arrowhead:"none",startLabelRight:"",endLabelLeft:"",arrowTypeStart:"none",arrowTypeEnd:"none",style:"fill:none",labelStyle:"",curve:x(te.curve,L)};t.setEdge(s.id,s.class,f,g)}))}),"addNotes"),ae=u((function(e,t){const n=y().flowchart;let i=0;e.forEach((function(e){var r;i++;const a={classes:"relation",pattern:1==e.relation.lineType?"dashed":"solid",id:N(e.id1,e.id2,{prefix:"id",counter:i}),arrowhead:"arrow_open"===e.type?"none":"normal",startLabelRight:"none"===e.relationTitle1?"":e.relationTitle1,endLabelLeft:"none"===e.relationTitle2?"":e.relationTitle2,arrowTypeStart:de(e.relation.type1),arrowTypeEnd:de(e.relation.type2),style:"fill:none",labelStyle:"",curve:x(null==n?void 0:n.curve,L)};if(w.info(a,e),void 0!==e.style){const t=m(e.style);a.style=t.style,a.labelStyle=t.labelStyle}e.text=e.title,void 0===e.text?void 0!==e.style&&(a.arrowheadStyle="fill: #333"):(a.arrowheadStyle="fill: #333",a.labelpos="c",(null==(r=y().flowchart)?void 0:r.htmlLabels)??y().htmlLabels?(a.labelType="html",a.label='<span class="edgeLabel">'+e.text+"</span>"):(a.labelType="text",a.label=e.text.replace(E.lineBreakRegex,"\n"),void 0===e.style&&(a.style=a.style||"stroke: #333; stroke-width: 1.5px;fill:none"),a.labelStyle=a.labelStyle.replace("color:","fill:"))),t.setEdge(e.id1,e.id2,a,i)}))}),"addRelations"),oe=u((function(e){te={...te,...e}}),"setConf"),se=u((async function(e,t,n,i){w.info("Drawing class - ",t);const r=y().flowchart??y().class,a=y().securityLevel;w.info("config:",r);const o=(null==r?void 0:r.nodeSpacing)??50,s=(null==r?void 0:r.rankSpacing)??50,d=new X({multigraph:!0,compound:!0}).setGraph({rankdir:i.db.getDirection(),nodesep:o,ranksep:s,marginx:8,marginy:8}).setDefaultEdgeLabel((function(){return{}})),l=i.db.getNamespaces(),c=i.db.getClasses(),h=i.db.getRelations(),g=i.db.getNotes();let f;w.info(h),ne(l,d,t,i),ie(c,d,t,i),ae(h,d),re(g,d,h.length+1,c),"sandbox"===a&&(f=k("#i"+t));const p=k("sandbox"===a?f.nodes()[0].contentDocument.body:"body"),u=p.select(`[id="${t}"]`),m=p.select("#"+t+" g");if(await Z(m,d,["aggregation","extension","composition","dependency","lollipop"],"classDiagram",t),b.insertTitle(u,"classTitleText",(null==r?void 0:r.titleTopMargin)??5,i.db.getDiagramTitle()),v(d,u,null==r?void 0:r.diagramPadding,null==r?void 0:r.useMaxWidth),!(null==r?void 0:r.htmlLabels)){const e="sandbox"===a?f.nodes()[0].contentDocument:document,n=e.querySelectorAll('[id="'+t+'"] .edgeLabel .label');for(const t of n){const n=t.getBBox(),i=e.createElementNS("http://www.w3.org/2000/svg","rect");i.setAttribute("rx",0),i.setAttribute("ry",0),i.setAttribute("width",n.width),i.setAttribute("height",n.height),t.insertBefore(i,t.firstChild)}}}),"draw");function de(e){let t;switch(e){case 0:t="aggregation";break;case 1:t="extension";break;case 2:t="composition";break;case 3:t="dependency";break;case 4:t="lollipop";break;default:t="none"}return t}u(de,"getArrowMarker");var le={parser:g,db:f,renderer:{setConf:oe,draw:se},styles:p,init:u((e=>{e.class||(e.class={}),e.class.arrowMarkerAbsolute=e.arrowMarkerAbsolute,f.clear()}),"init")};export{le as diagram};
