!function(n){var r,e,i=n.parent,t="?nof"===window.location.search||/_escaped_fragment_/.test(window.location.search),a={getMetaTags:function(){for(var e,t=document.getElementsByTagName("meta"),n={},r=0;r<t.length;r++)(e=t[r].getAttribute("name"))&&(n[e]?("string"!=typeof n[e]&&"number"!=typeof n[e]||(n[e]=[n[e]]),n[e].push(t[r].getAttribute("content"))):n[e]=t[r].getAttribute("content"));return n},getScript:function(e){var t=document.getElementsByTagName("head")[0],n=document.createElement("script");n.src=e,t.appendChild(n)},inferClientFrameworkPath:function(){for(var e,t=document.getElementsByTagName("script"),n="",r=0;r<t.length;r++)if((e=t[r].getAttribute("src"))&&/\/client\.js$/.test(e)){n=e.replace(/\/client\.js$/,"/");break}return n},isEmbeddedHelp:function(){return!!(-1!==navigator.userAgent.indexOf("AutodeskClient/2.")||window.exec&&"function"==typeof window.exec&&window.registerCallback||window.execAsync&&"function"==typeof window.execAsync&&window.registerCallback)},closest:function(e,t,n){if(a.matches(e,t))return e;if(e!==n){var r=e.parentElement||e.parentNode;if(r&&1===r.nodeType)return a.closest(e.parentNode,t,n)}return null},matches:(e=window.Element&&window.Element.prototype||function(){return!1},r=e.matches||e.msMatchesSelector||e.webkitMatchesSelector,function(e,t){return r.call(e,t)}),delegateEvent:function(n,e,r,o){function t(e){var t=a.closest(e.target,r,n);t&&(e._delegatedTarget=t,o.apply(e.target,[e]))}var i=-1!==["focus","blur"].indexOf(e);return n.addEventListener(e,t,i),t},parseURL:function(e){e=e.split("#");return{params:(/\?.+/.test(e[0])&&e[0].substring(e[0].indexOf("?")+1)||"").split("&").reduce(function(e,t){t=t.split("=");return e[t[0]]=decodeURIComponent(t[1]),e},{}),anchor:e[1]}}},o=a.getMetaTags();if(i&&i!==n.self&&(i.UIComponent||i.AthenaCore)){var c=i.Boot,d=i.Resources||i.AthenaCore.Resources,u=i.UIComponent||i.AthenaCore.UIComponent,l=document.title,s=!1,p=function(){var e,t;s||(s=!0,document.body.setAttribute("data-ui-theme",c.Config.theme),a.delegateEvent(document.body,"click",'[href*=".autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook"]',function(e){e.preventDefault();var t=e._delegatedTarget.getAttribute("href"),t=a.parseURL(t);c.App.handleRoute("guid",t.params.guid,{p:t.params.p,v:t.params.v,l:t.params.l,hash:t.anchor||t.params.anchor||e._delegatedTarget.getAttribute("anchor"),pushEntry:!0})}),a.delegateEvent(document.body,"click","a, area",function(e){var t=e._delegatedTarget,n=(t.getAttribute("href")||"").trim(),e=e.currentTarget.href||n;"_blank"===t.getAttribute("target")?c.App.trigger("logADPEvent","emb_link_click",e,{u:window.location.href,lt:"external"}):a.closest(t,".relinfo")?c.App.trigger("logADPEvent","emb_link_click",e,{u:window.location.href,lt:"related"}):c.App.trigger("logADPEvent","emb_link_click",e,{u:window.location.href,lt:"content"})}),c.App.setArticle({type:"guid",title:l,id:o.topicid,p:o.product,v:o.release,source:"CloudHelp",url:window.location.href,sourceUrl:window.location.href,appliesTo:o["applies-to"],indexterm:o.indexterm&&(Array.isArray(o.indexterm)?o.indexterm:[o.indexterm]),cid:Array.isArray(o.contextid)?o.contextid[0]:o.contextid,cmp:Array.isArray(o.component)?o.component[0]:o.component,productFeature:Array.isArray(o["product-feature"])?o["product-feature"][0]:o["product-feature"],metadata:o}),document.documentElement.setAttribute("lang",c.Config.isoLanguageCode),e="true"===o["disable-sharing"]||"true"===o["commenting-override"],c.Config.WTAH&&!e&&d.getAllCSS(["dh_helpful"],document).then(function(){var e=document.createElement("div");e.classList.add("was-this-helpful"),document.body.appendChild(e),c.App.ADPAnalytics.helpful(e,{data:{u:window.location.href,t:l,p:o.product,r:o.release,l:o.language,cmp:Array.isArray(o.component)?o.component[0]:o.component,mt:"true"===o.mtc?"yes":"no",cm_product_feature:Array.isArray(o["product-feature"])?o["product-feature"][0]:o["product-feature"]}})}),setTimeout(function(){var t,e=document.body.querySelectorAll("video[data-video-id]");e.length&&i.AKPVideoPlayerHelper&&(d.getCSS(c.Config.akpVideoPlayerCSSPath,document),t={appId:c.Config.AKNAnalyticsAppId,server:c.Config.ADPAnalyticsProvider,env:c.Config.environment,ADPData:{apiKey:c.Config.AKNAnalyticsApiKey,signWith:c.Config.AKNAnalyticsSignWith},allowTracking:c.App._allowTracking,data:{u:window.location.href,t:l,p:o.product||c.Config.meta.product,r:o.release||c.Config.meta.release,l:o.language||c.Config.meta.language,am:c.Config.accessmode||void 0,s:"CloudHelp",mt:"true"===o.mtc?"yes":"no",cmp:Array.isArray(o.component)?o.component[0]:o.component,guid:o.topicId,cm_product_feature:Array.isArray(o["product-feature"])?o["product-feature"][0]:o["product-feature"]}},Array.prototype.forEach.call(e,function(e){i.AKPVideoPlayerHelper.init(e,t)}))},0),e=d.getAllScripts(["content/Sharing"]),t=d.getAllCSS(["Dropdown","Sharing"],document),(n.Promise?n.Promise.all([e,t]):e.then(function(){return t})).then(function(){u.create("Sharing",{ready:function(){var e,t,n,r={insertBefore:".head > .version-info, div.head h1",prependTo:".head-text",insertAfter:".caas_body > h1:first-child"};for(n in r)if(r.hasOwnProperty(n)&&(e=document.body.querySelector(r[n]))){t=n;break}var o=this.element instanceof i.Element?this.element:this.element[0];switch(t){case"insertBefore":e.parentNode.insertBefore(o,e);break;case"prependTo":e.insertBefore(o,e.firstChild);break;case"insertAfter":e.parentNode.insertBefore(o,e.nextSibling)}},sharingOptions:{href:window.location.href,title:document.title,targetDocument:window.document}})}),i.DHAnalytics&&i.DHAnalytics.plugins.pageviews.create(document.body,{data:{u:window.location.href,t:l,p:o.product||c.Config.meta.product,r:o.release||c.Config.meta.release,l:o.language||c.Config.meta.language,am:c.Config.accessmode||void 0,s:"CloudHelp",mt:"true"===o.mtc?"yes":"no",cmp:Array.isArray(o.component)?o.component[0]:o.component,guid:o.topicId,cm_product_feature:Array.isArray(o["product-feature"])?o["product-feature"][0]:o["product-feature"]}}))};document.addEventListener?document.addEventListener("DOMContentLoaded",p,!1):function e(){document.body?p():setTimeout(e,50)}(),n.help=i.help}else if(n.self===n.top&&!t&&o.helpsystempath)return e=o.helpsystempath.replace(/^https?:\/\//,"//")+(o.topicid?"?guid="+o.topicid:"")+("#"!==window.location.hash?window.location.hash:""),t={},window.JSON&&(t[e]={l:o.language,url:window.location.href},window.name=JSON.stringify(t)),void window.location.replace(e);a.isEmbeddedHelp()?(document.documentElement.className+=" embedded",document.addEventListener&&document.addEventListener("helpuifinder:click",function(e){i.document.dispatchEvent(new CustomEvent("helpuifinder:click",e))},!1),"2015"===o.release?a.getScript(a.inferClientFrameworkPath()+"uifinder/helpuifinder-2015.js"):window.exec&&a.getScript(a.inferClientFrameworkPath()+"uifinder/helpuifinder.js")):(document.documentElement.className+=" browser",document.querySelectorAll&&document.addEventListener&&document.addEventListener("DOMContentLoaded",function(){for(var e=document.querySelectorAll(".uifinderbtn[title]"),t=0;t<e.length;t++)e[t].removeAttribute("title")},!1)),n.OO={VIDEOS_BASE_PATH:"https://help.autodesk.com/videos/",Player:{create:function(e,t){var n=OO.createVideoTag(OO.VIDEOS_BASE_PATH+t),e=document.getElementById(e);n.setAttribute("data-video-id",t),e.appendChild(n)}},ready:function(e){document.addEventListener("DOMContentLoaded",function(){e()},!1)},createVideoTag:function(e){var t=document.createElement("video");return t.setAttribute("controls",""),t.setAttribute("crossorigin","anonymous"),t.setAttribute("poster",e+"/poster"),OO.addVideoSource(t,"video/webm",e+"/video.webm"),OO.addVideoSource(t,"video/mp4",e+"/video.mp4"),t},addVideoSource:function(e,t,n){var r=document.createElement("source");r.setAttribute("type",t),r.setAttribute("src",n),e.appendChild(r)}},n.initFrame=function(e,t,n,r){},n.initPage=function(e,t){},n.convSymbols=function(){},n.hideInfo=function(){var e=document.getElementById("infoline");e.innerHTML=" ",e.style.visibility="hidden"},n.showInfo=function(e){var t=document.getElementById("infoline");t.innerHTML=e,t.style.visibility="visible"}}.call(window,window);