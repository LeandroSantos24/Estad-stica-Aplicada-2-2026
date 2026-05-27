var transferWindowWidget=(function(){"use strict";var va=Object.defineProperty;var ci=E=>{throw TypeError(E)};var ma=(E,T,D)=>T in E?va(E,T,{enumerable:!0,configurable:!0,writable:!0,value:D}):E[T]=D;var W=(E,T,D)=>ma(E,typeof T!="symbol"?T+"":T,D),Fn=(E,T,D)=>T.has(E)||ci("Cannot "+D);var c=(E,T,D)=>(Fn(E,T,"read from private field"),D?D.call(E):T.get(E)),x=(E,T,D)=>T.has(E)?ci("Cannot add the same private member more than once"):T instanceof WeakSet?T.add(E):T.set(E,D),p=(E,T,D,Xt)=>(Fn(E,T,"write to private field"),Xt?Xt.call(E,D):T.set(E,D),D),U=(E,T,D)=>(Fn(E,T,"access private method"),D);var ui,$t,xt,Fe,qt,St,Et,nt,Tt,Yt,Gt,se,Mn,yn,Bn,ue,te,Jt,be,rt,$e,ae,X,xe,Me,it,Be,st,We,wn,_n,F,di,hi,gn,bn,Wn,Pe,oe;typeof window<"u"&&((ui=window.__svelte??(window.__svelte={})).v??(ui.v=new Set)).add("5");const T=1,D=2,Xt=4,vi=8,mi=16,pi=1,wi=2,Hn="[",$n="[!",Vn="]",ht={},z=Symbol(),_i="http://www.w3.org/2000/svg",qn=!1;var Yn=Array.isArray,yi=Array.prototype.indexOf,gi=Array.from,Zt=Object.keys,vt=Object.defineProperty,He=Object.getOwnPropertyDescriptor,bi=Object.prototype,$i=Array.prototype,xi=Object.getPrototypeOf,Gn=Object.isExtensible;const Si=()=>{};function Ei(e){for(var t=0;t<e.length;t++)e[t]()}function Jn(){var e,t,n=new Promise((r,i)=>{e=r,t=i});return{promise:n,resolve:e,reject:t}}const K=2,xn=4,Sn=8,Ve=16,Ee=32,Ce=64,En=128,ne=256,en=512,M=1024,Z=2048,De=4096,Ie=8192,qe=16384,Tn=32768,Ot=65536,Kn=1<<17,Ti=1<<18,Ye=1<<19,Ri=1<<20,Rn=1<<21,tn=1<<22,Ge=1<<23,Pt=Symbol("$state"),Qn=Symbol("legacy props"),At=new class extends Error{constructor(){super(...arguments);W(this,"name","StaleReactionError");W(this,"message","The reaction that called `getAbortSignal()` was re-run or destroyed")}},ki=1,nn=3,jt=8;function Oi(e){throw new Error("https://svelte.dev/e/lifecycle_outside_component")}function Pi(){throw new Error("https://svelte.dev/e/async_derived_orphan")}function Ai(e){throw new Error("https://svelte.dev/e/effect_in_teardown")}function ji(){throw new Error("https://svelte.dev/e/effect_in_unowned_derived")}function Ci(e){throw new Error("https://svelte.dev/e/effect_orphan")}function Di(){throw new Error("https://svelte.dev/e/effect_update_depth_exceeded")}function Ii(){throw new Error("https://svelte.dev/e/hydration_failed")}function Ni(e){throw new Error("https://svelte.dev/e/props_invalid_value")}function Ui(){throw new Error("https://svelte.dev/e/state_descriptors_fixed")}function zi(){throw new Error("https://svelte.dev/e/state_prototype_fixed")}function Li(){throw new Error("https://svelte.dev/e/state_unsafe_mutation")}function Fi(){throw new Error("https://svelte.dev/e/svelte_boundary_reset_onerror")}function rn(e){console.warn("https://svelte.dev/e/hydration_mismatch")}function Mi(){console.warn("https://svelte.dev/e/svelte_boundary_reset_noop")}let g=!1;function de(e){g=e}let b;function H(e){if(e===null)throw rn(),ht;return b=e}function Ct(){return H(ke(b))}function V(e){if(g){if(ke(b)!==null)throw rn(),ht;b=e}}function Xn(e=1){if(g){for(var t=e,n=b;t--;)n=ke(n);b=n}}function Zn(e=!0){for(var t=0,n=b;;){if(n.nodeType===jt){var r=n.data;if(r===Vn){if(t===0)return n;t-=1}else(r===Hn||r===$n)&&(t+=1)}var i=ke(n);e&&n.remove(),n=i}}function Bi(e){if(!e||e.nodeType!==jt)throw rn(),ht;return e.data}function er(e){return e===this.v}function Wi(e,t){return e!=e?t==t:e!==t||e!==null&&typeof e=="object"||typeof e=="function"}function tr(e){return!Wi(e,this.v)}let mt=!1,Hi=!1;function Vi(){mt=!0}let P=null;function pt(e){P=e}function Dt(e,t=!1,n){P={p:P,c:null,e:null,s:e,x:null,l:mt&&!t?{s:null,u:null,$:[]}:null}}function It(e){var t=P,n=t.e;if(n!==null){t.e=null;for(var r of n)gr(r)}return e!==void 0&&(t.x=e),P=t.p,e??{}}function Nt(){return!mt||P!==null&&P.l===null}let Je=[];function nr(){var e=Je;Je=[],Ei(e)}function Ut(e){if(Je.length===0&&!zt){var t=Je;queueMicrotask(()=>{t===Je&&nr()})}Je.push(e)}function qi(){for(;Je.length>0;)nr()}const Yi=new WeakMap;function rr(e){var t=y;if(t===null)return _.f|=Ge,e;if((t.f&Tn)===0){if((t.f&En)===0)throw!t.parent&&e instanceof Error&&ir(e),e;t.b.error(e)}else wt(e,t)}function wt(e,t){for(;t!==null;){if((t.f&En)!==0)try{t.b.error(e);return}catch(n){e=n}t=t.parent}throw e instanceof Error&&ir(e),e}function ir(e){const t=Yi.get(e);t&&(vt(e,"message",{value:t.message}),vt(e,"stack",{value:t.stack}))}const sn=new Set;let A=null,kn=new Set,he=[],an=null,On=!1,zt=!1;const Rt=class Rt{constructor(){x(this,se);W(this,"current",new Map);x(this,$t,new Map);x(this,xt,new Set);x(this,Fe,0);x(this,qt,null);x(this,St,[]);x(this,Et,[]);x(this,nt,[]);x(this,Tt,[]);x(this,Yt,[]);x(this,Gt,[]);W(this,"skipped_effects",new Set)}process(t){var s;he=[];var n=Rt.apply(this);for(const a of t)U(this,se,Mn).call(this,a);if(c(this,Fe)===0){U(this,se,Bn).call(this);var r=c(this,Et),i=c(this,nt);p(this,Et,[]),p(this,nt,[]),p(this,Tt,[]),A=null,ar(r),ar(i),(s=c(this,qt))==null||s.resolve()}else U(this,se,yn).call(this,c(this,Et)),U(this,se,yn).call(this,c(this,nt)),U(this,se,yn).call(this,c(this,Tt));n();for(const a of c(this,St))Wt(a);p(this,St,[])}capture(t,n){c(this,$t).has(t)||c(this,$t).set(t,n),this.current.set(t,t.v)}activate(){A=this}deactivate(){A=null;for(const t of kn)if(kn.delete(t),t(),A!==null)break}flush(){if(he.length>0){if(this.activate(),sr(),A!==null&&A!==this)return}else c(this,Fe)===0&&U(this,se,Bn).call(this);this.deactivate()}increment(){p(this,Fe,c(this,Fe)+1)}decrement(){if(p(this,Fe,c(this,Fe)-1),c(this,Fe)===0){for(const t of c(this,Yt))J(t,Z),Ke(t);for(const t of c(this,Gt))J(t,De),Ke(t);this.flush()}else this.deactivate()}add_callback(t){c(this,xt).add(t)}settled(){return(c(this,qt)??p(this,qt,Jn())).promise}static ensure(){if(A===null){const t=A=new Rt;sn.add(A),zt||Rt.enqueue(()=>{A===t&&t.flush()})}return A}static enqueue(t){Ut(t)}static apply(t){return Si}};$t=new WeakMap,xt=new WeakMap,Fe=new WeakMap,qt=new WeakMap,St=new WeakMap,Et=new WeakMap,nt=new WeakMap,Tt=new WeakMap,Yt=new WeakMap,Gt=new WeakMap,se=new WeakSet,Mn=function(t){var f;t.f^=M;for(var n=t.first;n!==null;){var r=n.f,i=(r&(Ee|Ce))!==0,s=i&&(r&M)!==0,a=s||(r&Ie)!==0||this.skipped_effects.has(n);if(!a&&n.fn!==null){i?n.f^=M:(r&xn)!==0?c(this,nt).push(n):(r&M)===0&&((r&tn)!==0&&((f=n.b)!=null&&f.is_pending())?c(this,St).push(n):fn(n)&&((n.f&Ve)!==0&&c(this,Tt).push(n),Wt(n)));var o=n.first;if(o!==null){n=o;continue}}var l=n.parent;for(n=n.next;n===null&&l!==null;)n=l.next,l=l.parent}},yn=function(t){for(const n of t)((n.f&Z)!==0?c(this,Yt):c(this,Gt)).push(n),J(n,M);t.length=0},Bn=function(){var t;for(const n of c(this,xt))n();if(c(this,xt).clear(),sn.size>1){c(this,$t).clear();let n=!0;for(const r of sn){if(r===this){n=!1;continue}for(const[i,s]of this.current){if(r.current.has(i))if(n)r.current.set(i,s);else continue;or(i)}if(he.length>0){A=r;const i=Rt.apply(r);for(const s of he)U(t=r,se,Mn).call(t,s);he=[],i()}}A=null}sn.delete(this)};let ve=Rt;function Te(e){var t=zt;zt=!0;try{for(var n;;){if(qi(),he.length===0&&(A==null||A.flush(),he.length===0))return an=null,n;sr()}}finally{zt=t}}function sr(){var e=yt;On=!0;try{var t=0;for(kr(!0);he.length>0;){var n=ve.ensure();if(t++>1e3){var r,i;Gi()}n.process(he),Ne.clear()}}finally{On=!1,kr(e),an=null}}function Gi(){try{Di()}catch(e){wt(e,an)}}let Re=null;function ar(e){var t=e.length;if(t!==0){for(var n=0;n<t;){var r=e[n++];if((r.f&(qe|Ie))===0&&fn(r)&&(Re=[],Wt(r),r.deps===null&&r.first===null&&r.nodes_start===null&&(r.teardown===null&&r.ac===null?Sr(r):r.fn=null),(Re==null?void 0:Re.length)>0)){Ne.clear();for(const i of Re)Wt(i);Re=[]}}Re=null}}function or(e){if(e.reactions!==null)for(const t of e.reactions){const n=t.f;(n&K)!==0?or(t):(n&(tn|Ve))!==0&&(J(t,Z),Ke(t))}}function Ke(e){for(var t=an=e;t.parent!==null;){t=t.parent;var n=t.f;if(On&&t===y&&(n&Ve)!==0)return;if((n&(Ce|Ee))!==0){if((n&M)===0)return;t.f^=M}}he.push(t)}function Ji(e){let t=0,n=Lt(0),r;return()=>{us()&&($(n),jn(()=>(t===0&&(r=cn(()=>e(()=>Ft(n)))),t+=1,()=>{Ut(()=>{t-=1,t===0&&(r==null||r(),r=void 0,Ft(n))})})))}}var Ki=Ot|Ye|En;function Qi(e,t,n){new Xi(e,t,n)}class Xi{constructor(t,n,r){x(this,F);W(this,"parent");x(this,ue,!1);x(this,te);x(this,Jt,g?b:null);x(this,be);x(this,rt);x(this,$e);x(this,ae,null);x(this,X,null);x(this,xe,null);x(this,Me,null);x(this,it,0);x(this,Be,0);x(this,st,!1);x(this,We,null);x(this,wn,()=>{c(this,We)&&ln(c(this,We),c(this,it))});x(this,_n,Ji(()=>(p(this,We,Lt(c(this,it))),()=>{p(this,We,null)})));p(this,te,t),p(this,be,n),p(this,rt,r),this.parent=y.b,p(this,ue,!!c(this,be).pending),p(this,$e,Cn(()=>{if(y.b=this,g){const i=c(this,Jt);Ct(),i.nodeType===jt&&i.data===$n?U(this,F,hi).call(this):U(this,F,di).call(this)}else{try{p(this,ae,_e(()=>r(c(this,te))))}catch(i){this.error(i)}c(this,Be)>0?U(this,F,bn).call(this):p(this,ue,!1)}},Ki)),g&&p(this,te,b)}is_pending(){return c(this,ue)||!!this.parent&&this.parent.is_pending()}has_pending_snippet(){return!!c(this,be).pending}update_pending_count(t){U(this,F,Wn).call(this,t),p(this,it,c(this,it)+t),kn.add(c(this,wn))}get_effect_pending(){return c(this,_n).call(this),$(c(this,We))}error(t){var n=c(this,be).onerror;let r=c(this,be).failed;if(c(this,st)||!n&&!r)throw t;c(this,ae)&&(re(c(this,ae)),p(this,ae,null)),c(this,X)&&(re(c(this,X)),p(this,X,null)),c(this,xe)&&(re(c(this,xe)),p(this,xe,null)),g&&(H(c(this,Jt)),Xn(),H(Zn()));var i=!1,s=!1;const a=()=>{if(i){Mi();return}i=!0,s&&Fi(),ve.ensure(),p(this,it,0),c(this,xe)!==null&&_t(c(this,xe),()=>{p(this,xe,null)}),p(this,ue,this.has_pending_snippet()),p(this,ae,U(this,F,gn).call(this,()=>(p(this,st,!1),_e(()=>c(this,rt).call(this,c(this,te)))))),c(this,Be)>0?U(this,F,bn).call(this):p(this,ue,!1)};var o=_;try{Q(null),s=!0,n==null||n(t,a),s=!1}catch(l){wt(l,c(this,$e)&&c(this,$e).parent)}finally{Q(o)}r&&Ut(()=>{p(this,xe,U(this,F,gn).call(this,()=>{p(this,st,!0);try{return _e(()=>{r(c(this,te),()=>t,()=>a)})}catch(l){return wt(l,c(this,$e).parent),null}finally{p(this,st,!1)}}))})}}ue=new WeakMap,te=new WeakMap,Jt=new WeakMap,be=new WeakMap,rt=new WeakMap,$e=new WeakMap,ae=new WeakMap,X=new WeakMap,xe=new WeakMap,Me=new WeakMap,it=new WeakMap,Be=new WeakMap,st=new WeakMap,We=new WeakMap,wn=new WeakMap,_n=new WeakMap,F=new WeakSet,di=function(){try{p(this,ae,_e(()=>c(this,rt).call(this,c(this,te))))}catch(t){this.error(t)}p(this,ue,!1)},hi=function(){const t=c(this,be).pending;t&&(p(this,X,_e(()=>t(c(this,te)))),ve.enqueue(()=>{p(this,ae,U(this,F,gn).call(this,()=>(ve.ensure(),_e(()=>c(this,rt).call(this,c(this,te)))))),c(this,Be)>0?U(this,F,bn).call(this):(_t(c(this,X),()=>{p(this,X,null)}),p(this,ue,!1))}))},gn=function(t){var n=y,r=_,i=P;ye(c(this,$e)),Q(c(this,$e)),pt(c(this,$e).ctx);try{return t()}catch(s){return rr(s),null}finally{ye(n),Q(r),pt(i)}},bn=function(){const t=c(this,be).pending;c(this,ae)!==null&&(p(this,Me,document.createDocumentFragment()),Zi(c(this,ae),c(this,Me))),c(this,X)===null&&p(this,X,_e(()=>t(c(this,te))))},Wn=function(t){var n;if(!this.has_pending_snippet()){this.parent&&U(n=this.parent,F,Wn).call(n,t);return}p(this,Be,c(this,Be)+t),c(this,Be)===0&&(p(this,ue,!1),c(this,X)&&_t(c(this,X),()=>{p(this,X,null)}),c(this,Me)&&(c(this,te).before(c(this,Me)),p(this,Me,null)),Ut(()=>{ve.ensure().flush()}))};function Zi(e,t){for(var n=e.nodes_start,r=e.nodes_end;n!==null;){var i=n===r?null:ke(n);t.append(n),n=i}}function es(e,t,n){const r=Nt()?on:fr;if(t.length===0){n(e.map(r));return}var i=A,s=y,a=ts(),o=g;Promise.all(t.map(l=>ns(l))).then(l=>{i==null||i.activate(),a();try{n([...e.map(r),...l])}catch(f){(s.f&qe)===0&&wt(f,s)}o&&de(!1),i==null||i.deactivate(),lr()}).catch(l=>{wt(l,s)})}function ts(){var e=y,t=_,n=P,r=A,i=g;if(i)var s=b;return function(){ye(e),Q(t),pt(n),r==null||r.activate(),i&&(de(!0),H(s))}}function lr(){ye(null),Q(null),pt(null)}function on(e){var t=K|Z,n=_!==null&&(_.f&K)!==0?_:null;return y===null||n!==null&&(n.f&ne)!==0?t|=ne:y.f|=Ye,{ctx:P,deps:null,effects:null,equals:er,f:t,fn:e,reactions:null,rv:0,v:z,wv:0,parent:n??y,ac:null}}function ns(e,t){let n=y;n===null&&Pi();var r=n.b,i=void 0,s=Lt(z),a=!_,o=new Map;return vs(()=>{var u;var l=Jn();i=l.promise;try{Promise.resolve(e()).then(l.resolve,l.reject)}catch(v){l.reject(v)}var f=A,h=r.is_pending();a&&(r.update_pending_count(1),h||(f.increment(),(u=o.get(f))==null||u.reject(At),o.set(f,l)));const d=(v,m=void 0)=>{h||f.activate(),m?m!==At&&(s.f|=Ge,ln(s,m)):((s.f&Ge)!==0&&(s.f^=Ge),ln(s,v)),a&&(r.update_pending_count(-1),h||f.decrement()),lr()};l.promise.then(d,v=>d(null,v||"unknown"))}),cs(()=>{for(const l of o.values())l.reject(At)}),new Promise(l=>{function f(h){function d(){h===i?l(s):f(i)}h.then(d,d)}f(i)})}function rs(e){const t=on(e);return Pr(t),t}function fr(e){const t=on(e);return t.equals=tr,t}function ur(e){var t=e.effects;if(t!==null){e.effects=null;for(var n=0;n<t.length;n+=1)re(t[n])}}function is(e){for(var t=e.parent;t!==null;){if((t.f&K)===0)return t;t=t.parent}return null}function Pn(e){var t,n=y;ye(is(e));try{ur(e),t=Ir(e)}finally{ye(n)}return t}function cr(e){var t=Pn(e);if(e.equals(t)||(e.v=t,e.wv=Cr()),!Xe){var n=(ze||(e.f&ne)!==0)&&e.deps!==null?De:M;J(e,n)}}const Ne=new Map;function Lt(e,t){var n={f:0,v:e,reactions:null,equals:er,rv:0,wv:0};return n}function L(e,t){const n=Lt(e);return Pr(n),n}function ss(e,t=!1,n=!0){var i;const r=Lt(e);return t||(r.equals=tr),mt&&n&&P!==null&&P.l!==null&&((i=P.l).s??(i.s=[])).push(r),r}function j(e,t,n=!1){_!==null&&(!fe||(_.f&Kn)!==0)&&Nt()&&(_.f&(K|Ve|tn|Kn))!==0&&!(Y!=null&&Y.includes(e))&&Li();let r=n?Ue(t):t;return ln(e,r)}function ln(e,t){if(!e.equals(t)){var n=e.v;Xe?Ne.set(e,t):Ne.set(e,n),e.v=t;var r=ve.ensure();r.capture(e,n),(e.f&K)!==0&&((e.f&Z)!==0&&Pn(e),J(e,(e.f&ne)===0?M:De)),e.wv=Cr(),dr(e,Z),Nt()&&y!==null&&(y.f&M)!==0&&(y.f&(Ee|Ce))===0&&(ie===null?_s([e]):ie.push(e))}return t}function Ft(e){j(e,e.v+1)}function dr(e,t){var n=e.reactions;if(n!==null)for(var r=Nt(),i=n.length,s=0;s<i;s++){var a=n[s],o=a.f;if(!(!r&&a===y)){var l=(o&Z)===0;l&&J(a,t),(o&K)!==0?dr(a,De):l&&((o&Ve)!==0&&Re!==null&&Re.push(a),Ke(a))}}}function Ue(e){if(typeof e!="object"||e===null||Pt in e)return e;const t=xi(e);if(t!==bi&&t!==$i)return e;var n=new Map,r=Yn(e),i=L(0),s=Ze,a=o=>{if(Ze===s)return o();var l=_,f=Ze;Q(null),jr(s);var h=o();return Q(l),jr(f),h};return r&&n.set("length",L(e.length)),new Proxy(e,{defineProperty(o,l,f){(!("value"in f)||f.configurable===!1||f.enumerable===!1||f.writable===!1)&&Ui();var h=n.get(l);return h===void 0?h=a(()=>{var d=L(f.value);return n.set(l,d),d}):j(h,f.value,!0),!0},deleteProperty(o,l){var f=n.get(l);if(f===void 0){if(l in o){const h=a(()=>L(z));n.set(l,h),Ft(i)}}else j(f,z),Ft(i);return!0},get(o,l,f){var v;if(l===Pt)return e;var h=n.get(l),d=l in o;if(h===void 0&&(!d||(v=He(o,l))!=null&&v.writable)&&(h=a(()=>{var m=Ue(d?o[l]:z),S=L(m);return S}),n.set(l,h)),h!==void 0){var u=$(h);return u===z?void 0:u}return Reflect.get(o,l,f)},getOwnPropertyDescriptor(o,l){var f=Reflect.getOwnPropertyDescriptor(o,l);if(f&&"value"in f){var h=n.get(l);h&&(f.value=$(h))}else if(f===void 0){var d=n.get(l),u=d==null?void 0:d.v;if(d!==void 0&&u!==z)return{enumerable:!0,configurable:!0,value:u,writable:!0}}return f},has(o,l){var u;if(l===Pt)return!0;var f=n.get(l),h=f!==void 0&&f.v!==z||Reflect.has(o,l);if(f!==void 0||y!==null&&(!h||(u=He(o,l))!=null&&u.writable)){f===void 0&&(f=a(()=>{var v=h?Ue(o[l]):z,m=L(v);return m}),n.set(l,f));var d=$(f);if(d===z)return!1}return h},set(o,l,f,h){var C;var d=n.get(l),u=l in o;if(r&&l==="length")for(var v=f;v<d.v;v+=1){var m=n.get(v+"");m!==void 0?j(m,z):v in o&&(m=a(()=>L(z)),n.set(v+"",m))}if(d===void 0)(!u||(C=He(o,l))!=null&&C.writable)&&(d=a(()=>L(void 0)),j(d,Ue(f)),n.set(l,d));else{u=d.v!==z;var S=a(()=>Ue(f));j(d,S)}var R=Reflect.getOwnPropertyDescriptor(o,l);if(R!=null&&R.set&&R.set.call(h,f),!u){if(r&&typeof l=="string"){var k=n.get("length"),I=Number(l);Number.isInteger(I)&&I>=k.v&&j(k,I+1)}Ft(i)}return!0},ownKeys(o){$(i);var l=Reflect.ownKeys(o).filter(d=>{var u=n.get(d);return u===void 0||u.v!==z});for(var[f,h]of n)h.v!==z&&!(f in o)&&l.push(f);return l},setPrototypeOf(){zi()}})}var hr,vr,mr,pr;function An(){if(hr===void 0){hr=window,vr=/Firefox/.test(navigator.userAgent);var e=Element.prototype,t=Node.prototype,n=Text.prototype;mr=He(t,"firstChild").get,pr=He(t,"nextSibling").get,Gn(e)&&(e.__click=void 0,e.__className=void 0,e.__attributes=null,e.__style=void 0,e.__e=void 0),Gn(n)&&(n.__t=void 0)}}function me(e=""){return document.createTextNode(e)}function Qe(e){return mr.call(e)}function ke(e){return pr.call(e)}function q(e,t){if(!g)return Qe(e);var n=Qe(b);if(n===null)n=b.appendChild(me());else if(t&&n.nodeType!==nn){var r=me();return n==null||n.before(r),H(r),r}return H(n),n}function wr(e,t=!1){if(!g){var n=Qe(e);return n instanceof Comment&&n.data===""?ke(n):n}if(t&&(b==null?void 0:b.nodeType)!==nn){var r=me();return b==null||b.before(r),H(r),r}return b}function pe(e,t=1,n=!1){let r=g?b:e;for(var i;t--;)i=r,r=ke(r);if(!g)return r;if(n&&(r==null?void 0:r.nodeType)!==nn){var s=me();return r===null?i==null||i.after(s):r.before(s),H(s),s}return H(r),r}function as(e){e.textContent=""}function os(){return!1}function _r(e){var t=_,n=y;Q(null),ye(null);try{return e()}finally{Q(t),ye(n)}}function ls(e){y===null&&_===null&&Ci(),_!==null&&(_.f&ne)!==0&&y===null&&ji(),Xe&&Ai()}function fs(e,t){var n=t.last;n===null?t.last=t.first=e:(n.next=e,e.prev=n,t.last=e)}function we(e,t,n,r=!0){var i=y;i!==null&&(i.f&Ie)!==0&&(e|=Ie);var s={ctx:P,deps:null,nodes_start:null,nodes_end:null,f:e|Z,first:null,fn:t,last:null,next:null,parent:i,b:i&&i.b,prev:null,teardown:null,transitions:null,wv:0,ac:null};if(n)try{Wt(s),s.f|=Tn}catch(l){throw re(s),l}else t!==null&&Ke(s);if(r){var a=s;if(n&&a.deps===null&&a.teardown===null&&a.nodes_start===null&&a.first===a.last&&(a.f&Ye)===0&&(a=a.first),a!==null&&(a.parent=i,i!==null&&fs(a,i),_!==null&&(_.f&K)!==0&&(e&Ce)===0)){var o=_;(o.effects??(o.effects=[])).push(a)}}return s}function us(){return _!==null&&!fe}function cs(e){const t=we(Sn,null,!1);return J(t,M),t.teardown=e,t}function yr(e){ls();var t=y.f,n=!_&&(t&Ee)!==0&&(t&Tn)===0;if(n){var r=P;(r.e??(r.e=[])).push(e)}else return gr(e)}function gr(e){return we(xn|Ri,e,!1)}function ds(e){ve.ensure();const t=we(Ce|Ye,e,!0);return()=>{re(t)}}function hs(e){ve.ensure();const t=we(Ce|Ye,e,!0);return(n={})=>new Promise(r=>{n.outro?_t(t,()=>{re(t),r(void 0)}):(re(t),r(void 0))})}function br(e){return we(xn,e,!1)}function vs(e){return we(tn|Ye,e,!0)}function jn(e,t=0){return we(Sn|t,e,!0)}function Mt(e,t=[],n=[]){es(t,n,r=>{we(Sn,()=>e(...r.map($)),!0)})}function Cn(e,t=0){var n=we(Ve|t,e,!0);return n}function _e(e,t=!0){return we(Ee|Ye,e,!0,t)}function $r(e){var t=e.teardown;if(t!==null){const n=Xe,r=_;Or(!0),Q(null);try{t.call(null)}finally{Or(n),Q(r)}}}function xr(e,t=!1){var n=e.first;for(e.first=e.last=null;n!==null;){const i=n.ac;i!==null&&_r(()=>{i.abort(At)});var r=n.next;(n.f&Ce)!==0?n.parent=null:re(n,t),n=r}}function ms(e){for(var t=e.first;t!==null;){var n=t.next;(t.f&Ee)===0&&re(t),t=n}}function re(e,t=!0){var n=!1;(t||(e.f&Ti)!==0)&&e.nodes_start!==null&&e.nodes_end!==null&&(ps(e.nodes_start,e.nodes_end),n=!0),xr(e,t&&!n),un(e,0),J(e,qe);var r=e.transitions;if(r!==null)for(const s of r)s.stop();$r(e);var i=e.parent;i!==null&&i.first!==null&&Sr(e),e.next=e.prev=e.teardown=e.ctx=e.deps=e.fn=e.nodes_start=e.nodes_end=e.ac=null}function ps(e,t){for(;e!==null;){var n=e===t?null:ke(e);e.remove(),e=n}}function Sr(e){var t=e.parent,n=e.prev,r=e.next;n!==null&&(n.next=r),r!==null&&(r.prev=n),t!==null&&(t.first===e&&(t.first=r),t.last===e&&(t.last=n))}function _t(e,t){var n=[];Er(e,n,!0),ws(n,()=>{re(e),t&&t()})}function ws(e,t){var n=e.length;if(n>0){var r=()=>--n||t();for(var i of e)i.out(r)}else t()}function Er(e,t,n){if((e.f&Ie)===0){if(e.f^=Ie,e.transitions!==null)for(const a of e.transitions)(a.is_global||n)&&t.push(a);for(var r=e.first;r!==null;){var i=r.next,s=(r.f&Ot)!==0||(r.f&Ee)!==0;Er(r,t,s?n:!1),r=i}}}function Tr(e){Rr(e,!0)}function Rr(e,t){if((e.f&Ie)!==0){e.f^=Ie,(e.f&M)===0&&(J(e,Z),Ke(e));for(var n=e.first;n!==null;){var r=n.next,i=(n.f&Ot)!==0||(n.f&Ee)!==0;Rr(n,i?t:!1),n=r}if(e.transitions!==null)for(const s of e.transitions)(s.is_global||t)&&s.in()}}let yt=!1;function kr(e){yt=e}let Xe=!1;function Or(e){Xe=e}let _=null,fe=!1;function Q(e){_=e}let y=null;function ye(e){y=e}let Y=null;function Pr(e){_!==null&&(Y===null?Y=[e]:Y.push(e))}let G=null,ee=0,ie=null;function _s(e){ie=e}let Ar=1,Bt=0,Ze=Bt;function jr(e){Ze=e}let ze=!1;function Cr(){return++Ar}function fn(e){var d;var t=e.f;if((t&Z)!==0)return!0;if((t&De)!==0){var n=e.deps,r=(t&ne)!==0;if(n!==null){var i,s,a=(t&en)!==0,o=r&&y!==null&&!ze,l=n.length;if((a||o)&&(y===null||(y.f&qe)===0)){var f=e,h=f.parent;for(i=0;i<l;i++)s=n[i],(a||!((d=s==null?void 0:s.reactions)!=null&&d.includes(f)))&&(s.reactions??(s.reactions=[])).push(f);a&&(f.f^=en),o&&h!==null&&(h.f&ne)===0&&(f.f^=ne)}for(i=0;i<l;i++)if(s=n[i],fn(s)&&cr(s),s.wv>e.wv)return!0}(!r||y!==null&&!ze)&&J(e,M)}return!1}function Dr(e,t,n=!0){var r=e.reactions;if(r!==null&&!(Y!=null&&Y.includes(e)))for(var i=0;i<r.length;i++){var s=r[i];(s.f&K)!==0?Dr(s,t,!1):t===s&&(n?J(s,Z):(s.f&M)!==0&&J(s,De),Ke(s))}}function Ir(e){var S;var t=G,n=ee,r=ie,i=_,s=ze,a=Y,o=P,l=fe,f=Ze,h=e.f;G=null,ee=0,ie=null,ze=(h&ne)!==0&&(fe||!yt||_===null),_=(h&(Ee|Ce))===0?e:null,Y=null,pt(e.ctx),fe=!1,Ze=++Bt,e.ac!==null&&(_r(()=>{e.ac.abort(At)}),e.ac=null);try{e.f|=Rn;var d=e.fn,u=d(),v=e.deps;if(G!==null){var m;if(un(e,ee),v!==null&&ee>0)for(v.length=ee+G.length,m=0;m<G.length;m++)v[ee+m]=G[m];else e.deps=v=G;if(!ze||(h&K)!==0&&e.reactions!==null)for(m=ee;m<v.length;m++)((S=v[m]).reactions??(S.reactions=[])).push(e)}else v!==null&&ee<v.length&&(un(e,ee),v.length=ee);if(Nt()&&ie!==null&&!fe&&v!==null&&(e.f&(K|De|Z))===0)for(m=0;m<ie.length;m++)Dr(ie[m],e);return i!==null&&i!==e&&(Bt++,ie!==null&&(r===null?r=ie:r.push(...ie))),(e.f&Ge)!==0&&(e.f^=Ge),u}catch(R){return rr(R)}finally{e.f^=Rn,G=t,ee=n,ie=r,_=i,ze=s,Y=a,pt(o),fe=l,Ze=f}}function ys(e,t){let n=t.reactions;if(n!==null){var r=yi.call(n,e);if(r!==-1){var i=n.length-1;i===0?n=t.reactions=null:(n[r]=n[i],n.pop())}}n===null&&(t.f&K)!==0&&(G===null||!G.includes(t))&&(J(t,De),(t.f&(ne|en))===0&&(t.f^=en),ur(t),un(t,0))}function un(e,t){var n=e.deps;if(n!==null)for(var r=t;r<n.length;r++)ys(e,n[r])}function Wt(e){var t=e.f;if((t&qe)===0){J(e,M);var n=y,r=yt;y=e,yt=!0;try{(t&Ve)!==0?ms(e):xr(e),$r(e);var i=Ir(e);e.teardown=typeof i=="function"?i:null,e.wv=Ar;var s;qn&&Hi&&(e.f&Z)!==0&&e.deps}finally{yt=r,y=n}}}function $(e){var t=e.f,n=(t&K)!==0;if(_!==null&&!fe){var r=y!==null&&(y.f&qe)!==0;if(!r&&!(Y!=null&&Y.includes(e))){var i=_.deps;if((_.f&Rn)!==0)e.rv<Bt&&(e.rv=Bt,G===null&&i!==null&&i[ee]===e?ee++:G===null?G=[e]:(!ze||!G.includes(e))&&G.push(e));else{(_.deps??(_.deps=[])).push(e);var s=e.reactions;s===null?e.reactions=[_]:s.includes(_)||s.push(_)}}}else if(n&&e.deps===null&&e.effects===null){var a=e,o=a.parent;o!==null&&(o.f&ne)===0&&(a.f^=ne)}if(Xe){if(Ne.has(e))return Ne.get(e);if(n){a=e;var l=a.v;return((a.f&M)===0&&a.reactions!==null||Nr(a))&&(l=Pn(a)),Ne.set(a,l),l}}else n&&(a=e,fn(a)&&cr(a));if((e.f&Ge)!==0)throw e.v;return e.v}function Nr(e){if(e.v===z)return!0;if(e.deps===null)return!1;for(const t of e.deps)if(Ne.has(t)||(t.f&K)!==0&&Nr(t))return!0;return!1}function cn(e){var t=fe;try{return fe=!0,e()}finally{fe=t}}const gs=-7169;function J(e,t){e.f=e.f&gs|t}const bs=new Set,Ur=new Set;let zr=null;function dn(e){var I;var t=this,n=t.ownerDocument,r=e.type,i=((I=e.composedPath)==null?void 0:I.call(e))||[],s=i[0]||e.target;zr=e;var a=0,o=zr===e&&e.__root;if(o){var l=i.indexOf(o);if(l!==-1&&(t===document||t===window)){e.__root=t;return}var f=i.indexOf(t);if(f===-1)return;l<=f&&(a=l)}if(s=i[a]||e.target,s!==t){vt(e,"currentTarget",{configurable:!0,get(){return s||n}});var h=_,d=y;Q(null),ye(null);try{for(var u,v=[];s!==null;){var m=s.assignedSlot||s.parentNode||s.host||null;try{var S=s["__"+r];if(S!=null&&(!s.disabled||e.target===s))if(Yn(S)){var[R,...k]=S;R.apply(s,[e,...k])}else S.call(s,e)}catch(C){u?v.push(C):u=C}if(e.cancelBubble||m===t||m===null)break;s=m}if(u){for(let C of v)queueMicrotask(()=>{throw C});throw u}}finally{e.__root=t,delete e.currentTarget,Q(h),ye(d)}}}function $s(e){var t=document.createElement("template");return t.innerHTML=e.replaceAll("<!>","<!---->"),t.content}function Oe(e,t){var n=y;n.nodes_start===null&&(n.nodes_start=e,n.nodes_end=t)}function gt(e,t){var n=(t&pi)!==0,r=(t&wi)!==0,i,s=!e.startsWith("<!>");return()=>{if(g)return Oe(b,null),b;i===void 0&&(i=$s(s?e:"<!>"+e),n||(i=Qe(i)));var a=r||vr?document.importNode(i,!0):i.cloneNode(!0);if(n){var o=Qe(a),l=a.lastChild;Oe(o,l)}else Oe(a,a);return a}}function Lr(e=""){if(!g){var t=me(e+"");return Oe(t,t),t}var n=b;return n.nodeType!==nn&&(n.before(n=me()),H(n)),Oe(n,n),n}function xs(){if(g)return Oe(b,null),b;var e=document.createDocumentFragment(),t=document.createComment(""),n=me();return e.append(t,n),Oe(t,n),e}function ge(e,t){if(g){y.nodes_end=b,Ct();return}e!==null&&e.before(t)}const Ss=["touchstart","touchmove"];function Es(e){return Ss.includes(e)}const Ts=["textarea","script","style","title"];function Rs(e){return Ts.includes(e)}function et(e,t){var n=t==null?"":typeof t=="object"?t+"":t;n!==(e.__t??(e.__t=e.nodeValue))&&(e.__t=n,e.nodeValue=n+"")}function Fr(e,t){return Mr(e,t)}function ks(e,t){An(),t.intro=t.intro??!1;const n=t.target,r=g,i=b;try{for(var s=Qe(n);s&&(s.nodeType!==jt||s.data!==Hn);)s=ke(s);if(!s)throw ht;de(!0),H(s);const a=Mr(e,{...t,anchor:s});return de(!1),a}catch(a){if(a instanceof Error&&a.message.split(`
`).some(o=>o.startsWith("https://svelte.dev/e/")))throw a;return a!==ht&&console.warn("Failed to hydrate: ",a),t.recover===!1&&Ii(),An(),as(n),de(!1),Fr(e,t)}finally{de(r),H(i)}}const bt=new Map;function Mr(e,{target:t,anchor:n,props:r={},events:i,context:s,intro:a=!0}){An();var o=new Set,l=d=>{for(var u=0;u<d.length;u++){var v=d[u];if(!o.has(v)){o.add(v);var m=Es(v);t.addEventListener(v,dn,{passive:m});var S=bt.get(v);S===void 0?(document.addEventListener(v,dn,{passive:m}),bt.set(v,1)):bt.set(v,S+1)}}};l(gi(bs)),Ur.add(l);var f=void 0,h=hs(()=>{var d=n??t.appendChild(me());return Qi(d,{pending:()=>{}},u=>{if(s){Dt({});var v=P;v.c=s}if(i&&(r.$$events=i),g&&Oe(u,null),f=e(u,r)||{},g&&(y.nodes_end=b,b===null||b.nodeType!==jt||b.data!==Vn))throw rn(),ht;s&&It()}),()=>{var m;for(var u of o){t.removeEventListener(u,dn);var v=bt.get(u);--v===0?(document.removeEventListener(u,dn),bt.delete(u)):bt.set(u,v)}Ur.delete(l),d!==n&&((m=d.parentNode)==null||m.removeChild(d))}});return Dn.set(f,h),f}let Dn=new WeakMap;function Os(e,t){const n=Dn.get(e);return n?(Dn.delete(e),n(t)):Promise.resolve()}function Br(e){P===null&&Oi(),mt&&P.l!==null?Ps(P).m.push(e):yr(()=>{const t=cn(e);if(typeof t=="function")return t})}function Ps(e){var t=e.l;return t.u??(t.u={a:[],b:[],m:[]})}function Wr(e,t,n=!1){g&&Ct();var r=e,i=null,s=null,a=z,o=n?Ot:0,l=!1;const f=(v,m=!0)=>{l=!0,u(m,v)};var h=null;function d(){h!==null&&(h.lastChild.remove(),r.before(h),h=null);var v=a?i:s,m=a?s:i;v&&Tr(v),m&&_t(m,()=>{a?s=null:i=null})}const u=(v,m)=>{if(a===(a=v))return;let S=!1;if(g){const le=Bi(r)===$n;!!a===le&&(r=Zn(),H(r),de(!1),S=!0)}var R=os(),k=r;if(R&&(h=document.createDocumentFragment(),h.append(k=me())),a?i??(i=m&&_e(()=>m(k))):s??(s=m&&_e(()=>m(k))),R){var I=A,C=a?i:s,w=a?s:i;C&&I.skipped_effects.delete(C),w&&I.skipped_effects.add(w),I.add_callback(d)}else d();S&&de(!0)};Cn(()=>{l=!1,t(f),l||u(null,null)},o),g&&(r=b)}function As(e,t,n,r,i,s){let a=g;g&&Ct();var o,l,f=null;g&&b.nodeType===ki&&(f=b,Ct());var h=g?b:e,d;Cn(()=>{const u=t()||null;var v=u==="svg"?_i:null;u!==o&&(d&&(u===null?_t(d,()=>{d=null,l=null}):u===l?Tr(d):re(d)),u&&u!==l&&(d=_e(()=>{if(f=g?f:v?document.createElementNS(v,u):document.createElement(u),Oe(f,f),r){g&&Rs(u)&&f.append(document.createComment(""));var m=g?Qe(f):f.appendChild(me());g&&(m===null?de(!1):H(m)),r(f,m)}y.nodes_end=f,h.before(f)})),o=u,o&&(l=o))},Ot),a&&(de(!0),H(h))}function hn(e,t){br(()=>{var n=e.getRootNode(),r=n.host?n:n.head??n.ownerDocument.head;if(!r.querySelector("#"+t.hash)){const i=document.createElement("style");i.id=t.hash,i.textContent=t.code,r.appendChild(i)}})}const Hr=[...` 	
\r\f \v\uFEFF`];function js(e,t,n){var r=e==null?"":""+e;if(t&&(r=r?r+" "+t:t),n){for(var i in n)if(n[i])r=r?r+" "+i:i;else if(r.length)for(var s=i.length,a=0;(a=r.indexOf(i,a))>=0;){var o=a+s;(a===0||Hr.includes(r[a-1]))&&(o===r.length||Hr.includes(r[o]))?r=(a===0?"":r.substring(0,a))+r.substring(o+1):a=o}}return r===""?null:r}function Cs(e,t){return e==null?null:String(e)}function Vr(e,t,n,r,i,s){var a=e.__className;if(g||a!==n||a===void 0){var o=js(n,r,s);(!g||o!==e.getAttribute("class"))&&(o==null?e.removeAttribute("class"):t?e.className=o:e.setAttribute("class",o)),e.__className=n}else if(s&&i!==s)for(var l in s){var f=!!s[l];(i==null||f!==!!i[l])&&e.classList.toggle(l,f)}return s}function Ds(e,t,n,r){var i=e.__style;if(g||i!==t){var s=Cs(t);(!g||s!==e.getAttribute("style"))&&(s==null?e.removeAttribute("style"):e.style.cssText=s),e.__style=t}return r}function qr(e,t){return e===t||(e==null?void 0:e[Pt])===t}function Is(e={},t,n,r){return br(()=>{var i,s;return jn(()=>{i=s,s=[],cn(()=>{e!==n(...s)&&(t(e,...s),i&&qr(n(...i),e)&&t(null,...i))})}),()=>{Ut(()=>{s&&qr(n(...s),e)&&t(null,...s)})}}),e}let vn=!1;function Ns(e){var t=vn;try{return vn=!1,[e(),vn]}finally{vn=t}}function Le(e,t,n,r){var C;var i=!mt||(n&D)!==0,s=(n&vi)!==0,a=(n&mi)!==0,o=r,l=!0,f=()=>(l&&(l=!1,o=a?cn(r):r),o),h;if(s){var d=Pt in e||Qn in e;h=((C=He(e,t))==null?void 0:C.set)??(d&&t in e?w=>e[t]=w:void 0)}var u,v=!1;s?[u,v]=Ns(()=>e[t]):u=e[t],u===void 0&&r!==void 0&&(u=f(),h&&(i&&Ni(),h(u)));var m;if(i?m=()=>{var w=e[t];return w===void 0?f():(l=!0,w)}:m=()=>{var w=e[t];return w!==void 0&&(o=void 0),w===void 0?o:w},i&&(n&Xt)===0)return m;if(h){var S=e.$$legacy;return(function(w,le){return arguments.length>0?((!i||!le||S||v)&&h(le?m():w),w):m()})}var R=!1,k=((n&T)!==0?on:fr)(()=>(R=!1,m()));s&&$(k);var I=y;return(function(w,le){if(arguments.length>0){const Ae=le?$(k):i&&s?Ue(w):w;return j(k,Ae),R=!0,o!==void 0&&(o=Ae),w}return Xe&&R||(I.f&qe)!==0?k.v:$(k)})}function Us(e){return new zs(e)}class zs{constructor(t){x(this,Pe);x(this,oe);var s;var n=new Map,r=(a,o)=>{var l=ss(o,!1,!1);return n.set(a,l),l};const i=new Proxy({...t.props||{},$$events:{}},{get(a,o){return $(n.get(o)??r(o,Reflect.get(a,o)))},has(a,o){return o===Qn?!0:($(n.get(o)??r(o,Reflect.get(a,o))),Reflect.has(a,o))},set(a,o,l){return j(n.get(o)??r(o,l),l),Reflect.set(a,o,l)}});p(this,oe,(t.hydrate?ks:Fr)(t.component,{target:t.target,anchor:t.anchor,props:i,context:t.context,intro:t.intro??!1,recover:t.recover})),(!((s=t==null?void 0:t.props)!=null&&s.$$host)||t.sync===!1)&&Te(),p(this,Pe,i.$$events);for(const a of Object.keys(c(this,oe)))a==="$set"||a==="$destroy"||a==="$on"||vt(this,a,{get(){return c(this,oe)[a]},set(o){c(this,oe)[a]=o},enumerable:!0});c(this,oe).$set=a=>{Object.assign(i,a)},c(this,oe).$destroy=()=>{Os(c(this,oe))}}$set(t){c(this,oe).$set(t)}$on(t,n){c(this,Pe)[t]=c(this,Pe)[t]||[];const r=(...i)=>n.call(this,...i);return c(this,Pe)[t].push(r),()=>{c(this,Pe)[t]=c(this,Pe)[t].filter(i=>i!==r)}}$destroy(){c(this,oe).$destroy()}}Pe=new WeakMap,oe=new WeakMap;let Yr;typeof HTMLElement=="function"&&(Yr=class extends HTMLElement{constructor(t,n,r){super();W(this,"$$ctor");W(this,"$$s");W(this,"$$c");W(this,"$$cn",!1);W(this,"$$d",{});W(this,"$$r",!1);W(this,"$$p_d",{});W(this,"$$l",{});W(this,"$$l_u",new Map);W(this,"$$me");this.$$ctor=t,this.$$s=n,r&&this.attachShadow({mode:"open"})}addEventListener(t,n,r){if(this.$$l[t]=this.$$l[t]||[],this.$$l[t].push(n),this.$$c){const i=this.$$c.$on(t,n);this.$$l_u.set(n,i)}super.addEventListener(t,n,r)}removeEventListener(t,n,r){if(super.removeEventListener(t,n,r),this.$$c){const i=this.$$l_u.get(n);i&&(i(),this.$$l_u.delete(n))}}async connectedCallback(){if(this.$$cn=!0,!this.$$c){let t=function(i){return s=>{const a=document.createElement("slot");i!=="default"&&(a.name=i),ge(s,a)}};if(await Promise.resolve(),!this.$$cn||this.$$c)return;const n={},r=Ls(this);for(const i of this.$$s)i in r&&(i==="default"&&!this.$$d.children?(this.$$d.children=t(i),n.default=!0):n[i]=t(i));for(const i of this.attributes){const s=this.$$g_p(i.name);s in this.$$d||(this.$$d[s]=mn(s,i.value,this.$$p_d,"toProp"))}for(const i in this.$$p_d)!(i in this.$$d)&&this[i]!==void 0&&(this.$$d[i]=this[i],delete this[i]);this.$$c=Us({component:this.$$ctor,target:this.shadowRoot||this,props:{...this.$$d,$$slots:n,$$host:this}}),this.$$me=ds(()=>{jn(()=>{var i;this.$$r=!0;for(const s of Zt(this.$$c)){if(!((i=this.$$p_d[s])!=null&&i.reflect))continue;this.$$d[s]=this.$$c[s];const a=mn(s,this.$$d[s],this.$$p_d,"toAttribute");a==null?this.removeAttribute(this.$$p_d[s].attribute||s):this.setAttribute(this.$$p_d[s].attribute||s,a)}this.$$r=!1})});for(const i in this.$$l)for(const s of this.$$l[i]){const a=this.$$c.$on(i,s);this.$$l_u.set(s,a)}this.$$l={}}}attributeChangedCallback(t,n,r){var i;this.$$r||(t=this.$$g_p(t),this.$$d[t]=mn(t,r,this.$$p_d,"toProp"),(i=this.$$c)==null||i.$set({[t]:this.$$d[t]}))}disconnectedCallback(){this.$$cn=!1,Promise.resolve().then(()=>{!this.$$cn&&this.$$c&&(this.$$c.$destroy(),this.$$me(),this.$$c=void 0)})}$$g_p(t){return Zt(this.$$p_d).find(n=>this.$$p_d[n].attribute===t||!this.$$p_d[n].attribute&&n.toLowerCase()===t)||t}});function mn(e,t,n,r){var s;const i=(s=n[e])==null?void 0:s.type;if(t=i==="Boolean"&&typeof t!="boolean"?t!=null:t,!r||!n[e])return t;if(r==="toAttribute")switch(i){case"Object":case"Array":return t==null?null:JSON.stringify(t);case"Boolean":return t?"":null;case"Number":return t??null;default:return t}else switch(i){case"Object":case"Array":return t&&JSON.parse(t);case"Boolean":return t;case"Number":return t!=null?+t:t;default:return t}}function Ls(e){const t={};return e.childNodes.forEach(n=>{t[n.slot||"default"]=!0}),t}function Ht(e,t,n,r,i,s){let a=class extends Yr{constructor(){super(e,n,i),this.$$p_d=t}static get observedAttributes(){return Zt(t).map(o=>(t[o].attribute||o).toLowerCase())}};return Zt(t).forEach(o=>{vt(a.prototype,o,{get(){return this.$$c&&o in this.$$c?this.$$c[o]:this.$$d[o]},set(l){var d;l=mn(o,l,t),this.$$d[o]=l;var f=this.$$c;if(f){var h=(d=He(f,o))==null?void 0:d.get;h?f[o]=l:f.$set({[o]:l})}}})}),r.forEach(o=>{vt(a.prototype,o,{get(){var l;return(l=this.$$c)==null?void 0:l[o]}})}),e.element=a,a}const Gr={hour:"2-digit",minute:"2-digit",second:"2-digit"},Jr=(e,t,n=void 0)=>new Intl.DateTimeFormat(t,n).format(e),Kr=1440*60*1e3,In=(e,t)=>{const n=new Date(e),r=new Date(t);return n.setHours(0,0,0,0),r.setHours(0,0,0,0),Math.round((r.getTime()-n.getTime())/Kr)},Fs=(e,t)=>Math.ceil((t-e)/Kr),Ms=(e,t)=>new Intl.NumberFormat(t,{style:"unit",unit:"day",unitDisplay:"long"}).format(e),Bs=/\{[^{}]+\}/g,Ws=()=>{var e,t;return typeof process=="object"&&Number.parseInt((t=(e=process==null?void 0:process.versions)==null?void 0:e.node)==null?void 0:t.substring(0,2))>=18&&process.versions.undici};function Hs(){return Math.random().toString(36).slice(2,11)}function Vs(e){let{baseUrl:t="",Request:n=globalThis.Request,fetch:r=globalThis.fetch,querySerializer:i,bodySerializer:s,headers:a,requestInitExt:o=void 0,...l}={...e};o=Ws()?o:void 0,t=ti(t);const f=[];async function h(d,u){const{baseUrl:v,fetch:m=r,Request:S=n,headers:R,params:k={},parseAs:I="json",querySerializer:C,bodySerializer:w=s??Ys,body:le,...Ae}=u||{};let at=t;v&&(at=ti(v)??t);let ot=typeof i=="function"?i:Zr(i);C&&(ot=typeof C=="function"?C:Zr({...typeof i=="object"?i:{},...C}));const lt=le===void 0?void 0:w(le,ei(a,R,k.header)),zn=ei(lt===void 0||lt instanceof FormData?{}:{"Content-Type":"application/json"},a,R,k.header),Kt={redirect:"follow",...l,...Ae,body:lt,headers:zn};let ft,kt,ce=new S(Gs(d,{baseUrl:at,params:k,querySerializer:ot}),Kt),O;for(const B in Ae)B in ce||(ce[B]=Ae[B]);if(f.length){ft=Hs(),kt=Object.freeze({baseUrl:at,fetch:m,parseAs:I,querySerializer:ot,bodySerializer:w});for(const B of f)if(B&&typeof B=="object"&&typeof B.onRequest=="function"){const N=await B.onRequest({request:ce,schemaPath:d,params:k,options:kt,id:ft});if(N)if(N instanceof S)ce=N;else if(N instanceof Response){O=N;break}else throw new Error("onRequest: must return new Request() or Response() when modifying the request")}}if(!O){try{O=await m(ce,o)}catch(B){let N=B;if(f.length)for(let je=f.length-1;je>=0;je--){const ut=f[je];if(ut&&typeof ut=="object"&&typeof ut.onError=="function"){const ct=await ut.onError({request:ce,error:N,schemaPath:d,params:k,options:kt,id:ft});if(ct){if(ct instanceof Response){N=void 0,O=ct;break}if(ct instanceof Error){N=ct;continue}throw new Error("onError: must return new Response() or instance of Error")}}}if(N)throw N}if(f.length)for(let B=f.length-1;B>=0;B--){const N=f[B];if(N&&typeof N=="object"&&typeof N.onResponse=="function"){const je=await N.onResponse({request:ce,response:O,schemaPath:d,params:k,options:kt,id:ft});if(je){if(!(je instanceof Response))throw new Error("onResponse: must return new Response() when modifying the response");O=je}}}}if(O.status===204||ce.method==="HEAD"||O.headers.get("Content-Length")==="0")return O.ok?{data:void 0,response:O}:{error:void 0,response:O};if(O.ok)return I==="stream"?{data:O.body,response:O}:{data:await O[I](),response:O};let Qt=await O.text();try{Qt=JSON.parse(Qt)}catch{}return{error:Qt,response:O}}return{request(d,u,v){return h(u,{...v,method:d.toUpperCase()})},GET(d,u){return h(d,{...u,method:"GET"})},PUT(d,u){return h(d,{...u,method:"PUT"})},POST(d,u){return h(d,{...u,method:"POST"})},DELETE(d,u){return h(d,{...u,method:"DELETE"})},OPTIONS(d,u){return h(d,{...u,method:"OPTIONS"})},HEAD(d,u){return h(d,{...u,method:"HEAD"})},PATCH(d,u){return h(d,{...u,method:"PATCH"})},TRACE(d,u){return h(d,{...u,method:"TRACE"})},use(...d){for(const u of d)if(u){if(typeof u!="object"||!("onRequest"in u||"onResponse"in u||"onError"in u))throw new Error("Middleware must be an object with one of `onRequest()`, `onResponse() or `onError()`");f.push(u)}},eject(...d){for(const u of d){const v=f.indexOf(u);v!==-1&&f.splice(v,1)}}}}function pn(e,t,n){if(t==null)return"";if(typeof t=="object")throw new Error("Deeply-nested arrays/objects aren’t supported. Provide your own `querySerializer()` to handle these.");return`${e}=${(n==null?void 0:n.allowReserved)===!0?t:encodeURIComponent(t)}`}function Qr(e,t,n){if(!t||typeof t!="object")return"";const r=[],i={simple:",",label:".",matrix:";"}[n.style]||"&";if(n.style!=="deepObject"&&n.explode===!1){for(const o in t)r.push(o,n.allowReserved===!0?t[o]:encodeURIComponent(t[o]));const a=r.join(",");switch(n.style){case"form":return`${e}=${a}`;case"label":return`.${a}`;case"matrix":return`;${e}=${a}`;default:return a}}for(const a in t){const o=n.style==="deepObject"?`${e}[${a}]`:a;r.push(pn(o,t[a],n))}const s=r.join(i);return n.style==="label"||n.style==="matrix"?`${i}${s}`:s}function Xr(e,t,n){if(!Array.isArray(t))return"";if(n.explode===!1){const s={form:",",spaceDelimited:"%20",pipeDelimited:"|"}[n.style]||",",a=(n.allowReserved===!0?t:t.map(o=>encodeURIComponent(o))).join(s);switch(n.style){case"simple":return a;case"label":return`.${a}`;case"matrix":return`;${e}=${a}`;default:return`${e}=${a}`}}const r={simple:",",label:".",matrix:";"}[n.style]||"&",i=[];for(const s of t)n.style==="simple"||n.style==="label"?i.push(n.allowReserved===!0?s:encodeURIComponent(s)):i.push(pn(e,s,n));return n.style==="label"||n.style==="matrix"?`${r}${i.join(r)}`:i.join(r)}function Zr(e){return function(n){const r=[];if(n&&typeof n=="object")for(const i in n){const s=n[i];if(s!=null){if(Array.isArray(s)){if(s.length===0)continue;r.push(Xr(i,s,{style:"form",explode:!0,...e==null?void 0:e.array,allowReserved:(e==null?void 0:e.allowReserved)||!1}));continue}if(typeof s=="object"){r.push(Qr(i,s,{style:"deepObject",explode:!0,...e==null?void 0:e.object,allowReserved:(e==null?void 0:e.allowReserved)||!1}));continue}r.push(pn(i,s,e))}}return r.join("&")}}function qs(e,t){let n=e;for(const r of e.match(Bs)??[]){let i=r.substring(1,r.length-1),s=!1,a="simple";if(i.endsWith("*")&&(s=!0,i=i.substring(0,i.length-1)),i.startsWith(".")?(a="label",i=i.substring(1)):i.startsWith(";")&&(a="matrix",i=i.substring(1)),!t||t[i]===void 0||t[i]===null)continue;const o=t[i];if(Array.isArray(o)){n=n.replace(r,Xr(i,o,{style:a,explode:s}));continue}if(typeof o=="object"){n=n.replace(r,Qr(i,o,{style:a,explode:s}));continue}if(a==="matrix"){n=n.replace(r,`;${pn(i,o)}`);continue}n=n.replace(r,a==="label"?`.${encodeURIComponent(o)}`:encodeURIComponent(o))}return n}function Ys(e,t){return e instanceof FormData?e:t&&(t.get instanceof Function?t.get("Content-Type")??t.get("content-type"):t["Content-Type"]??t["content-type"])==="application/x-www-form-urlencoded"?new URLSearchParams(e).toString():JSON.stringify(e)}function Gs(e,t){var i;let n=`${t.baseUrl}${e}`;(i=t.params)!=null&&i.path&&(n=qs(n,t.params.path));let r=t.querySerializer(t.params.query??{});return r.startsWith("?")&&(r=r.substring(1)),r&&(n+=`?${r}`),n}function ei(...e){const t=new Headers;for(const n of e){if(!n||typeof n!="object")continue;const r=n instanceof Headers?n.entries():Object.entries(n);for(const[i,s]of r)if(s===null)t.delete(i);else if(Array.isArray(s))for(const a of s)t.append(i,a);else s!==void 0&&t.set(i,s)}return t}function ti(e){return e.endsWith("/")?e.substring(0,e.length-1):e}const ni={at:"de-AT",ar:"es-AR",be:"nl-BE",br:"pt-BR",ch:"de-CH",co:"es-CO",com:"en-GB",de:"de-DE",es:"es-ES",fr:"fr-FR",gr:"el-GR",id:"id-ID",in:"en-IN",it:"it-IT",jp:"ja-JP",kr:"ko-KR",mx:"es-MX",nl:"nl-NL",pe:"es-PE",pl:"pl-PL",pt:"pt-PT",ro:"ro-RO",tr:"tr-TR",uk:"en-GB",us:"en-US",world:"ru-RU",za:"en-GB"},Js="com",ri="en-US",Nn={accessToken:null,baseUrl:"https://tmapi-alpha.transfermarkt.technology/",useDomainContext:!1,useLocale:!1,signal:null},Ks=(e={})=>{Nn.baseUrl=document.body.getAttribute("data-api-domain")??Nn.baseUrl;const t={...Nn,...e},n=document.body.getAttribute("data-tm-tld")??Js,r=ni[n]??ri,i=Vs({baseUrl:t.baseUrl,headers:{Accept:"application/json","Accept-Language":t.useLocale?r:ri,...t.accessToken?{Authorization:`Bearer ${t.accessToken}`}:{}},...t.signal?{signal:t.signal}:{}});if(t.useDomainContext){const s={async onRequest({request:a}){const o=new URL(a.url);if(o.searchParams.set("_x_preferred_context",n),["POST","PUT","PATCH"].includes(a.method)){const l=await a.clone().text();return new Request(o.toString(),{method:a.method,headers:a.headers,body:l,mode:a.mode,credentials:a.credentials,cache:a.cache,redirect:a.redirect,referrer:a.referrer,referrerPolicy:a.referrerPolicy,integrity:a.integrity,keepalive:a.keepalive,signal:a.signal})}else return new Request(o.toString(),{method:a.method,headers:a.headers,mode:a.mode,credentials:a.credentials,cache:a.cache,redirect:a.redirect,referrer:a.referrer,referrerPolicy:a.referrerPolicy,integrity:a.integrity,keepalive:a.keepalive,signal:a.signal})}};i.use(s)}return i},Qs=async(e,t=-1)=>{const n=Ks({useLocale:!0}),{data:r,error:i}=await n.GET("/competition/{competitionId}/transfer-window",{params:{path:{competitionId:e},...t!==-1?{query:{maxDaysInPast:t}}:{}}});if(i||!(r!=null&&r.data))throw new Error(`Failed to fetch transfer window data for competition ID: ${e}`);return r.data},Xs=()=>document.body.getAttribute("data-tm-tld")||"com",Zs=()=>ni[Xs()]??"en-US",ii=e=>new Date(e).getTime(),si=(e,t)=>{const[n,r,i]=e.split(":").map(Number),s=new Date,a=new Date(s.getFullYear(),s.getMonth(),s.getDate(),n,r,i),o=new Intl.DateTimeFormat(t,{timeStyle:"short"}).format(a);return`${new Intl.RelativeTimeFormat(t,{numeric:"auto"}).format(0,"day")}, ${o}`},ea=10,Vt=Zs(),Un=(e,t,n,r)=>({state:e,relative:t,days:n,dayString:Ms(n,Vt),time:r}),ta=async(e,t=-1)=>{const n=await Qs(e,t);if(n.length===0)return;const r=new Date().getTime(),i=n.map(l=>({transferWindow:l,from:ii(l.from),to:ii(l.to)})),s=i.find(l=>l.from<=r&&r<=l.to);if(s){const l=In(r,s.to),h=Fs(r,s.to)<=1?new Date(s.to-r).toISOString().slice(11,19):void 0;return Un("open","closes_in",l,h)}const a=i.filter(l=>l.to<r).sort((l,f)=>f.to-l.to).shift(),o=i.filter(l=>l.from>r).sort((l,f)=>l.from-f.from).shift();if(a){const l=In(a.to,r);if(l<=ea||!o){const f=l===0?Jr(new Date(a.to),Vt,Gr):void 0;return Un("closed","closed_since",l,f?si(f,Vt):void 0)}}if(o){const l=In(r,o.from),f=l===0?Jr(new Date(o.from),Vt,Gr):void 0;return Un("closed","opens_in",l,f?si(f,Vt):void 0)}},na=(e,t)=>{const n=new IntersectionObserver(r=>{(r[0].isIntersecting||r[0].intersectionRatio>0)&&(t(),n.disconnect())},{root:null,rootMargin:"200px 0px 200px 0px",threshold:1});return n.observe(e),n},ra=e=>{if(!e)return;const t=e.getRootNode();t instanceof ShadowRoot&&t.host instanceof HTMLElement?e.parentNode instanceof ShadowRoot?t.host.remove():e.remove():e.parentElement&&e.parentElement.remove()};Vi();const ia={hash:"svelte-1r2dsxy",code:`/* stylelint-disable */
/* stylelint-enable */
/* stylelint-disable */
/* stylelint-enable */
/* stylelint-disable */
/* stylelint-enable */.content-box-headline.svelte-1r2dsxy {background-color:#00193f;color:white;display:block;font-family:'Oswald-VF', 'Oswald-fallback', sans-serif;font-size:1rem;font-variation-settings:"wght" 400;font-weight:initial;line-height:1.625rem;margin:0;padding:0 0.5rem !important;scroll-margin-top:5rem;text-transform:uppercase;}`};function ai(e,t){Dt(t,!1),hn(e,ia);let n=Le(t,"elementType",12,"div"),r=Le(t,"headline",12,"");var i={get elementType(){return n()},set elementType(o){n(o),Te()},get headline(){return r()},set headline(o){r(o),Te()}},s=xs(),a=wr(s);return As(a,n,!1,(o,l)=>{Vr(o,0,"content-box-headline svelte-1r2dsxy");var f=Lr();Mt(()=>et(f,r())),ge(l,f)}),ge(e,s),It(i)}Ht(ai,{elementType:{},headline:{}},[],[],!0);function oi(e,t){Dt(t,!0);const n=3600,r=60;let i=Le(t,"timeString",7),s=L(Ue(i()));const a=()=>{let[f,h,d]=$(s).split(":").map(Number),u=f*n+h*r+d;u=Math.max(0,u-1);const v=String(Math.floor(u/n)),m=String(Math.floor(u%n/r)).padStart(2,"0"),S=String(u%r).padStart(2,"0");j(s,`${v}:${m}:${S}`)};Br(()=>{const f=setInterval(a,1e3);return()=>clearInterval(f)});var o={get timeString(){return i()},set timeString(f){i(f),Te()}};Xn();var l=Lr();return Mt(()=>et(l,$(s))),ge(e,l),It(o)}Ht(oi,{timeString:{}},[],[],!0);var sa=gt('<div class="svelte-py9x6n"></div>');const aa={hash:"svelte-py9x6n",code:`/* stylelint-disable */
/* stylelint-enable */
@keyframes svelte-py9x6n-sk-pulse {
  0% {
    opacity: 0.6;
  }
  50% {
    opacity: 0.8;
  }
  100% {
    opacity: 0.6;
  }
}div.svelte-py9x6n {
  animation: svelte-py9x6n-sk-pulse 1.5s infinite;background-color:#e9e9e9;}`};function tt(e,t){Dt(t,!0),hn(e,aa);let n=Le(t,"height",7,"100%"),r=Le(t,"width",7,"100%");var i={get height(){return n()},set height(a="100%"){n(a),Te()},get width(){return r()},set width(a="100%"){r(a),Te()}},s=sa();return Mt(()=>Ds(s,`height: ${n()??""}; width: ${r()??""};`)),ge(e,s),It(i)}Ht(tt,{height:{},width:{}},[],[],!0);var oa=gt('<div><!> <div class="inner svelte-1suw85r"><div class="row svelte-1suw85r"><!> <!></div> <div class="row svelte-1suw85r"><!> <!></div> <div class="link svelte-1suw85r"><!></div></div></div>');const la={hash:"svelte-1suw85r",code:`/* stylelint-disable */
/* stylelint-enable */
/* stylelint-disable */
/* stylelint-enable */
/* stylelint-disable */
/* stylelint-enable */
/* stylelint-disable */
/* stylelint-enable */
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@container (max-width: 340px) {
}
@media print, (min-width: 769px) {
}
@container (max-width: 340px) {
}
@media print, (min-width: 769px) {
}

@font-face {font-display:swap;font-family:"SourceSansPro-VF";font-style:normal;font-weight:normal;src:url("https://tmsi.akamaized.net/fonts/SourceSans3VF-Roman.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Oswald-VF";font-style:normal;font-weight:normal;src:url("https://tmsi.akamaized.net/fonts/oswald-var.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Oswald";font-style:normal;font-weight:200;src:url("https://tmsi.akamaized.net/fonts/Oswald-Light200.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Oswald";font-style:normal;font-weight:400;src:url("https://tmsi.akamaized.net/fonts/Oswald-Regular400.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Oswald";font-style:normal;font-weight:700;src:url("https://tmsi.akamaized.net/fonts/Oswald-Bold700.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"OSL";font-style:normal;font-weight:300;src:url("https://tmsi.akamaized.net/fonts/OpenSans-CondensedLight300.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"OSB";font-style:normal;font-weight:300;src:url("https://tmsi.akamaized.net/fonts/OpenSans-CondensedLight300.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Source Sans Pro";font-style:normal;font-weight:700;src:url("https://tmsi.akamaized.net/fonts/SourceSansPro-Bold700.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Source Sans Pro";font-style:normal;font-weight:400;src:url("https://tmsi.akamaized.net/fonts/SourceSansPro-Regular400.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Source Sans Pro";font-style:normal;font-weight:700;src:url("https://tmsi.akamaized.net/fonts/SourceSansPro-Bold700.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"UniviaPro";font-style:normal;font-weight:450;src:url("https://tmsi.akamaized.net/fonts/UniviaPro-Regular.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"UniviaPro";font-style:normal;font-weight:500;src:url("https://tmsi.akamaized.net/fonts/UniviaPro-Medium.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"UniviaPro";font-style:normal;font-weight:700;src:url("https://tmsi.akamaized.net/fonts/UniviaPro-Bold.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"UniviaPro";font-style:normal;font-weight:900;src:url("https://tmsi.akamaized.net/fonts/UniviaPro-Black.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"UniviaPro";font-style:normal;font-weight:950;src:url("https://tmsi.akamaized.net/fonts/UniviaPro-Ultra.woff2") format("woff2");
}
@font-face {ascent-override:160%;font-family:"Oswald-fallback";size-adjust:81.94%;src:local("Arial");
}
@font-face {ascent-override:111%;font-family:"Source Sans Pro-fallback";size-adjust:93.75%;src:local("Arial");
}
@font-face {ascent-override:110%;font-family:"OSL-fallback";size-adjust:73.1%;src:local("Arial");
}
@font-face {ascent-override:110%;font-family:"OSB-fallback";size-adjust:62.7%;src:local("Arial");
}
@font-face {ascent-override:75.84%;descent-override:18.96%;font-family:"UniviaPro-fallback";line-gap-override:18.96%;size-adjust:105.49%;src:local("Arial");
}
@media print, (max-width: 768px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}.inner.svelte-1suw85r {padding:0.3125rem 0.3125rem 0;}.row.svelte-1suw85r {align-items:center;display:flex;height:22px;justify-content:space-between;}.link.svelte-1suw85r {align-items:center;display:flex;height:38px;justify-content:flex-end;padding:0 0.3125rem;}`};function li(e){hn(e,la);var t=oa(),n=q(t);tt(n,{height:"26px"});var r=pe(n,2),i=q(r),s=q(i);tt(s,{height:"12px",width:"35px"});var a=pe(s,2);tt(a,{height:"12px",width:"35px"}),V(i);var o=pe(i,2),l=q(o);tt(l,{height:"12px",width:"35px"});var f=pe(l,2);tt(f,{height:"12px",width:"35px"}),V(o);var h=pe(o,2),d=q(h);tt(d,{height:"12px",width:"160px"}),V(h),V(r),V(t),ge(e,t)}Ht(li,{},[],[],!0);var fa=gt("<span><!></span>"),ua=gt("<span> </span>"),ca=gt('<!> <div class="content svelte-gjt4pb"><div class="line svelte-gjt4pb"><span> </span> <strong> </strong></div> <div class="line svelte-gjt4pb"><span> </span> <!></div></div> <a href="/statistik/transferfenster" class="content-link svelte-gjt4pb"> </a>',1),da=gt('<section class="transfer-window-widget svelte-gjt4pb"><!></section>');const ha={hash:"svelte-gjt4pb",code:`/* stylelint-disable */
/* stylelint-enable */
/* stylelint-disable */
/* stylelint-enable */
/* stylelint-disable */
/* stylelint-enable */
/* stylelint-disable */
/* stylelint-enable */
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@container (max-width: 340px) {
}
@media print, (min-width: 769px) {
}
@container (max-width: 340px) {
}
@media print, (min-width: 769px) {
}

@font-face {font-display:swap;font-family:"SourceSansPro-VF";font-style:normal;font-weight:normal;src:url("https://tmsi.akamaized.net/fonts/SourceSans3VF-Roman.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Oswald-VF";font-style:normal;font-weight:normal;src:url("https://tmsi.akamaized.net/fonts/oswald-var.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Oswald";font-style:normal;font-weight:200;src:url("https://tmsi.akamaized.net/fonts/Oswald-Light200.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Oswald";font-style:normal;font-weight:400;src:url("https://tmsi.akamaized.net/fonts/Oswald-Regular400.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Oswald";font-style:normal;font-weight:700;src:url("https://tmsi.akamaized.net/fonts/Oswald-Bold700.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"OSL";font-style:normal;font-weight:300;src:url("https://tmsi.akamaized.net/fonts/OpenSans-CondensedLight300.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"OSB";font-style:normal;font-weight:300;src:url("https://tmsi.akamaized.net/fonts/OpenSans-CondensedLight300.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Source Sans Pro";font-style:normal;font-weight:700;src:url("https://tmsi.akamaized.net/fonts/SourceSansPro-Bold700.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Source Sans Pro";font-style:normal;font-weight:400;src:url("https://tmsi.akamaized.net/fonts/SourceSansPro-Regular400.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"Source Sans Pro";font-style:normal;font-weight:700;src:url("https://tmsi.akamaized.net/fonts/SourceSansPro-Bold700.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"UniviaPro";font-style:normal;font-weight:450;src:url("https://tmsi.akamaized.net/fonts/UniviaPro-Regular.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"UniviaPro";font-style:normal;font-weight:500;src:url("https://tmsi.akamaized.net/fonts/UniviaPro-Medium.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"UniviaPro";font-style:normal;font-weight:700;src:url("https://tmsi.akamaized.net/fonts/UniviaPro-Bold.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"UniviaPro";font-style:normal;font-weight:900;src:url("https://tmsi.akamaized.net/fonts/UniviaPro-Black.woff2") format("woff2");
}
@font-face {font-display:swap;font-family:"UniviaPro";font-style:normal;font-weight:950;src:url("https://tmsi.akamaized.net/fonts/UniviaPro-Ultra.woff2") format("woff2");
}
@font-face {ascent-override:160%;font-family:"Oswald-fallback";size-adjust:81.94%;src:local("Arial");
}
@font-face {ascent-override:111%;font-family:"Source Sans Pro-fallback";size-adjust:93.75%;src:local("Arial");
}
@font-face {ascent-override:110%;font-family:"OSL-fallback";size-adjust:73.1%;src:local("Arial");
}
@font-face {ascent-override:110%;font-family:"OSB-fallback";size-adjust:62.7%;src:local("Arial");
}
@font-face {ascent-override:75.84%;descent-override:18.96%;font-family:"UniviaPro-fallback";line-gap-override:18.96%;size-adjust:105.49%;src:local("Arial");
}
@media print, (max-width: 768px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media print, (min-width: 769px) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}
@media (hover: hover) {
}.transfer-window-widget.svelte-gjt4pb {background-color:white;border:0.0625rem solid #dddddd;font-family:'SourceSansPro-VF', sans-serif;margin-top:0.625rem;}.content.svelte-gjt4pb {padding:0.625rem 0.625rem 0.3125rem;}.line.svelte-gjt4pb {display:flex;justify-content:space-between;}.line.svelte-gjt4pb:first-child {margin-bottom:0.625rem;}.line.svelte-gjt4pb strong:where(.svelte-gjt4pb) {color:#8f1a29;}.line.svelte-gjt4pb strong.open:where(.svelte-gjt4pb) {color:#749f18;}a.content-link.svelte-gjt4pb {align-items:center;color:#1d75a3;cursor:pointer;display:flex;font-family:'SourceSansPro-VF', sans-serif;font-size:0.875rem;font-variation-settings:"wght" 700;font-weight:initial;justify-content:flex-end;line-height:0.875rem;padding:0.75rem;text-align:right;text-decoration:none;transition:color 0.08s ease-in;}a.content-link.svelte-gjt4pb:hover {color:#5ca6ff;text-decoration:none;transition:color 0.08s ease-in;}a.content-link.svelte-gjt4pb::after {border-right:0.125rem solid #00aded;border-top:0.125rem solid #00aded;box-sizing:border-box;content:"";display:block;height:0.4375rem;margin-left:0.5rem;transform:rotate(45deg);width:0.4375rem;}`};function fi(e,t){Dt(t,!0),hn(e,ha);let n=Le(t,"competitionId",7),r=Le(t,"maxDaysInPast",7,30),i=Le(t,"translations",7);const s={opens_in:i().opensIn,closes_in:i().closesIn,closed_since:i().closedSince};let a=L(void 0),o=L(!0),l=L(Ue(n())),f=L(!1),h=L(""),d=L(""),u=L(void 0),v=L(!1);const m=async()=>{j(l,n(),!0);const w=await ta(n(),r());if(!w){ra($(a));return}j(f,w.state==="open"),j(h,s[w.relative],!0),j(u,w.time,!0),$(u)?j(d,$(u),!0):j(d,w.dayString,!0),j(v,$(f)&&w.relative==="closes_in"&&!!$(u),!0),j(o,!1)};yr(()=>{!$(o)&&n()!==$(l)&&(j(o,!0),m())}),Br(()=>{$(a)&&na($(a),m)});var S={get competitionId(){return n()},set competitionId(w){n(w),Te()},get maxDaysInPast(){return r()},set maxDaysInPast(w=30){r(w),Te()},get translations(){return i()},set translations(w){i(w),Te()}},R=da(),k=q(R);{var I=w=>{li(w)},C=w=>{var le=ca(),Ae=wr(le);{let Se=rs(()=>i().currentTransferWindow||"Current Transfer Window");ai(Ae,{get headline(){return $(Se)}})}var at=pe(Ae,2),ot=q(at),lt=q(ot),zn=q(lt);V(lt);var Kt=pe(lt,2);let ft;var kt=q(Kt,!0);V(Kt),V(ot);var ce=pe(ot,2),O=q(ce),Qt=q(O);V(O);var B=pe(O,2);{var N=Se=>{var dt=fa(),Ln=q(dt);oi(Ln,{get timeString(){return $(u)}}),V(dt),ge(Se,dt)},je=Se=>{var dt=ua(),Ln=q(dt,!0);V(dt),Mt(()=>et(Ln,$(d))),ge(Se,dt)};Wr(B,Se=>{$(v)&&$(u)?Se(N):Se(je,!1)})}V(ce),V(at);var ut=pe(at,2),ct=q(ut,!0);V(ut),Mt(Se=>{et(zn,`${i().status??""}:`),ft=Vr(Kt,1,"svelte-gjt4pb",null,ft,Se),et(kt,$(f)?i().open:i().closed),et(Qt,`${$(h)??""}:`),et(ct,i().transferWindowOverview)},[()=>({open:$(f)})]),ge(w,le)};Wr(k,w=>{$(o)?w(I):w(C,!1)})}return V(R),Is(R,w=>j(a,w),()=>$(a)),ge(e,R),It(S)}return customElements.define("tm-transfer-window-widget",Ht(fi,{competitionId:{attribute:"competition-id",type:"String"},maxDaysInPast:{attribute:"max-days-in-past",type:"Number"},translations:{attribute:"translations",type:"Object"}},[],[],!0)),fi})();
