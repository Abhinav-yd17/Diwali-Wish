"""Diwali Festival Experience (enhanced, shareable with anyone) - a single-file Streamlit app."""
import html as _html
import base64
import mimetypes
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Diwali 🪔", page_icon="🪔", layout="wide")

# Put your own song at: assets/diwali.mp3
# The audio is bundled into the page so visitors hear the same track after deployment.
AUDIO_PATH = Path(__file__).parent / "assets" / "diwali.mp3"
MUSIC_PLAYER = ""
if AUDIO_PATH.exists():
    audio_type = mimetypes.guess_type(AUDIO_PATH.name)[0] or "audio/mpeg"
    audio_b64 = base64.b64encode(AUDIO_PATH.read_bytes()).decode("ascii")
    audio_src = f"data:{audio_type};base64,{audio_b64}"
    MUSIC_PLAYER = f"""
    <div id="musicDock">
      <audio id="bgMusic" src="{audio_src}" loop preload="auto" autoplay></audio>
      <button id="musicToggle" onclick="toggleOwnMusic()">▶ Play music</button>
      <label for="musicVolume">VOL</label>
      <input id="musicVolume" type="range" min="0" max="1" step="0.01" value="0.55"
             oninput="setOwnMusicVolume(this.value)">
    </div>
    """


# Optional personalisation: share the link as  https://your-app/?name=Anu
NAME = _html.escape(str(st.query_params.get("name", "")).strip()[:30])
PH = {"%%HEY%%": NAME or "there", "%%HEYU%%": (NAME or "there").upper(),
      "%%COMMA%%": f", {NAME}" if NAME else "", "%%COMMAU%%": f", {NAME.upper()}" if NAME else ""}

PAGES = ["intro", "hero", "treasure", "days", "diyas", "fun", "note", "finale", "game", "memory", "rangoli", "pop"]
if "page" not in st.session_state:
    st.session_state.page = "intro"


def go(p):
    st.session_state.page = p


# ---------------------------------------------------------------- outer styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Poppins:wght@300;400;600;800&display=swap');
#MainMenu, header, footer {visibility:hidden;}
.stApp {
  background:
    radial-gradient(circle at 15% 10%, rgba(185,128,255,.15), transparent 40%),
    radial-gradient(circle at 85% 90%, rgba(255,153,51,.12), transparent 45%),
    radial-gradient(ellipse at top, #2a0f4a 0%, #0a0614 75%);
}
.block-container {padding:0.5rem 1rem 2rem; max-width:1200px;}
iframe {border:0; border-radius:18px;}

/* Streamlit buttons */
.stButton>button {
  width:100%; min-height:64px; border-radius:16px; color:#ffe9b0; font-weight:600;
  background:rgba(255,255,255,.07); border:1px solid rgba(245,192,74,.45);
  backdrop-filter:blur(10px); transition:all .25s; white-space:normal;
  font-family:'Poppins','Segoe UI',sans-serif;
}
.stButton>button:hover {
  transform:translateY(-4px); border-color:#f5c04a;
  box-shadow:0 0 26px rgba(255,153,51,.55); color:#fff;
  background:rgba(255,153,51,.10);
}
.stButton>button:focus-visible {outline:3px solid #f5c04a; outline-offset:3px;}
.stButton>button:active {transform:translateY(-1px);}

/* Dramatic ENTER button on the intro screen */
.st-key-enter{
  position:fixed!important;left:50%!important;
  bottom:max(18px,env(safe-area-inset-bottom))!important;
  transform:translateX(-50%)!important;
  display:flex!important;justify-content:center!important;
  width:min(560px,92vw)!important;margin:0!important;
  z-index:999999!important;
  filter:drop-shadow(0 10px 28px rgba(0,0,0,.45));
}
.st-key-enter::before{
  content:"👇  CLICK THE BUTTON TO CONTINUE";
  position:absolute!important;
  left:50%!important;
  bottom:calc(100% + 13px)!important;
  transform:translateX(-50%)!important;
  width:max-content!important;
  max-width:90vw!important;
  padding:9px 16px!important;
  border:1px solid rgba(255,224,151,.55)!important;
  border-radius:999px!important;
  background:rgba(35,12,48,.88)!important;
  color:#fff0c2!important;
  font-family:'Poppins','Segoe UI',sans-serif!important;
  font-size:clamp(.72rem,2.4vw,.95rem)!important;
  font-weight:800!important;
  letter-spacing:.09em!important;
  text-align:center!important;
  text-shadow:0 1px 8px rgba(0,0,0,.45)!important;
  box-shadow:0 5px 22px rgba(0,0,0,.28)!important;
  animation:instructionPulse 1.8s ease-in-out infinite!important;
  pointer-events:none!important;
}
@keyframes instructionPulse{
  0%,100%{opacity:.82;transform:translateX(-50%) translateY(0)}
  50%{opacity:1;transform:translateX(-50%) translateY(-4px)}
}
.st-key-enter button{
  width:min(560px,92vw)!important;min-height:92px!important;padding:20px 34px!important;
  border:2px solid rgba(255,239,190,.95)!important;border-radius:22px!important;
  background:linear-gradient(110deg,#ff8b22 0%,#ffd978 32%,#fff0b5 50%,#f4b632 72%,#ff8b22 100%)!important;
  background-size:220% 100%!important;color:#32104e!important;
  font-family:'Poppins','Segoe UI',sans-serif!important;font-size:clamp(1.05rem,2.8vw,1.5rem)!important;
  font-weight:900!important;letter-spacing:.09em!important;text-transform:uppercase!important;
  box-shadow:0 0 0 6px rgba(245,192,74,.10),0 12px 34px rgba(255,153,51,.42),
    0 0 48px rgba(255,205,105,.35)!important;
  animation:enterReveal .75s cubic-bezier(.16,1,.3,1) both,enterShine 3.2s ease-in-out .75s infinite!important;
  transition:transform .2s,box-shadow .2s!important;
}
.st-key-enter button:hover{
  transform:translateY(-5px) scale(1.025)!important;
  box-shadow:0 0 0 8px rgba(245,192,74,.14),0 18px 44px rgba(255,153,51,.58),
    0 0 62px rgba(255,220,130,.55)!important;
}
.st-key-enter button:active{transform:scale(.985)!important;}
.st-key-enter button:focus-visible{outline:3px solid #fff!important;outline-offset:5px!important;}
@keyframes enterReveal{from{opacity:0;transform:translateY(24px) scale(.82);filter:blur(5px)}to{opacity:1;transform:translateY(0) scale(1);filter:blur(0)}}
@keyframes enterShine{0%,100%{background-position:0% 50%;box-shadow:0 0 0 6px rgba(245,192,74,.10),0 12px 34px rgba(255,153,51,.42),0 0 48px rgba(255,205,105,.35)}50%{background-position:100% 50%;box-shadow:0 0 0 9px rgba(245,192,74,.15),0 14px 42px rgba(255,153,51,.58),0 0 62px rgba(255,220,130,.52)}}
@media(max-width:600px){.st-key-enter button{min-height:78px!important;padding:16px 18px!important;letter-spacing:.045em!important}}
@media(prefers-reduced-motion:reduce){.st-key-enter button{animation:none!important}}

/* Custom scrollbar (outer) */
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-track{background:rgba(255,255,255,.04);border-radius:10px}
::-webkit-scrollbar-thumb{background:linear-gradient(#ff9933,#f5c04a);border-radius:10px}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------- shared iframe shell
BASE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Poppins:wght@300;400;600;800&display=swap" rel="stylesheet">
<style>
:root{--gold:#f5c04a;--saf:#ff9933;--org:#ff6a1a;--pur:#2a0f4a;--pink:#ff7eb6;
  --ink:#0a0614;--cream:#fff4d6;--violet:#b980ff}
*{box-sizing:border-box}
html,body{margin:0;background:transparent;color:var(--cream);
  font-family:'Poppins','Segoe UI',sans-serif;overflow-x:hidden;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* layered festival backdrop */
body::before{content:'';position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:
    radial-gradient(circle at 15% 8%,rgba(185,128,255,.18),transparent 42%),
    radial-gradient(circle at 85% 92%,rgba(255,153,51,.14),transparent 48%),
    radial-gradient(circle at 50% 50%,rgba(255,126,182,.08),transparent 62%),
    radial-gradient(ellipse at top,#2a0f4a 0%,#0a0614 78%);}
body::after{content:'';position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.08;
  background-image:repeating-conic-gradient(from 0deg at 50% 50%,
    #f5c04a 0deg 1deg,transparent 1deg 10deg);
  -webkit-mask:radial-gradient(circle at 50% 50%,#000 10%,transparent 70%);
  mask:radial-gradient(circle at 50% 50%,#000 10%,transparent 70%);}

h1,h2,h3{font-family:'Cinzel Decorative',Georgia,serif;margin:.3em 0;color:var(--gold);
  text-shadow:0 0 18px rgba(255,153,51,.7),0 2px 0 rgba(0,0,0,.25);
  letter-spacing:.02em;line-height:1.15}
h1{color:var(--gold)}
@supports ((-webkit-background-clip:text) or (background-clip:text)){
  h1{background:linear-gradient(90deg,#ff9933,#fff1b8,#ff7eb6,#f5c04a,#ff9933);
    background-size:300% 100%;
    -webkit-background-clip:text;background-clip:text;color:transparent;
    animation:titleShine 8s linear infinite;
    filter:drop-shadow(0 0 18px rgba(255,153,51,.55));}
  @keyframes titleShine{to{background-position:300% 0}}
}
::selection{background:rgba(255,153,51,.5);color:#fff}

#bg{position:fixed;inset:0;pointer-events:none;z-index:0}
#cursorGlow{position:fixed;top:0;left:0;width:340px;height:340px;border-radius:50%;
  pointer-events:none;z-index:1;transition:transform .12s ease-out;will-change:transform;
  background:radial-gradient(circle,rgba(255,180,70,.14),
    rgba(255,120,50,.06) 40%,transparent 70%);}

.wrap{position:relative;z-index:2;padding:18px;text-align:center;max-width:1000px;margin:auto;
  animation:pageIn .8s cubic-bezier(.2,.9,.3,1.2) both}
@keyframes pageIn{from{opacity:0;transform:translateY(24px) scale(.98)}to{opacity:1;transform:none}}

/* Glass card with gradient border */
.glass{position:relative;
  background:linear-gradient(135deg,rgba(255,255,255,.09),rgba(255,255,255,.035));
  border:1px solid rgba(245,192,74,.35);border-radius:20px;
  backdrop-filter:blur(14px) saturate(1.2);padding:20px;
  box-shadow:0 8px 40px rgba(0,0,0,.4),inset 0 1px 0 rgba(255,255,255,.12);
  transition:transform .2s,box-shadow .3s,border-color .3s;}
.glass::before{content:'';position:absolute;inset:-1px;border-radius:20px;padding:1px;
  background:linear-gradient(135deg,rgba(245,192,74,.55),transparent 40%,
    transparent 60%,rgba(255,126,182,.45));
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;opacity:.65}

/* Buttons */
.btn{position:relative;overflow:hidden;
  background:linear-gradient(135deg,var(--saf),var(--gold) 50%,#ffcf6b);
  color:var(--pur);font-weight:800;border:0;border-radius:999px;
  padding:14px 28px;font-size:1rem;cursor:pointer;margin:8px;
  transition:transform .2s,box-shadow .3s;font-family:inherit;letter-spacing:.03em;
  box-shadow:0 4px 20px rgba(255,153,51,.35);}
.btn::after{content:'';position:absolute;inset:0;
  background:linear-gradient(120deg,transparent 30%,rgba(255,255,255,.55) 50%,transparent 70%);
  transform:translateX(-120%);transition:transform .7s;}
.btn:hover{transform:translateY(-2px) scale(1.04);
  box-shadow:0 0 30px var(--saf),0 6px 24px rgba(255,153,51,.5);}
.btn:hover::after{transform:translateX(120%);}
.btn:focus-visible{outline:3px solid #fff;outline-offset:3px;}
.btn:disabled{opacity:.55;cursor:not-allowed;transform:none!important;}

.garland{height:34px;margin:4px 0;border-radius:6px;
  background:radial-gradient(circle at 50% 50%,#ffb000 0 5px,#ff7a00 6px 10px,transparent 11px)
    0 0/30px 30px repeat-x;
  filter:drop-shadow(0 2px 6px rgba(255,122,0,.6));}

/* ============ Enhanced Diya ============ */
.diya{width:110px;height:90px;position:relative;margin:auto;
  filter:drop-shadow(0 4px 12px rgba(0,0,0,.5));}
.bowl{position:absolute;bottom:0;left:0;right:0;height:42px;
  background:linear-gradient(180deg,#ff9f3d 0%,#c14b0c 60%,#6b2705 100%);
  border-radius:0 0 100px 100px/0 0 80px 80px;
  box-shadow:0 6px 0 #4a1902,inset 0 -4px 8px rgba(0,0,0,.4),
    inset 0 4px 6px rgba(255,200,120,.3);}
.bowl::before{content:'';position:absolute;top:-3px;left:10%;right:10%;height:6px;
  background:linear-gradient(90deg,transparent,#ffb62e,transparent);
  border-radius:50%;filter:blur(2px);}
.flame{position:absolute;left:50%;bottom:36px;width:22px;height:44px;margin-left:-11px;
  opacity:0;transition:opacity .4s;
  border-radius:50% 50% 50% 50%/62% 62% 38% 38%;
  background:radial-gradient(ellipse at 50% 80%,#fff6c8 0%,#ffb62e 45%,#ff6a1a 85%,transparent 100%);
  filter:drop-shadow(0 0 16px #ffb62e) drop-shadow(0 0 30px #ff6a1a);
  animation:fl .18s infinite alternate;transform-origin:bottom center;}
.flame::before{content:'';position:absolute;inset:20% 30% 10% 30%;
  background:radial-gradient(#fff 20%,transparent 70%);border-radius:50%;
  animation:flicker .3s infinite alternate;}
.lit .flame{opacity:1}
.lit .bowl{box-shadow:0 6px 0 #4a1902,0 0 60px 14px rgba(255,170,50,.55),
  inset 0 -4px 8px rgba(0,0,0,.4),inset 0 4px 6px rgba(255,200,120,.35);}
.diya.big{transform:scale(2);margin:60px auto;}
@keyframes fl{to{transform:scale(1.08,.93) rotate(4deg)}}
@keyframes flicker{to{opacity:.55;transform:scale(.85)}}

@media (prefers-reduced-motion:reduce){
  *{animation-duration:.01s!important;transition-duration:.01s!important}
}

/* Floating lamps in the background */
.ln{position:fixed;bottom:-60px;width:26px;height:34px;
  border-radius:8px 8px 4px 4px;pointer-events:none;z-index:0;
  background:linear-gradient(#ffb62e,#ff6a1a);
  box-shadow:0 0 22px 6px rgba(255,150,40,.6);opacity:.65;
  animation:rise linear infinite;}
@keyframes rise{to{transform:translate(40px,-125vh)}}

/* Scrollbar (iframe) */
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-track{background:rgba(255,255,255,.04);border-radius:10px}
::-webkit-scrollbar-thumb{background:linear-gradient(var(--saf),var(--gold));
  border-radius:10px;border:2px solid transparent;background-clip:content-box}

@media (max-width:600px){
  .wrap{padding:12px}
  h1{font-size:1.4rem!important}
  .diya{transform:scale(.9)}
}
#musicDock{position:fixed;left:14px;bottom:14px;z-index:20;display:flex;align-items:center;
  gap:9px;padding:9px 12px;border:1px solid rgba(245,192,74,.55);border-radius:999px;
  background:rgba(25,10,42,.88);backdrop-filter:blur(12px);
  box-shadow:0 8px 28px rgba(0,0,0,.35),0 0 18px rgba(245,192,74,.16)}
#musicDock button{border:0;border-radius:999px;padding:9px 14px;cursor:pointer;
  color:#2a0f4a;background:linear-gradient(135deg,#ff9933,#f5c04a);
  font:700 .82rem 'Poppins',sans-serif}
#musicDock label{font-size:.65rem;color:#ffe9b0;font-weight:700;letter-spacing:.08em}
#musicVolume{width:76px;accent-color:#f5c04a}
@media(max-width:600px){#musicDock{left:8px;bottom:8px;gap:6px;padding:7px 9px}
  #musicVolume{width:58px}#musicDock button{padding:8px 11px}}
%%CSS%%
</style></head><body><canvas id="bg"></canvas><div id="cursorGlow"></div>
%%MUSIC_PLAYER%%
<div class="wrap">%%BODY%%</div>
<script>
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const pick=a=>a[Math.floor(Math.random()*a.length)];
const cv=$('#bg'),cx=cv.getContext('2d');
let W,H,P=[],F=[],T=[],C=[],S=[],R=[],hook=()=>{};
function rs(){W=cv.width=innerWidth;H=cv.height=innerHeight}
rs();addEventListener('resize',rs);

// Twinkling stars (gold + cream)
for(let i=0;i<90;i++)P.push({
  x:Math.random()*W, y:Math.random()*H,
  r:Math.random()*1.8+.3, v:Math.random()*.4+.1,
  a:Math.random()*6.28,
  c:Math.random()<.5?'#f5c04a':'#fff1b8'
});

// Burst = single firework at (x,y)
function burst(x,y){
  const cs=['#f5c04a','#ff9933','#ff6a1a','#ff7eb6','#fff1b8','#b980ff'];
  const n=80;
  for(let i=0;i<n;i++){
    const a=Math.PI*2*i/n+Math.random()*.12, s=Math.random()*4.5+1.5;
    F.push({x,y,vx:Math.cos(a)*s,vy:Math.sin(a)*s,l:1,c:cs[i%cs.length]});
  }
}
let boom=burst;

function salvo(n){
  for(let i=0;i<n;i++)
    setTimeout(()=>boom(Math.random()*W*.8+W*.1,Math.random()*H*.5+H*.1), i*350);
}

// Main animation loop
(function loop(){
  cx.clearRect(0,0,W,H);
  P.forEach(p=>{
    p.y-=p.v;
    if(p.y<0){p.y=H;p.x=Math.random()*W}
    cx.globalAlpha=.4+.4*Math.sin(Date.now()/500+p.a*6);
    cx.fillStyle=p.c;
    cx.beginPath();cx.arc(p.x,p.y,p.r,0,7);cx.fill();
  });
  F=F.filter(f=>f.l>0);
  F.forEach(f=>{
    f.x+=f.vx;f.y+=f.vy;f.vy+=.05;f.vx*=.985;f.l-=.012;
    cx.globalAlpha=Math.max(f.l,0);
    cx.fillStyle=f.c;
    cx.beginPath();cx.arc(f.x,f.y,2.4,0,7);cx.fill();
  });
  hook();
  requestAnimationFrame(loop);
})();

// Rockets
function launch(x,y){R.push({x:W/2+(Math.random()-.5)*W*.4, y:H, tx:x, ty:y, t:0})}

// Confetti
function confetti(n){
  const c=['#f5c04a','#ff9933','#ff6a1a','#ff7eb6','#b980ff','#fff1b8'];
  for(let i=0;i<(n||120);i++)C.push({
    x:Math.random()*W, y:-20-Math.random()*200,
    vx:Math.random()*2-1, vy:Math.random()*3+2,
    r:Math.random()*6, s:Math.random()*8+4,
    c:c[i%c.length], w:Math.random()*2-.5
  });
}

function shake(){
  document.body.animate(
    [{transform:'translate(7px,-4px)'},{transform:'translate(-7px,4px)'},{transform:'none'}],
    {duration:260,iterations:3}
  );
}

// Click-to-launch (skip interactive elements)
addEventListener('pointerdown',e=>{
  if(e.target.closest('button,[role=button],.diya,.card,canvas#g'))return;
  launch(e.clientX,e.clientY);
});

// Cursor sparkle trail + cursor glow
addEventListener('pointermove',e=>{
  if(Math.random()<.35) T.push({
    x:e.clientX+(Math.random()-.5)*14,
    y:e.clientY+(Math.random()-.5)*14,
    l:1, c:pick(['#f5c04a','#ff9933','#fff1b8'])
  });
  const g=$('#cursorGlow');
  if(g) g.style.transform=`translate(${e.clientX-170}px,${e.clientY-170}px)`;
});

// Shooting stars
setInterval(()=>S.push({
  x:Math.random()*W, y:0,
  vx:-6-Math.random()*4, vy:3+Math.random()*2, l:1
}),3200);

// Per-frame paint hook
hook=()=>{
  R=R.filter(r=>{
    r.t+=.03;
    const k=Math.min(r.t,1),
          x=r.x+(r.tx-r.x)*k,
          y=r.y+(r.ty-r.y)*k;
    T.push({x,y,l:1,c:'#ffd27a'});
    if(r.t>=1){burst(r.tx,r.ty);return false}
    return true;
  });
  T=T.filter(t=>t.l>0);
  T.forEach(t=>{
    t.l-=.05;
    cx.globalAlpha=t.l;cx.fillStyle=t.c;cx.fillRect(t.x,t.y,3,3);
  });
  S=S.filter(s=>s.l>0);
  S.forEach(s=>{
    s.x+=s.vx;s.y+=s.vy;s.l-=.01;
    cx.globalAlpha=s.l;cx.strokeStyle='#fff';
    cx.beginPath();cx.moveTo(s.x,s.y);
    cx.lineTo(s.x-s.vx*5,s.y-s.vy*5);cx.stroke();
  });
  C=C.filter(c=>c.y<H+20);
  C.forEach(c=>{
    c.x+=c.vx;c.y+=c.vy;c.r+=.1;
    cx.globalAlpha=1;cx.fillStyle=c.c;
    cx.save();cx.translate(c.x,c.y);cx.rotate(c.r);
    cx.fillRect(-c.s/2,-c.s/4,c.s,c.s/2);cx.restore();
  });
};

// Background floating lamps
for(let i=0;i<8;i++){
  const d=document.createElement('div');d.className='ln';
  d.style.left=Math.random()*95+'%';
  d.style.animationDuration=(14+Math.random()*12)+'s';
  d.style.animationDelay=(-Math.random()*20)+'s';
  document.body.appendChild(d);
}

// Emoji rain
function rain(em,n){
  for(let i=0;i<n;i++){
    const d=document.createElement('div');d.textContent=pick(em);
    d.style.cssText='position:fixed;top:-40px;left:'+Math.random()*100+
      '%;font-size:'+(18+Math.random()*26)+'px;z-index:5;pointer-events:none;'+
      'transition:transform '+(3+Math.random()*3)+'s linear,opacity 3s linear';
    document.body.appendChild(d);
    requestAnimationFrame(()=>{
      d.style.transform='translateY('+(H+80)+'px) rotate('+
        Math.random()*720+'deg)';
      d.style.opacity='0';
    });
    setTimeout(()=>d.remove(),6500);
  }
}

// Chaos mode
function chaos(){
  salvo(12);confetti(250);shake();
  rain(['🪔','🎆','✨','🍬','🪙','🎇','🎉'],50);
  const e=document.documentElement;
  e.style.transition='filter 1s';
  e.style.filter='hue-rotate(40deg) saturate(1.5)';
  setTimeout(()=>e.style.filter='',5000);
}

// Keyboard easter egg
let kb='';
addEventListener('keydown',e=>{
  kb=(kb+e.key.toLowerCase()).slice(-6);
  if(kb=='diwali')chaos();
});

// Chaos button
const cb=document.createElement('button');
cb.className='btn';cb.textContent='💥 CHAOS MODE';
cb.style.cssText='position:fixed;right:8px;bottom:8px;z-index:9;'+
  'padding:9px 16px;font-size:.75rem;margin:0';
cb.onclick=chaos;
document.body.appendChild(cb);

// 3D tilt on .glass
document.addEventListener('pointermove',e=>{
  const g=e.target.closest&&e.target.closest('.glass');
  $$('.glass').forEach(x=>{if(x!==g)x.style.transform=''});
  if(g){
    const r=g.getBoundingClientRect();
    g.style.transform='perspective(600px) rotateY('+
      ((e.clientX-r.left)/r.width-.5)*10+'deg) rotateX('+
      (-((e.clientY-r.top)/r.height-.5))*10+'deg)';
  }
});

// User-provided background music (assets/diwali.mp3)
const bgMusic=$('#bgMusic');
function updateMusicButtons(){
  const playing=!!(bgMusic && !bgMusic.paused);
  const dockButton=$('#musicToggle');
  if(dockButton)dockButton.textContent=playing?'⏸ Pause music':'▶ Play music';
  $$('#mu').forEach(b=>b.textContent=playing?'⏸ Pause music':'🎵 Play music');
}
async function startOwnMusic(){
  if(!bgMusic || !bgMusic.getAttribute('src'))return false;
  try{
    await bgMusic.play();
    updateMusicButtons();
    return true;
  }catch(e){
    // Browser autoplay policy blocked audible playback. No prompt is shown.
    updateMusicButtons();
    return false;
  }
}
async function toggleOwnMusic(){
  if(!bgMusic || !bgMusic.getAttribute('src')){
    alert('Add your song at assets/diwali.mp3, then restart the app.');
    return;
  }
  if(bgMusic.paused){
    await startOwnMusic();
  }else{
    bgMusic.pause();
  }
  updateMusicButtons();
}
function setOwnMusicVolume(v){
  if(bgMusic)bgMusic.volume=Math.max(0,Math.min(1,Number(v)));
}
if(bgMusic){
  bgMusic.volume=.55;
  bgMusic.addEventListener('play',updateMusicButtons);
  bgMusic.addEventListener('pause',updateMusicButtons);
  bgMusic.addEventListener('ended',updateMusicButtons);
  // Best-effort audible autoplay immediately when the iframe loads.
  // If the browser blocks it, there is deliberately no tap-anywhere prompt.
  window.addEventListener('load',()=>{
    startOwnMusic();
  },{once:true});
}
%%JS%%
</script></body></html>"""

MUSIC_BTN = '<button class="btn" id="mu" onclick="toggleOwnMusic()" style="padding:8px 16px;font-size:.8rem">🎵 Play music</button>'


def show(body, js="", css="", h=640):
    html = BASE.replace("%%CSS%%", css).replace("%%BODY%%", body).replace("%%JS%%", js).replace("%%MUSIC_PLAYER%%", MUSIC_PLAYER)
    for k, v in PH.items():
        html = html.replace(k, v)
    components.html(html, height=h, scrolling=True)


def back_bar():
    c = st.columns([1, 3])
    c[0].button("⬅ Back to festival", key="back", on_click=go, args=("hero",))


DIYA = '<div class="diya %s"><div class="flame"></div><div class="bowl"></div></div>'

# ---------------------------------------------------------------- pages
def intro():
    css = """
    .stage{min-height:min(560px,calc(100svh - 150px));display:flex;flex-direction:column;
      align-items:center;justify-content:center}
    #spark{width:6px;height:6px;border-radius:50%;background:#fff3c0;
      box-shadow:0 0 12px 4px #f5c04a;
      transition:all 3s cubic-bezier(.4,0,.2,1);opacity:0}
    #spark.grow{opacity:1;width:260px;height:260px;
      box-shadow:0 0 140px 80px rgba(255,153,51,.55),
                 0 0 60px 20px rgba(255,240,180,.6)}
    .line{opacity:0;transition:opacity 1s;font-size:1.2rem;margin:6px}
    .line.on{opacity:1}
    #hey{opacity:0;transform:scale(.7);transition:all 1.2s;
      font-size:clamp(2rem,8vw,4.5rem)}
    #hey.on{opacity:1;transform:scale(1)}
    #dv{opacity:0;transition:opacity 1.5s;margin-top:-170px}
    #dv.on{opacity:1}"""
    body = f"""<div class="stage"><div id="spark"></div>
    <div id="dv">{DIYA % 'lit'}</div>
    <div style="margin-top:130px"><div class="line">Lights are ready...</div>
    <div class="line">Fireworks are ready...</div>
    <div class="line">Sweets are probably ready too...</div>
    <h1 id="hey">HEY %%HEYU%%! 🪔</h1>
    <p class="line" id="sub" style="font-size:1.3rem">Your personal Diwali surprise is here!</p></div></div>"""
    js = """
    const L=$$('.line');
    setTimeout(()=>$('#spark').classList.add('grow'),400);
    setTimeout(()=>$('#dv').classList.add('on'),2600);
    L.slice(0,3).forEach((l,i)=>setTimeout(()=>l.classList.add('on'),3400+i*1200));
    setTimeout(()=>{
      L.slice(0,3).forEach(l=>l.style.display='none');
      $('#hey').classList.add('on');
      salvo(3);
    },7400);
    setTimeout(()=>$('#sub').classList.add('on'),8600);"""
    show(body, js, css, 560)
    st.button("ENTER THE FESTIVE WORLD ✨", key="enter", on_click=go, args=("hero",))


def hero():
    body = f"""<div class="garland"></div>
    <h1 style="font-size:clamp(1.5rem,5vw,3rem)">A Festival Full of Lights, Laughter &amp; Good Vibes!</h1>
    <p style="font-size:1.2rem">Welcome to your little Diwali celebration%%COMMA%%.</p>
    {DIYA % 'lit big'}
    <button class="btn" onclick="salvo(5)">Fireworks! 🎆</button>{MUSIC_BTN}
    <p>Tap anywhere for a rocket 🚀 and wave your cursor around!
    Type <b>diwali</b> or hit CHAOS MODE for a surprise.</p>"""
    show(body, "salvo(4);confetti(80);setInterval(()=>salvo(2),6000);", "", 500)
    cols = st.columns(5)
    items = [("Dhanteras Treasure 🪙", "treasure"), ("Seven Days of Diwali 🪔", "days"),
             ("Light Up the Diyas ✨", "diyas"), ("Festival Fun Zone 🎉", "fun"),
             ("Final Celebration 🎆", "finale")]
    for c, (label, p) in zip(cols, items):
        c.button(label, key="nav_" + p, on_click=go, args=(p,))
    c1, c2 = st.columns(2)
    c1.button("🎮 Sweet Catch Game", key="nav_game", on_click=go, args=("game",))
    c2.button("📜 Read the little festive note", key="nav_note", on_click=go, args=("note",))
    d1, d2, d3 = st.columns(3)
    d1.button("🧠 Memory Match", key="nav_mem", on_click=go, args=("memory",))
    d2.button("🎨 Rangoli Painter", key="nav_rg", on_click=go, args=("rangoli",))
    d3.button("💥 Cracker Pop", key="nav_pop", on_click=go, args=("pop",))


def treasure():
    back_bar()
    css = """
    .chest{position:relative;width:220px;height:150px;margin:60px auto 20px}
    .base{position:absolute;bottom:0;width:100%;height:95px;
      background:linear-gradient(#b8770f,#6e3f06);
      border:4px solid var(--gold);border-radius:6px 6px 14px 14px;
      box-shadow:inset 0 -6px 12px rgba(0,0,0,.5)}
    .lid{position:absolute;top:0;width:100%;height:60px;
      background:linear-gradient(#d99a1f,#8a5208);
      border:4px solid var(--gold);border-radius:60px 60px 4px 4px;
      transform-origin:top left;
      transition:transform 1s cubic-bezier(.3,1.4,.5,1);}
    .open .lid{transform:rotate(-65deg) translateY(-20px)}
    .glow{position:absolute;left:10%;width:80%;top:50px;height:20px;
      border-radius:50%;opacity:0;transition:1s;
      background:#ffe08a;box-shadow:0 0 80px 40px #ffb62e;}
    .open .glow{opacity:1}
    .coin{position:absolute;left:50%;top:60px;width:26px;height:26px;
      border-radius:50%;z-index:3;
      background:radial-gradient(#fff2a8,#e8a817);
      border:2px solid #b87a0a;
      animation:burst 1.4s ease-out forwards}
    @keyframes burst{to{transform:translate(var(--dx),var(--dy)) rotate(720deg);opacity:0}}
    #big{width:90px;height:90px;border-radius:50%;margin:20px auto;
      cursor:pointer;font-size:2.4rem;font-weight:800;
      background:radial-gradient(#fff2a8,#e8a817);
      border:4px solid #b87a0a;color:#8a5208;
      transition:.3s;animation:pulse 2s infinite;
      display:flex;align-items:center;justify-content:center;
      user-select:none}
    #big:hover{transform:rotateY(180deg) scale(1.1)}
    @keyframes pulse{50%{box-shadow:0 0 40px 10px #ffb62e}}
    #msg{opacity:0;transition:opacity 1.2s;font-size:1.25rem}
    #msg.on{opacity:1}"""
    body = """<h1>Dhanteras Treasure 🪙</h1>
    <div class="chest" id="ch"><div class="glow"></div>
    <div class="base"></div><div class="lid"></div></div>
    <button class="btn" id="ob" onclick="openT()">OPEN TREASURE</button>
    <div class="glass" id="msg">May this Dhanteras bring you prosperity, success,
    good health, and countless reasons to celebrate!</div>
    <p>Tap the golden coin for a wish:</p>
    <div id="big" role="button" tabindex="0">₹</div>
    <div class="glass" id="w" style="min-height:70px;font-size:1.1rem">
    Your wish will appear here ✨</div>"""
    js = """
    const wishes=[
      "May your wallet be as full as your plate during Diwali!",
      "May every coin you touch turn into a good memory!",
      "May your year be golden, minus the price hikes!",
      "May luck knock on your door and refuse to leave!",
      "May your savings grow faster than the sweet box empties!",
      "May good health be your biggest treasure!"
    ];
    function openT(){
      $('#ch').classList.add('open');
      $('#ob').disabled=true;$('#ob').textContent='Treasure opened!';
      const ch=$('#ch');
      for(let i=0;i<32;i++){
        const c=document.createElement('div');c.className='coin';
        c.style.setProperty('--dx',(Math.random()*400-200)+'px');
        c.style.setProperty('--dy',(Math.random()*-260-30)+'px');
        c.style.animationDelay=Math.random()*.4+'s';
        ch.appendChild(c);
        setTimeout(()=>c.remove(),2200);
      }
      salvo(3);confetti(100);shake();
      setTimeout(()=>$('#msg').classList.add('on'),900);
    }
    function wish(){$('#w').textContent=pick(wishes);boom(W/2,H/3)}
    $('#big').onclick=wish;
    $('#big').onkeydown=e=>{if(e.key==='Enter'||e.key===' ')wish()};"""
    show(body, js, css, 860)


def days():
    back_bar()
    css = """.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
    .card{cursor:pointer;text-align:left;transition:.3s;
      border:1px solid rgba(245,192,74,.4);color:inherit;font-family:inherit}
    .card:hover{transform:translateY(-4px);
      box-shadow:0 0 24px rgba(255,153,51,.5)}
    .card b{color:var(--gold);font-size:1.05rem}
    .m{max-height:0;overflow:hidden;opacity:0;transition:all .7s;margin-top:0}
    .card.on .m{max-height:140px;opacity:1;margin-top:10px}
    .card.on{background:rgba(255,153,51,.18)}"""
    D = [("Day 1 — Dhanteras", "May your life be filled with prosperity and opportunities."),
         ("Day 2 — Choti Diwali", "May all negativity disappear and positive vibes take over!"),
         ("Day 3 — Diwali", "May your home shine with happiness, laughter, and beautiful memories."),
         ("Day 4 — Govardhan Puja", "Wishing you strength, blessings, and good fortune."),
         ("Day 5 — Bhai Dooj", "May your family bonds always remain strong and joyful."),
         ("Day 6 — Festival Vibes", "May you get unlimited happiness and unlimited holidays!"),
         ("Day 7 — The Grand Finale", "May the coming year be full of achievements and exciting adventures.")]
    cards = "".join(
        f'<button class="glass card" onclick="t(this)"><b>{a}</b><div class="m">{b}</div></button>'
        for a, b in D
    )
    body = f'<h1>Seven Days of Diwali 🪔</h1><p>Tap a day to reveal its wish.</p><div class="grid">{cards}</div>'
    js = ("function t(e){e.classList.toggle('on');"
          "if(e.classList.contains('on')){"
          "const r=e.getBoundingClientRect();boom(r.left+r.width/2,r.top)}}")
    show(body, js, css, 760)


def diyas():
    back_bar()
    css = """.row{display:flex;flex-wrap:wrap;justify-content:center;gap:26px;margin:40px 0}
    .row .diya{cursor:pointer;transition:.3s}
    .row .diya:hover{transform:scale(1.12)}"""
    body = """<h1>Light Up the Diyas ✨</h1>
    <p>Tap each diya to light it. <b id="c">0 / 7</b></p>
    <div class="row" id="row"></div>
    <div class="glass" id="m" style="min-height:70px;font-size:1.15rem">
    Tap a diya to begin.</div>"""
    js = """
    const M=[
      "Good vibes loading... 100%!",
      "Today's forecast: sweets with a chance of fireworks.",
      "You make every room brighter.",
      "Success is heading your way. Keep the door open!",
      "Smiles are free. Spread them like diyas.",
      "Your sparkle is officially on trend.",
      "Peak festive energy detected!"
    ];
    let n=0;
    for(let i=0;i<7;i++){
      const d=document.createElement('div');
      d.className='diya';d.tabIndex=0;
      d.innerHTML='<div class="flame"></div><div class="bowl"></div>';
      const f=()=>{
        if(d.classList.contains('lit'))return;
        d.classList.add('lit');n++;
        $('#c').textContent=n+' / 7';
        const r=d.getBoundingClientRect();
        boom(r.left+55,r.top);
        $('#m').textContent = n==7
          ? "Congratulations! You just upgraded this website's brightness by 1000%!"
          : pick(M);
        if(n==7){
          salvo(6);confetti(200);shake();
          document.body.style.filter='brightness(1.25)';
        }
      };
      d.onclick=f;
      d.onkeydown=e=>{if(e.key==='Enter'||e.key===' ')f()};
      $('#row').appendChild(d);
    }"""
    show(body, js, css, 640)


def fun():
    back_bar()
    css = """.q button{display:block;width:100%;margin:6px 0;padding:12px;
      border-radius:12px;border:1px solid rgba(245,192,74,.5);
      background:rgba(255,255,255,.08);color:inherit;
      font-family:inherit;cursor:pointer;font-size:1rem;
      transition:background .2s,transform .15s}
    .q button:hover{background:rgba(255,153,51,.3);transform:translateY(-1px)}
    .sec{margin:18px 0}"""
    body = """<h1>Festival Fun Zone 🎉</h1>
    <div class="glass sec"><button class="btn" onclick="salvo(8)">MAKE SOME NOISE! 🎆</button></div>
    <div class="glass sec"><button class="btn" onclick="$('#w').textContent=pick(WI);boom(W/2,H/4)">SURPRISE ME!</button>
      <p id="w" style="font-size:1.15rem">Press the button for a random wish.</p></div>
    <div class="glass sec"><button class="btn" onclick="$('#md').textContent=pick(MO);boom(W/2,H/4)">Generate my Diwali mood</button>
      <h3 id="md">Your mood: ???</h3></div>
    <div class="glass sec q" id="qz"></div>"""
    js = """
    const WI=[
      "May your sweets be endless and your diet be on holiday!",
      "May your phone camera survive all the festive photos!",
      "May your diyas stay lit and your WiFi stay strong!",
      "May the only crackers around you be the fireworks!",
      "May your leftovers outlast your willpower!",
      "May all your Mondays feel like Diwali holidays!"
    ];
    const MO=[
      "Sweets Overload Mode 🍬","Fireworks Enthusiast 🎆",
      "Professional Diya Lighter 🪔","Festival Photography Expert 📸",
      "Holiday Enjoyment Specialist 🏖️"
    ];
    const Q=[
      ["Which sweet is a Diwali classic?",["Kaju Katli","Plain boiled rice","Raw onion"],0],
      ["Diwali is known as the festival of...",["Snow","Lights","Sand"],1],
      ["What do we light in rows at home?",["Diyas","Candles shaped like pizza","Ice cubes"],0],
      ["Dhanteras is the day for...",["Ignoring prosperity","Welcoming prosperity","Sleeping through the festival"],1],
      ["Best way to handle the sweet box?",["Share generously (and sneak one)","Hide it forever","Give it to the fireworks"],0]
    ];
    let qi=0,sc=0;
    function qr(){
      const z=$('#qz');
      if(qi>=Q.length){
        const r = sc==5 ? "Diwali Legend! Sweets are on you."
                : sc>=3 ? "Festival Pro! Almost perfect."
                : "Festival Rookie, but the sweets still love you!";
        z.innerHTML='<h3>Quiz done! Score: '+sc+'/5</h3><p>'+r+
          '</p><button class="btn" onclick="qi=0;sc=0;qr()">Play again</button>';
        salvo(5);return;
      }
      const q=Q[qi];
      z.innerHTML='<h3>Question '+(qi+1)+' of 5</h3><p>'+q[0]+'</p>';
      q[1].forEach((o,i)=>{
        const b=document.createElement('button');
        b.textContent=o;
        b.onclick=()=>{if(i==q[2])sc++;qi++;qr()};
        z.appendChild(b);
      });
    }
    qr();"""
    show(body, js, css, 1250)


def note():
    back_bar()
    css = """.card{max-width:640px;margin:30px auto;text-align:left;line-height:1.8;
      font-size:1.08rem;border:2px solid var(--gold)}"""
    body = """<div class="garland"></div>
    <h1>A Little Festive Note</h1>
    <div class="glass card">
    <p>Hey %%HEY%%!</p>
    <p>Just dropping by with a little digital Diwali surprise!</p>
    <p>Hope this festive season brings you loads of happiness, success, good health,
    delicious sweets, amazing memories, and plenty of reasons to smile.</p>
    <p>May your Diwali be prosperous and your Diwali week be full of fun,
    laughter, and positive vibes.</p>
    <p>Keep shining and keep being awesome!</p>
    <p>Wishing you a very Happy Diwali and a fantastic Diwali week!</p>
    <p><b>Happy Diwali! 🪔✨</b></p></div>
    <div class="garland"></div>"""
    show(body, "salvo(2)", css, 900)


def finale():
    css = """.rg{position:fixed;width:360px;height:360px;border-radius:50%;
      opacity:.4;z-index:0;animation:spin 40s linear infinite;
      background:repeating-conic-gradient(#ff9933 0 8deg,#2a0f4a 8deg 16deg);
      -webkit-mask:radial-gradient(circle,transparent 25%,#000 26% 60%,transparent 61%);
      mask:radial-gradient(circle,transparent 25%,#000 26% 60%,transparent 61%)}
    @keyframes spin{to{transform:rotate(360deg)}}
    .stage{min-height:600px;display:flex;flex-direction:column;
      justify-content:center;align-items:center}
    .big{font-size:clamp(1.8rem,7vw,4rem);
      background:linear-gradient(90deg,#ff9933,#fff1b8,#ff7eb6,#f5c04a,#ff9933);
      background-size:300%;-webkit-background-clip:text;background-clip:text;
      color:transparent;animation:sh 4s linear infinite;text-shadow:none}
    @keyframes sh{to{background-position:300%}}
    .row{display:flex;gap:30px;justify-content:center;margin-top:60px}
    .fade{opacity:0;transition:opacity 1.5s}
    .fade.on{opacity:1}"""
    body = f"""<div class="rg" style="left:-120px;top:-120px"></div>
    <div class="rg" style="right:-120px;bottom:-120px"></div>
    <div class="stage">
    <h1 class="big">LET THE FESTIVAL OF LIGHTS BEGIN!</h1>
    <h2 class="fade" id="a" style="font-size:clamp(1.2rem,4vw,2.2rem)">
    HAPPY DHANTERAS &amp; HAPPY DIWALI WEEK%%COMMAU%%! 🪔🎆</h2>
    <p class="fade" id="b" style="font-size:1.3rem">
    Stay awesome, keep smiling, and enjoy all the sweets!</p>
    <div class="row">{DIYA % 'lit'}{DIYA % 'lit'}{DIYA % 'lit'}{DIYA % 'lit'}{DIYA % 'lit'}</div>
    {MUSIC_BTN}</div>"""
    js = ("salvo(8);confetti(220);"
          "setInterval(()=>{salvo(5);confetti(80);shake()},5000);"
          "setTimeout(()=>$('#a').classList.add('on'),1500);"
          "setTimeout(()=>$('#b').classList.add('on'),3000);")
    show(body, js, css, 680)
    st.markdown('<div class="cta">', unsafe_allow_html=True)
    st.button("EXPERIENCE IT AGAIN ✨", key="again", on_click=go, args=("intro",))
    st.markdown("</div>", unsafe_allow_html=True)
    st.button("⬅ Back to festival", key="back_f", on_click=go, args=("hero",))


def game():
    back_bar()
    css = """#g{width:100%;max-width:700px;border-radius:18px;
      border:2px solid var(--gold);touch-action:none;
      background:linear-gradient(#1b0a33,#0a0614)}"""
    body = """<h1>Sweet Catch 🧺</h1>
    <p>Move your mouse or finger to catch sweets 🍡 (+1), coins 🪙 (+2) and diyas 🪔 (+3).
    Dodge the crackers 💥 (-3)! You get 30 seconds.</p>
    <canvas id="g"></canvas><br>
    <button class="btn" id="go" onclick="start()">START GAME</button>
    <div class="glass" id="r" style="min-height:60px">Ready when you are!</div>"""
    js = """
    const g=$('#g'),gx=g.getContext('2d');
    g.width=700;g.height=420;
    let run=false,sc=0,tl=30,bx=350,I=[],hi=0,lt;
    const K=[['🍡',1],['🪔',3],['🪙',2],['💥',-3]];
    g.addEventListener('pointermove',e=>{
      const r=g.getBoundingClientRect();
      bx=(e.clientX-r.left)*700/r.width;
    });
    function start(){
      run=true;sc=0;tl=30;I=[];
      $('#go').disabled=true;$('#r').textContent='Go go go!';
      lt=setInterval(()=>{tl--;if(tl<=0)end()},1000);
    }
    function end(){
      run=false;clearInterval(lt);
      $('#go').disabled=false;hi=Math.max(hi,sc);
      confetti(160);salvo(4);
      $('#r').textContent='Score: '+sc+' | '+
        (sc>=40 ? 'Diwali Champion! Sweets are on you.'
                : sc>=20 ? 'Sweet Master! Impressive.'
                : 'Warm-up round, hit start again!');
    }
    function spawn(){
      const r=Math.random();
      I.push({x:Math.random()*660+20,y:-20,v:2+Math.random()*2+(30-tl)*.06,
        k:r<.5?0:r<.7?1:r<.9?2:3});
    }
    (function gl(){
      gx.clearRect(0,0,700,420);gx.textAlign='center';
      if(run&&Math.random()<.07+(30-tl)*.003)spawn();
      I=I.filter(i=>{
        i.y+=i.v;
        if(run&&i.y>370&&i.y<405&&Math.abs(i.x-bx)<50){
          sc+=K[i.k][1];
          const r=g.getBoundingClientRect();
          if(K[i.k][1]<0)shake();
          else if(i.k>0)boom(r.left+i.x*r.width/700,r.top+i.y*r.height/420);
          return false;
        }
        return i.y<440;
      });
      gx.font='32px serif';I.forEach(i=>gx.fillText(K[i.k][0],i.x,i.y));
      gx.font='44px serif';gx.fillText('🧺',bx,410);
      gx.font='bold 20px sans-serif';gx.fillStyle='#ffe9b0';
      gx.fillText('Score '+sc+'   Time '+tl+'   Best '+hi,350,28);
      requestAnimationFrame(gl);
    })();"""
    show(body, js, css, 820)


def memory():
    back_bar()
    css = """.gr{display:grid;grid-template-columns:repeat(4,1fr);
      gap:10px;max-width:420px;margin:20px auto}
    .mc{height:80px;font-size:2rem;border-radius:14px;
      border:1px solid var(--gold);cursor:pointer;color:#fff;
      background:linear-gradient(135deg,#2a0f4a,#6b2a9a);
      transition:all .3s}
    .mc.up{background:rgba(255,153,51,.35);transform:rotateY(360deg)}"""
    body = """<h1>Memory Match 🧠</h1>
    <p>Find all six pairs. Moves: <b id="mv">0</b></p>
    <div class="gr" id="gr"></div>
    <button class="btn" onclick="init()">Shuffle &amp; restart</button>
    <div class="glass" id="r" style="min-height:50px">Flip two cards!</div>"""
    js = """
    const E=['🪔','🍬','🎆','🪙','🌼','🎇'];
    let a=[],lock=false,mv=0,got=0;
    function init(){
      const d=[...E,...E].sort(()=>Math.random()-.5);
      mv=0;got=0;a=[];lock=false;
      $('#mv').textContent=0;$('#gr').innerHTML='';
      d.forEach(e=>{
        const b=document.createElement('button');
        b.className='mc';b.dataset.e=e;
        b.setAttribute('aria-label','Memory card');
        b.onclick=()=>flip(b);
        $('#gr').appendChild(b);
      });
    }
    function flip(b){
      if(lock||b.classList.contains('up'))return;
      b.classList.add('up');b.textContent=b.dataset.e;
      a.push(b);
      if(a.length==2){
        mv++;$('#mv').textContent=mv;
        const[x,y]=a;a=[];
        if(x.dataset.e==y.dataset.e){
          got++;
          const r=x.getBoundingClientRect();boom(r.left,r.top);
          if(got==6){
            chaos();
            $('#r').textContent='Solved in '+mv+' moves! Memory of a Diwali legend.';
          }
        }else{
          lock=true;
          setTimeout(()=>{
            [x,y].forEach(c=>{c.classList.remove('up');c.textContent=''});
            lock=false;
          },800);
        }
      }
    }
    init();"""
    show(body, js, css, 780)


def rangoli():
    back_bar()
    css = """#g{width:100%;max-width:500px;border-radius:50%;
      border:3px solid var(--gold);touch-action:none;cursor:crosshair;
      background:radial-gradient(#2a0f4a,#0a0614);
      box-shadow:0 0 40px rgba(255,153,51,.3),inset 0 0 60px rgba(255,153,51,.15)}"""
    body = """<h1>Rangoli Painter 🎨</h1>
    <p>Draw anywhere: every stroke is mirrored 16 ways into a rangoli!</p>
    <canvas id="g"></canvas>
    <div id="pal"></div>
    <button class="btn" onclick="magic()">✨ Magic rangoli</button>
    <button class="btn" onclick="clr()">Clear</button>"""
    js = """
    const g=$('#g'),x=g.getContext('2d');
    g.width=g.height=500;
    let col='#f5c04a',dn=false,lp=null;
    const cs=['#f5c04a','#ff9933','#ff6a1a','#ff7eb6','#b980ff','#ffffff'];
    cs.forEach(c=>{
      const b=document.createElement('button');
      b.style.cssText='width:36px;height:36px;border-radius:50%;margin:4px;'+
        'border:2px solid #fff;cursor:pointer;background:'+c+
        ';box-shadow:0 0 10px '+c;
      b.setAttribute('aria-label','Colour '+c);
      b.onclick=()=>col=c;
      $('#pal').appendChild(b);
    });
    function pt(e){
      const r=g.getBoundingClientRect();
      return[(e.clientX-r.left)*500/r.width-250,
             (e.clientY-r.top)*500/r.height-250];
    }
    function seg(p,q){
      x.strokeStyle=col;x.lineWidth=3;x.lineCap='round';
      x.shadowColor=col;x.shadowBlur=8;
      for(let i=0;i<8;i++){
        x.save();x.translate(250,250);x.rotate(i*Math.PI/4);
        for(let m=0;m<2;m++){
          x.beginPath();
          x.moveTo(p[0],m?-p[1]:p[1]);
          x.lineTo(q[0],m?-q[1]:q[1]);
          x.stroke();
        }
        x.restore();
      }
    }
    g.onpointerdown=e=>{dn=true;lp=pt(e);g.setPointerCapture(e.pointerId)};
    g.onpointermove=e=>{if(!dn)return;const p=pt(e);seg(lp,p);lp=p};
    g.onpointerup=()=>dn=false;
    function clr(){x.clearRect(0,0,500,500)}
    function magic(){
      clr();let t=0;
      const id=setInterval(()=>{
        col=pick(cs);
        const a=t*.3,r=30+t*1.5,
              p=[Math.cos(a)*r,Math.sin(a)*r],
              q=[Math.cos(a+.3)*(r+1.5),Math.sin(a+.3)*(r+1.5)];
        seg(p,q);
        if(++t>140){clearInterval(id);salvo(3)}
      },12);
    }"""
    show(body, js, css, 880)


def pop():
    back_bar()
    css = """.gr{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;
      max-width:360px;margin:20px auto}
    .ho{height:100px;font-size:2.6rem;border-radius:50%;cursor:pointer;
      border:3px solid #6b2705;color:#fff;
      background:radial-gradient(circle at 50% 30%,#4a2010,#150a04 70%);
      box-shadow:inset 0 6px 12px rgba(0,0,0,.8),0 4px 0 #6b2705;
      transition:transform .15s}
    .ho:hover{transform:translateY(-2px)}
    .ho:active{transform:translateY(2px)}"""
    body = """<h1>Cracker Pop 💥</h1>
    <p>Pop the crackers 🎆 (+1) and golden coins 🪙 (+3) as they appear! Faster and faster...</p>
    <p>Score <b id="s">0</b> | Time <b id="t">30</b></p>
    <div class="gr" id="gr"></div>
    <button class="btn" id="go" onclick="start()">START</button>
    <div class="glass" id="r" style="min-height:50px">Ready?</div>"""
    js = """
    let sc=0,tl=30,run=false,tmr,ti,cur=-1;
    const HO=[];
    for(let i=0;i<9;i++){
      const b=document.createElement('button');
      b.className='ho';b.setAttribute('aria-label','Hole '+(i+1));
      b.onclick=()=>hit(i);
      $('#gr').appendChild(b);HO.push(b);
    }
    function show(){
      if(!run)return;
      HO.forEach(h=>h.textContent='');
      cur=Math.floor(Math.random()*9);
      const k=Math.random()<.2?['🪙',3]:['🎆',1];
      HO[cur].textContent=k[0];HO[cur].dataset.p=k[1];
      ti=setTimeout(show,Math.max(350,900-(30-tl)*18));
    }
    function hit(i){
      if(!run||i!=cur||!HO[i].textContent||HO[i].textContent=='💥')return;
      sc+=+HO[i].dataset.p;$('#s').textContent=sc;
      HO[i].textContent='💥';
      const r=HO[i].getBoundingClientRect();
      boom(r.left+r.width/2,r.top);
    }
    function start(){
      run=true;sc=0;tl=30;
      $('#s').textContent=0;$('#go').disabled=true;
      $('#r').textContent='Pop pop pop!';
      show();
      tmr=setInterval(()=>{
        $('#t').textContent=--tl;
        if(tl<=0){
          run=false;clearInterval(tmr);clearTimeout(ti);
          HO.forEach(h=>h.textContent='');
          $('#go').disabled=false;confetti(160);salvo(5);
          $('#r').textContent='Final score: '+sc+
            (sc>=35?' | Cracker King/Queen!':sc>=20?' | Pro popper!':' | Try again!');
        }
      },1000);
    }"""
    show(body, js, css, 860)

# ---------------------------------------------------------------- router
{"intro": intro, "hero": hero, "treasure": treasure, "days": days, "diyas": diyas,
 "fun": fun, "note": note, "finale": finale, "game": game, "memory": memory,
 "rangoli": rangoli, "pop": pop}[st.session_state.page]()