# """Divya's Diwali Festival Experience - a single-file Streamlit app."""
# import streamlit as st
# import streamlit.components.v1 as components

# st.set_page_config(page_title="Divya's Diwali 🪔", page_icon="🪔", layout="wide")

# PAGES = ["intro", "hero", "treasure", "days", "diyas", "fun", "note", "finale"]
# if "page" not in st.session_state:
#     st.session_state.page = "intro"


# def go(p):
#     st.session_state.page = p


# # ---------------------------------------------------------------- styling
# st.markdown("""
# <style>
# #MainMenu, header, footer {visibility:hidden;}
# .stApp {background:radial-gradient(ellipse at top,#2a0f4a 0%,#0a0614 70%);}
# .block-container {padding:0.5rem 1rem 2rem; max-width:1200px;}
# iframe {border:0; border-radius:18px;}
# .stButton>button {
#   width:100%; min-height:64px; border-radius:16px; color:#ffe9b0; font-weight:600;
#   background:rgba(255,255,255,.07); border:1px solid rgba(245,192,74,.45);
#   backdrop-filter:blur(10px); transition:all .25s; white-space:normal;
# }
# .stButton>button:hover {transform:translateY(-4px); border-color:#f5c04a;
#   box-shadow:0 0 26px rgba(255,153,51,.55); color:#fff;}
# .stButton>button:focus-visible {outline:3px solid #f5c04a;}
# .cta .stButton>button {background:linear-gradient(90deg,#ff9933,#f5c04a); color:#2a0f4a;
#   font-size:1.1rem; font-weight:800; letter-spacing:.04em;}
# </style>
# """, unsafe_allow_html=True)

# # ---------------------------------------------------------------- shared iframe shell
# BASE = """<!doctype html><html><head><meta charset="utf-8">
# <meta name="viewport" content="width=device-width,initial-scale=1">
# <style>
# :root{--gold:#f5c04a;--saf:#ff9933;--org:#ff6a1a;--pur:#2a0f4a;--pink:#ff7eb6;--ink:#0a0614}
# *{box-sizing:border-box}
# html,body{margin:0;background:transparent;color:#fff4d6;font-family:'Poppins','Segoe UI',sans-serif;overflow-x:hidden}
# h1,h2,h3{font-family:'Cinzel Decorative',Georgia,serif;margin:.3em 0;color:var(--gold);text-shadow:0 0 18px rgba(255,153,51,.7)}
# #bg{position:fixed;inset:0;pointer-events:none;z-index:0}
# .wrap{position:relative;z-index:1;padding:18px;text-align:center;max-width:1000px;margin:auto}
# .glass{background:rgba(255,255,255,.07);border:1px solid rgba(245,192,74,.4);border-radius:20px;
#   backdrop-filter:blur(12px);padding:20px;box-shadow:0 8px 40px rgba(0,0,0,.4)}
# .btn{background:linear-gradient(90deg,var(--saf),var(--gold));color:var(--pur);font-weight:800;border:0;
#   border-radius:999px;padding:14px 26px;font-size:1rem;cursor:pointer;margin:8px;transition:.2s;font-family:inherit}
# .btn:hover{transform:scale(1.06);box-shadow:0 0 26px var(--saf)}
# .btn:focus-visible{outline:3px solid #fff}
# .garland{height:30px;background:radial-gradient(circle at 50% 50%,#ffb000 0 6px,#ff7a00 7px 11px,transparent 12px) 0 0/30px 30px repeat-x}
# .diya{width:90px;height:70px;position:relative;margin:auto}
# .bowl{position:absolute;bottom:0;width:90px;height:34px;background:linear-gradient(#ff9933,#a33f08);border-radius:0 0 90px 90px;box-shadow:0 6px 0 #6b2705}
# .flame{position:absolute;left:50%;bottom:30px;width:18px;height:36px;margin-left:-9px;opacity:0;transition:opacity .4s;
#   border-radius:50% 50% 50% 50%/62% 62% 38% 38%;background:radial-gradient(#fff6c8,#ffb62e 60%,#ff6a1a);
#   filter:drop-shadow(0 0 14px #ffb62e);animation:fl .15s infinite alternate}
# .lit .flame{opacity:1}
# .lit .bowl{box-shadow:0 6px 0 #6b2705,0 0 60px 14px rgba(255,170,50,.55)}
# .diya.big{transform:scale(2);margin:50px auto}
# @keyframes fl{to{transform:scale(1.1,.92) rotate(4deg)}}
# @media (prefers-reduced-motion:reduce){*{animation-duration:.01s!important}}
# %%CSS%%
# </style></head><body><canvas id="bg"></canvas>
# <div class="wrap">%%BODY%%</div>
# <script>
# const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
# const pick=a=>a[Math.floor(Math.random()*a.length)];
# const cv=$('#bg'),cx=cv.getContext('2d');let W,H,P=[],F=[];
# function rs(){W=cv.width=innerWidth;H=cv.height=innerHeight}rs();addEventListener('resize',rs);
# for(let i=0;i<60;i++)P.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*2+.5,v:Math.random()*.6+.2,a:Math.random()});
# function boom(x,y){const c=['#f5c04a','#ff9933','#ff6a1a','#ff7eb6','#fff1b8'];
#   for(let i=0;i<70;i++){const a=Math.PI*2*i/70,s=Math.random()*4+1.5;F.push({x,y,vx:Math.cos(a)*s,vy:Math.sin(a)*s,l:1,c:c[i%5]})}}
# function salvo(n){for(let i=0;i<n;i++)setTimeout(()=>boom(Math.random()*W*.8+W*.1,Math.random()*H*.5+H*.1),i*350)}
# (function loop(){cx.clearRect(0,0,W,H);
#   P.forEach(p=>{p.y-=p.v;if(p.y<0){p.y=H;p.x=Math.random()*W}cx.globalAlpha=.4+.4*Math.sin(Date.now()/500+p.a*6);
#     cx.fillStyle='#f5c04a';cx.beginPath();cx.arc(p.x,p.y,p.r,0,7);cx.fill()});
#   F=F.filter(f=>f.l>0);F.forEach(f=>{f.x+=f.vx;f.y+=f.vy;f.vy+=.05;f.vx*=.985;f.l-=.012;
#     cx.globalAlpha=Math.max(f.l,0);cx.fillStyle=f.c;cx.beginPath();cx.arc(f.x,f.y,2.2,0,7);cx.fill()});
#   requestAnimationFrame(loop)})();
# /* music: synthesised with WebAudio, so there are no audio files that can go missing */
# let AC,mOn=false,tm,step=0;const N=[392,440,494,587,659,587,494,440];
# function tone(f,d){const t=AC.currentTime,o=AC.createOscillator(),g=AC.createGain();o.type='triangle';o.frequency.value=f;
#   g.gain.setValueAtTime(.0001,t);g.gain.exponentialRampToValueAtTime(.07,t+.05);g.gain.exponentialRampToValueAtTime(.0001,t+d);
#   o.connect(g);g.connect(AC.destination);o.start(t);o.stop(t+d)}
# function tick(){if(!mOn)return;tone(N[step%8]*(step%16<8?1:.75),.9);step++;tm=setTimeout(tick,450)}
# function music(){const b=$('#mu');try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();mOn=!mOn;
#   if(mOn){AC.resume();tick()}else clearTimeout(tm);b.textContent=mOn?'⏸ Pause music':'🎵 Play music'}
#   catch(e){b.textContent='Audio unavailable';b.disabled=true}}
# %%JS%%
# </script></body></html>"""

# MUSIC_BTN = '<button class="btn" id="mu" onclick="music()" style="padding:8px 16px;font-size:.8rem">🎵 Play music</button>'


# def show(body, js="", css="", h=640):
#     html = BASE.replace("%%CSS%%", css).replace("%%BODY%%", body).replace("%%JS%%", js)
#     components.html(html, height=h, scrolling=True)


# def back_bar():
#     c = st.columns([1, 3])
#     c[0].button("⬅ Back to festival", key="back", on_click=go, args=("hero",))


# DIYA = '<div class="diya %s"><div class="flame"></div><div class="bowl"></div></div>'

# # ---------------------------------------------------------------- pages
# def intro():
#     css = """
#     .stage{min-height:600px;display:flex;flex-direction:column;align-items:center;justify-content:center}
#     #spark{width:6px;height:6px;border-radius:50%;background:#fff3c0;box-shadow:0 0 12px 4px #f5c04a;
#       transition:all 3s ease;opacity:0}
#     #spark.grow{opacity:1;width:260px;height:260px;box-shadow:0 0 140px 80px rgba(255,153,51,.55)}
#     .line{opacity:0;transition:opacity 1s;font-size:1.2rem;margin:6px}.line.on{opacity:1}
#     #hey{opacity:0;transform:scale(.7);transition:all 1.2s;font-size:clamp(2rem,8vw,4.5rem)}
#     #hey.on{opacity:1;transform:scale(1)}#dv{opacity:0;transition:opacity 1.5s;margin-top:-170px}
#     #dv.on{opacity:1}"""
#     body = f"""<div class="stage"><div id="spark"></div><div id="dv">{DIYA % 'lit'}</div>
#     <div style="margin-top:130px"><div class="line">Lights are ready...</div>
#     <div class="line">Fireworks are ready...</div><div class="line">Sweets are probably ready too...</div>
#     <h1 id="hey">HEY DIVYA! 🪔</h1><p class="line" id="sub" style="font-size:1.3rem">Your personal Diwali surprise is here!</p></div></div>"""
#     js = """
#     const L=$$('.line');setTimeout(()=>$('#spark').classList.add('grow'),400);
#     setTimeout(()=>$('#dv').classList.add('on'),2600);
#     L.slice(0,3).forEach((l,i)=>setTimeout(()=>l.classList.add('on'),3400+i*1200));
#     setTimeout(()=>{L.slice(0,3).forEach(l=>l.style.display='none');$('#hey').classList.add('on');salvo(3)},7400);
#     setTimeout(()=>$('#sub').classList.add('on'),8600);"""
#     show(body, js, css, 640)
#     st.markdown('<div class="cta">', unsafe_allow_html=True)
#     st.button("ENTER THE FESTIVE WORLD ✨", key="enter", on_click=go, args=("hero",))
#     st.markdown("</div>", unsafe_allow_html=True)


# def hero():
#     body = f"""<div class="garland"></div><h1 style="font-size:clamp(1.5rem,5vw,3rem)">A Festival Full of Lights, Laughter &amp; Good Vibes!</h1>
#     <p style="font-size:1.2rem">Welcome to your little Diwali celebration, Divya.</p>
#     {DIYA % 'lit big'}<button class="btn" onclick="salvo(5)">Fireworks! 🎆</button>{MUSIC_BTN}"""
#     show(body, "salvo(4);setInterval(()=>salvo(2),6000);", "", 470)
#     cols = st.columns(5)
#     items = [("Dhanteras Treasure 🪙", "treasure"), ("Seven Days of Diwali 🪔", "days"),
#              ("Light Up the Diyas ✨", "diyas"), ("Festival Fun Zone 🎉", "fun"),
#              ("Final Celebration 🎆", "finale")]
#     for c, (label, p) in zip(cols, items):
#         c.button(label, key="nav_" + p, on_click=go, args=(p,))
#     st.button("📜 Read the little festive note", key="nav_note", on_click=go, args=("note",))


# def treasure():
#     back_bar()
#     css = """
#     .chest{position:relative;width:220px;height:150px;margin:60px auto 20px}
#     .base{position:absolute;bottom:0;width:100%;height:95px;background:linear-gradient(#b8770f,#6e3f06);border:4px solid var(--gold);border-radius:6px 6px 14px 14px}
#     .lid{position:absolute;top:0;width:100%;height:60px;background:linear-gradient(#d99a1f,#8a5208);border:4px solid var(--gold);
#       border-radius:60px 60px 4px 4px;transform-origin:top left;transition:transform 1s cubic-bezier(.3,1.4,.5,1)}
#     .open .lid{transform:rotate(-65deg) translateY(-20px)}
#     .glow{position:absolute;left:10%;width:80%;top:50px;height:20px;border-radius:50%;opacity:0;transition:1s;
#       background:#ffe08a;box-shadow:0 0 80px 40px #ffb62e}.open .glow{opacity:1}
#     .coin{position:absolute;left:50%;top:60px;width:26px;height:26px;border-radius:50%;z-index:3;
#       background:radial-gradient(#fff2a8,#e8a817);border:2px solid #b87a0a;animation:burst 1.4s ease-out forwards}
#     @keyframes burst{to{transform:translate(var(--dx),var(--dy)) rotate(720deg);opacity:0}}
#     #big{width:90px;height:90px;border-radius:50%;margin:20px auto;cursor:pointer;font-size:2.4rem;font-weight:800;
#       background:radial-gradient(#fff2a8,#e8a817);border:4px solid #b87a0a;color:#8a5208;transition:.3s;animation:pulse 2s infinite}
#     #big:hover{transform:rotateY(180deg) scale(1.1)}@keyframes pulse{50%{box-shadow:0 0 40px 10px #ffb62e}}
#     #msg{opacity:0;transition:opacity 1.2s;font-size:1.25rem}#msg.on{opacity:1}"""
#     body = """<h1>Dhanteras Treasure 🪙</h1><div class="chest" id="ch"><div class="glow"></div>
#     <div class="base"></div><div class="lid"></div></div>
#     <button class="btn" id="ob" onclick="openT()">OPEN TREASURE</button>
#     <div class="glass" id="msg">May this Dhanteras bring you prosperity, success, good health, and countless reasons to celebrate!</div>
#     <p>Tap the golden coin for a wish:</p><div id="big" role="button" tabindex="0">₹</div>
#     <div class="glass" id="w" style="min-height:70px;font-size:1.1rem">Your wish will appear here ✨</div>"""
#     js = """
#     const wishes=["May your wallet be as full as your plate during Diwali!","May every coin you touch turn into a good memory!",
#     "May your year be golden, minus the price hikes!","May luck knock on your door and refuse to leave!",
#     "May your savings grow faster than the sweet box empties!","May good health be your biggest treasure!"];
#     function openT(){$('#ch').classList.add('open');$('#ob').disabled=true;$('#ob').textContent='Treasure opened!';
#       const ch=$('#ch');for(let i=0;i<32;i++){const c=document.createElement('div');c.className='coin';
#         c.style.setProperty('--dx',(Math.random()*400-200)+'px');c.style.setProperty('--dy',(Math.random()*-260-30)+'px');
#         c.style.animationDelay=Math.random()*.4+'s';ch.appendChild(c);setTimeout(()=>c.remove(),2200)}
#       salvo(3);setTimeout(()=>$('#msg').classList.add('on'),900)}
#     function wish(){$('#w').textContent=pick(wishes);boom(W/2,H/3)}
#     $('#big').onclick=wish;$('#big').onkeydown=e=>{if(e.key==='Enter'||e.key===' ')wish()};"""
#     show(body, js, css, 860)


# def days():
#     back_bar()
#     css = """.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
#     .card{cursor:pointer;text-align:left;transition:.3s;border:1px solid rgba(245,192,74,.4);color:inherit;font-family:inherit}
#     .card:hover{transform:translateY(-4px);box-shadow:0 0 24px rgba(255,153,51,.5)}
#     .card b{color:var(--gold);font-size:1.05rem}.m{max-height:0;overflow:hidden;opacity:0;transition:all .7s;margin-top:0}
#     .card.on .m{max-height:140px;opacity:1;margin-top:10px}.card.on{background:rgba(255,153,51,.18)}"""
#     D = [("Day 1 — Dhanteras", "May your life be filled with prosperity and opportunities."),
#          ("Day 2 — Choti Diwali", "May all negativity disappear and positive vibes take over!"),
#          ("Day 3 — Diwali", "May your home shine with happiness, laughter, and beautiful memories."),
#          ("Day 4 — Govardhan Puja", "Wishing you strength, blessings, and good fortune."),
#          ("Day 5 — Bhai Dooj", "May your family bonds always remain strong and joyful."),
#          ("Day 6 — Festival Vibes", "May you get unlimited happiness and unlimited holidays!"),
#          ("Day 7 — The Grand Finale", "May the coming year be full of achievements and exciting adventures.")]
#     cards = "".join(f'<button class="glass card" onclick="t(this)"><b>{a}</b><div class="m">{b}</div></button>' for a, b in D)
#     body = f'<h1>Seven Days of Diwali 🪔</h1><p>Tap a day to reveal its wish.</p><div class="grid">{cards}</div>'
#     js = "function t(e){e.classList.toggle('on');if(e.classList.contains('on')){const r=e.getBoundingClientRect();boom(r.left+r.width/2,r.top)}}"
#     show(body, js, css, 760)


# def diyas():
#     back_bar()
#     css = ".row{display:flex;flex-wrap:wrap;justify-content:center;gap:26px;margin:40px 0}.row .diya{cursor:pointer;transition:.3s}.row .diya:hover{transform:scale(1.12)}"
#     body = """<h1>Light Up the Diyas ✨</h1><p>Tap each diya to light it. <b id="c">0 / 7</b></p>
#     <div class="row" id="row"></div><div class="glass" id="m" style="min-height:70px;font-size:1.15rem">Tap a diya to begin.</div>"""
#     js = """
#     const M=["Good vibes loading... 100%!","Today's forecast: sweets with a chance of fireworks.","You make every room brighter.",
#     "Success is heading your way. Keep the door open!","Smiles are free. Spread them like diyas.","Your sparkle is officially on trend.","Peak festive energy detected!"];
#     let n=0;for(let i=0;i<7;i++){const d=document.createElement('div');d.className='diya';d.tabIndex=0;
#       d.innerHTML='<div class="flame"></div><div class="bowl"></div>';
#       const f=()=>{if(d.classList.contains('lit'))return;d.classList.add('lit');n++;$('#c').textContent=n+' / 7';
#         const r=d.getBoundingClientRect();boom(r.left+45,r.top);
#         $('#m').textContent=n==7?'Congratulations! You just upgraded this website\\'s brightness by 1000%!':pick(M);
#         if(n==7){salvo(6);document.body.style.filter='brightness(1.25)'}};
#       d.onclick=f;d.onkeydown=e=>{if(e.key==='Enter'||e.key===' ')f()};$('#row').appendChild(d)}"""
#     show(body, js, css, 640)


# def fun():
#     back_bar()
#     css = """.q button{display:block;width:100%;margin:6px 0;padding:12px;border-radius:12px;border:1px solid rgba(245,192,74,.5);
#       background:rgba(255,255,255,.08);color:inherit;font-family:inherit;cursor:pointer;font-size:1rem}
#     .q button:hover{background:rgba(255,153,51,.3)}.sec{margin:18px 0}"""
#     body = """<h1>Festival Fun Zone 🎉</h1>
#     <div class="glass sec"><button class="btn" onclick="salvo(8)">MAKE SOME NOISE! 🎆</button></div>
#     <div class="glass sec"><button class="btn" onclick="$('#w').textContent=pick(WI);boom(W/2,H/4)">SURPRISE ME!</button>
#       <p id="w" style="font-size:1.15rem">Press the button for a random wish.</p></div>
#     <div class="glass sec"><button class="btn" onclick="$('#md').textContent=pick(MO);boom(W/2,H/4)">Generate my Diwali mood</button>
#       <h3 id="md">Your mood: ???</h3></div>
#     <div class="glass sec q" id="qz"></div>"""
#     js = """
#     const WI=["May your sweets be endless and your diet be on holiday!","May your phone camera survive all the festive photos!",
#     "May your diyas stay lit and your WiFi stay strong!","May the only crackers around you be the fireworks!",
#     "May your leftovers outlast your willpower!","May all your Mondays feel like Diwali holidays!"];
#     const MO=["Sweets Overload Mode 🍬","Fireworks Enthusiast 🎆","Professional Diya Lighter 🪔","Festival Photography Expert 📸","Holiday Enjoyment Specialist 🏖️"];
#     const Q=[["Which sweet is a Diwali classic?",["Kaju Katli","Plain boiled rice","Raw onion"],0],
#     ["Diwali is known as the festival of...",["Snow","Lights","Sand"],1],
#     ["What do we light in rows at home?",["Diyas","Candles shaped like pizza","Ice cubes"],0],
#     ["Dhanteras is the day for...",["Ignoring prosperity","Welcoming prosperity","Sleeping through the festival"],1],
#     ["Best way to handle the sweet box?",["Share generously (and sneak one)","Hide it forever","Give it to the fireworks"],0]];
#     let qi=0,sc=0;function qr(){const z=$('#qz');
#       if(qi>=Q.length){const r=sc==5?"Diwali Legend! Sweets are on you.":sc>=3?"Festival Pro! Almost perfect.":"Festival Rookie, but the sweets still love you!";
#         z.innerHTML='<h3>Quiz done! Score: '+sc+'/5</h3><p>'+r+'</p><button class="btn" onclick="qi=0;sc=0;qr()">Play again</button>';salvo(5);return}
#       const q=Q[qi];z.innerHTML='<h3>Question '+(qi+1)+' of 5</h3><p>'+q[0]+'</p>';
#       q[1].forEach((o,i)=>{const b=document.createElement('button');b.textContent=o;
#         b.onclick=()=>{if(i==q[2])sc++;qi++;qr()};z.appendChild(b)})}qr();"""
#     show(body, js, css, 1250)


# def note():
#     back_bar()
#     css = ".card{max-width:640px;margin:30px auto;text-align:left;line-height:1.8;font-size:1.08rem;border:2px solid var(--gold)}"
#     body = """<div class="garland"></div><h1>A Little Festive Note</h1><div class="glass card">
#     <p>Hey Divya!</p><p>Just dropping by with a little digital Diwali surprise!</p>
#     <p>Hope this festive season brings you loads of happiness, success, good health, delicious sweets, amazing memories, and plenty of reasons to smile.</p>
#     <p>May your Dhanteras be prosperous and your Diwali week be full of fun, laughter, and positive vibes.</p>
#     <p>Keep shining and keep being awesome!</p><p>Wishing you a very Happy Dhanteras and a fantastic Diwali week!</p>
#     <p><b>Happy Diwali! 🪔✨</b></p></div><div class="garland"></div>"""
#     show(body, "salvo(2)", css, 900)


# def finale():
#     css = """.rg{position:fixed;width:360px;height:360px;border-radius:50%;opacity:.4;z-index:0;animation:spin 40s linear infinite;
#       background:repeating-conic-gradient(#ff9933 0 8deg,#2a0f4a 8deg 16deg);-webkit-mask:radial-gradient(circle,transparent 25%,#000 26% 60%,transparent 61%);mask:radial-gradient(circle,transparent 25%,#000 26% 60%,transparent 61%)}
#     @keyframes spin{to{transform:rotate(360deg)}}.stage{min-height:600px;display:flex;flex-direction:column;justify-content:center;align-items:center}
#     .big{font-size:clamp(1.8rem,7vw,4rem);background:linear-gradient(90deg,#ff9933,#fff1b8,#ff7eb6,#f5c04a);background-size:300%;
#       -webkit-background-clip:text;background-clip:text;color:transparent;animation:sh 4s linear infinite;text-shadow:none}
#     @keyframes sh{to{background-position:300%}}.row{display:flex;gap:30px;justify-content:center;margin-top:60px}
#     .fade{opacity:0;transition:opacity 1.5s}.fade.on{opacity:1}"""
#     body = f"""<div class="rg" style="left:-120px;top:-120px"></div><div class="rg" style="right:-120px;bottom:-120px"></div>
#     <div class="stage"><h1 class="big">LET THE FESTIVAL OF LIGHTS BEGIN!</h1>
#     <h2 class="fade" id="a" style="font-size:clamp(1.2rem,4vw,2.2rem)">HAPPY DHANTERAS &amp; HAPPY DIWALI WEEK, DIVYA! 🪔🎆</h2>
#     <p class="fade" id="b" style="font-size:1.3rem">Stay awesome, keep smiling, and enjoy all the sweets!</p>
#     <div class="row">{DIYA % 'lit'}{DIYA % 'lit'}{DIYA % 'lit'}{DIYA % 'lit'}{DIYA % 'lit'}</div>{MUSIC_BTN}</div>"""
#     js = "salvo(8);setInterval(()=>salvo(5),3500);setTimeout(()=>$('#a').classList.add('on'),1500);setTimeout(()=>$('#b').classList.add('on'),3000);"
#     show(body, js, css, 680)
#     st.markdown('<div class="cta">', unsafe_allow_html=True)
#     st.button("EXPERIENCE IT AGAIN ✨", key="again", on_click=go, args=("intro",))
#     st.markdown("</div>", unsafe_allow_html=True)
#     st.button("⬅ Back to festival", key="back_f", on_click=go, args=("hero",))


# # ---------------------------------------------------------------- router
# {"intro": intro, "hero": hero, "treasure": treasure, "days": days, "diyas": diyas,
#  "fun": fun, "note": note, "finale": finale}[st.session_state.page]()
# %%


"""Diwali Festival Experience (shareable with anyone) - a single-file Streamlit app."""
import html as _html
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Diwali 🪔", page_icon="🪔", layout="wide")

# Optional personalisation: share the link as  https://your-app/?name=Anu
NAME = _html.escape(str(st.query_params.get("name", "")).strip()[:30])
PH = {"%%HEY%%": NAME or "there", "%%HEYU%%": (NAME or "there").upper(),
      "%%COMMA%%": f", {NAME}" if NAME else "", "%%COMMAU%%": f", {NAME.upper()}" if NAME else ""}

PAGES = ["intro", "hero", "treasure", "days", "diyas", "fun", "note", "finale", "game"]
if "page" not in st.session_state:
    st.session_state.page = "intro"


def go(p):
    st.session_state.page = p


# ---------------------------------------------------------------- styling
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}
.stApp {background:radial-gradient(ellipse at top,#2a0f4a 0%,#0a0614 70%);}
.block-container {padding:0.5rem 1rem 2rem; max-width:1200px;}
iframe {border:0; border-radius:18px;}
.stButton>button {
  width:100%; min-height:64px; border-radius:16px; color:#ffe9b0; font-weight:600;
  background:rgba(255,255,255,.07); border:1px solid rgba(245,192,74,.45);
  backdrop-filter:blur(10px); transition:all .25s; white-space:normal;
}
.stButton>button:hover {transform:translateY(-4px); border-color:#f5c04a;
  box-shadow:0 0 26px rgba(255,153,51,.55); color:#fff;}
.stButton>button:focus-visible {outline:3px solid #f5c04a;}
.cta .stButton>button {background:linear-gradient(90deg,#ff9933,#f5c04a); color:#2a0f4a;
  font-size:1.1rem; font-weight:800; letter-spacing:.04em;}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------- shared iframe shell
BASE = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{--gold:#f5c04a;--saf:#ff9933;--org:#ff6a1a;--pur:#2a0f4a;--pink:#ff7eb6;--ink:#0a0614}
*{box-sizing:border-box}
html,body{margin:0;background:transparent;color:#fff4d6;font-family:'Poppins','Segoe UI',sans-serif;overflow-x:hidden}
h1,h2,h3{font-family:'Cinzel Decorative',Georgia,serif;margin:.3em 0;color:var(--gold);text-shadow:0 0 18px rgba(255,153,51,.7)}
#bg{position:fixed;inset:0;pointer-events:none;z-index:0}
.wrap{position:relative;z-index:1;padding:18px;text-align:center;max-width:1000px;margin:auto}
.glass{background:rgba(255,255,255,.07);border:1px solid rgba(245,192,74,.4);border-radius:20px;
  backdrop-filter:blur(12px);padding:20px;box-shadow:0 8px 40px rgba(0,0,0,.4)}
.btn{background:linear-gradient(90deg,var(--saf),var(--gold));color:var(--pur);font-weight:800;border:0;
  border-radius:999px;padding:14px 26px;font-size:1rem;cursor:pointer;margin:8px;transition:.2s;font-family:inherit}
.btn:hover{transform:scale(1.06);box-shadow:0 0 26px var(--saf)}
.btn:focus-visible{outline:3px solid #fff}
.garland{height:30px;background:radial-gradient(circle at 50% 50%,#ffb000 0 6px,#ff7a00 7px 11px,transparent 12px) 0 0/30px 30px repeat-x}
.diya{width:90px;height:70px;position:relative;margin:auto}
.bowl{position:absolute;bottom:0;width:90px;height:34px;background:linear-gradient(#ff9933,#a33f08);border-radius:0 0 90px 90px;box-shadow:0 6px 0 #6b2705}
.flame{position:absolute;left:50%;bottom:30px;width:18px;height:36px;margin-left:-9px;opacity:0;transition:opacity .4s;
  border-radius:50% 50% 50% 50%/62% 62% 38% 38%;background:radial-gradient(#fff6c8,#ffb62e 60%,#ff6a1a);
  filter:drop-shadow(0 0 14px #ffb62e);animation:fl .15s infinite alternate}
.lit .flame{opacity:1}
.lit .bowl{box-shadow:0 6px 0 #6b2705,0 0 60px 14px rgba(255,170,50,.55)}
.diya.big{transform:scale(2);margin:50px auto}
@keyframes fl{to{transform:scale(1.1,.92) rotate(4deg)}}
@media (prefers-reduced-motion:reduce){*{animation-duration:.01s!important}}
.ln{position:fixed;bottom:-60px;width:26px;height:34px;border-radius:8px 8px 4px 4px;pointer-events:none;z-index:0;
  background:linear-gradient(#ffb62e,#ff6a1a);box-shadow:0 0 22px 6px rgba(255,150,40,.6);opacity:.7;animation:rise linear infinite}
@keyframes rise{to{transform:translate(40px,-125vh)}}
%%CSS%%
</style></head><body><canvas id="bg"></canvas>
<div class="wrap">%%BODY%%</div>
<script>
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const pick=a=>a[Math.floor(Math.random()*a.length)];
const cv=$('#bg'),cx=cv.getContext('2d');let W,H,P=[],F=[],hook=()=>{};
function rs(){W=cv.width=innerWidth;H=cv.height=innerHeight}rs();addEventListener('resize',rs);
for(let i=0;i<60;i++)P.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*2+.5,v:Math.random()*.6+.2,a:Math.random()});
function boom(x,y){const c=['#f5c04a','#ff9933','#ff6a1a','#ff7eb6','#fff1b8'];
  for(let i=0;i<70;i++){const a=Math.PI*2*i/70,s=Math.random()*4+1.5;F.push({x,y,vx:Math.cos(a)*s,vy:Math.sin(a)*s,l:1,c:c[i%5]})}}
function salvo(n){for(let i=0;i<n;i++)setTimeout(()=>boom(Math.random()*W*.8+W*.1,Math.random()*H*.5+H*.1),i*350)}
(function loop(){cx.clearRect(0,0,W,H);
  P.forEach(p=>{p.y-=p.v;if(p.y<0){p.y=H;p.x=Math.random()*W}cx.globalAlpha=.4+.4*Math.sin(Date.now()/500+p.a*6);
    cx.fillStyle='#f5c04a';cx.beginPath();cx.arc(p.x,p.y,p.r,0,7);cx.fill()});
  F=F.filter(f=>f.l>0);F.forEach(f=>{f.x+=f.vx;f.y+=f.vy;f.vy+=.05;f.vx*=.985;f.l-=.012;
    cx.globalAlpha=Math.max(f.l,0);cx.fillStyle=f.c;cx.beginPath();cx.arc(f.x,f.y,2.2,0,7);cx.fill()});
  hook();requestAnimationFrame(loop)})();

let R=[],T=[],S=[],C=[];
function launch(x,y){R.push({x:W/2+(Math.random()-.5)*W*.4,y:H,tx:x,ty:y,t:0})}
function burst(x,y){const t=Math.floor(Math.random()*3),cs=['#f5c04a','#ff9933','#ff6a1a','#ff7eb6','#fff1b8'],n=t==2?90:70;
  for(let i=0;i<n;i++){let a=Math.PI*2*i/n,v=t==0?Math.random()*4+1.5:t==1?4.5:2+(i%3)*1.6;if(t==2)a+=i*.35;
    F.push({x,y,vx:Math.cos(a)*v,vy:Math.sin(a)*v,l:1,c:cs[(i+t)%5]})}}
boom=burst;
function confetti(n){const c=['#f5c04a','#ff9933','#ff6a1a','#ff7eb6','#b980ff'];
  for(let i=0;i<(n||120);i++)C.push({x:Math.random()*W,y:-20-Math.random()*200,vx:Math.random()*2-1,vy:Math.random()*3+2,r:Math.random()*6,s:Math.random()*8+4,c:c[i%5]})}
function shake(){document.body.animate([{transform:'translate(7px,-4px)'},{transform:'translate(-7px,4px)'},{transform:'none'}],{duration:260,iterations:3})}
addEventListener('pointerdown',e=>{if(e.target.closest('button,[role=button],.diya,.card,canvas#g'))return;launch(e.clientX,e.clientY)});
addEventListener('pointermove',e=>{T.push({x:e.clientX,y:e.clientY,l:1,c:pick(['#f5c04a','#ff9933','#fff1b8'])})});
setInterval(()=>S.push({x:Math.random()*W,y:0,vx:-6-Math.random()*4,vy:3+Math.random()*2,l:1}),3500);
hook=()=>{R=R.filter(r=>{r.t+=.03;const k=Math.min(r.t,1),x=r.x+(r.tx-r.x)*k,y=r.y+(r.ty-r.y)*k;
    T.push({x,y,l:1,c:'#ffd27a'});if(r.t>=1){burst(r.tx,r.ty);return false}return true});
  T=T.filter(t=>t.l>0);T.forEach(t=>{t.l-=.05;cx.globalAlpha=t.l;cx.fillStyle=t.c;cx.fillRect(t.x,t.y,3,3)});
  S=S.filter(s=>s.l>0);S.forEach(s=>{s.x+=s.vx;s.y+=s.vy;s.l-=.01;cx.globalAlpha=s.l;cx.strokeStyle='#fff';cx.beginPath();cx.moveTo(s.x,s.y);cx.lineTo(s.x-s.vx*5,s.y-s.vy*5);cx.stroke()});
  C=C.filter(c=>c.y<H+20);C.forEach(c=>{c.x+=c.vx;c.y+=c.vy;c.r+=.1;cx.globalAlpha=1;cx.fillStyle=c.c;cx.save();cx.translate(c.x,c.y);cx.rotate(c.r);cx.fillRect(-c.s/2,-c.s/4,c.s,c.s/2);cx.restore()})};
for(let i=0;i<8;i++){const d=document.createElement('div');d.className='ln';d.style.left=Math.random()*95+'%';
  d.style.animationDuration=(14+Math.random()*12)+'s';d.style.animationDelay=(-Math.random()*20)+'s';document.body.appendChild(d)}
/* music: synthesised with WebAudio, so there are no audio files that can go missing */
let AC,mOn=false,tm,step=0;const N=[392,440,494,587,659,587,494,440];
function tone(f,d){const t=AC.currentTime,o=AC.createOscillator(),g=AC.createGain();o.type='triangle';o.frequency.value=f;
  g.gain.setValueAtTime(.0001,t);g.gain.exponentialRampToValueAtTime(.07,t+.05);g.gain.exponentialRampToValueAtTime(.0001,t+d);
  o.connect(g);g.connect(AC.destination);o.start(t);o.stop(t+d)}
function tick(){if(!mOn)return;tone(N[step%8]*(step%16<8?1:.75),.9);step++;tm=setTimeout(tick,450)}
function music(){const b=$('#mu');try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();mOn=!mOn;
  if(mOn){AC.resume();tick()}else clearTimeout(tm);b.textContent=mOn?'⏸ Pause music':'🎵 Play music'}
  catch(e){b.textContent='Audio unavailable';b.disabled=true}}
%%JS%%
</script></body></html>"""

MUSIC_BTN = '<button class="btn" id="mu" onclick="music()" style="padding:8px 16px;font-size:.8rem">🎵 Play music</button>'


def show(body, js="", css="", h=640):
    html = BASE.replace("%%CSS%%", css).replace("%%BODY%%", body).replace("%%JS%%", js)
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
    .stage{min-height:600px;display:flex;flex-direction:column;align-items:center;justify-content:center}
    #spark{width:6px;height:6px;border-radius:50%;background:#fff3c0;box-shadow:0 0 12px 4px #f5c04a;
      transition:all 3s ease;opacity:0}
    #spark.grow{opacity:1;width:260px;height:260px;box-shadow:0 0 140px 80px rgba(255,153,51,.55)}
    .line{opacity:0;transition:opacity 1s;font-size:1.2rem;margin:6px}.line.on{opacity:1}
    #hey{opacity:0;transform:scale(.7);transition:all 1.2s;font-size:clamp(2rem,8vw,4.5rem)}
    #hey.on{opacity:1;transform:scale(1)}#dv{opacity:0;transition:opacity 1.5s;margin-top:-170px}
    #dv.on{opacity:1}"""
    body = f"""<div class="stage"><div id="spark"></div><div id="dv">{DIYA % 'lit'}</div>
    <div style="margin-top:130px"><div class="line">Lights are ready...</div>
    <div class="line">Fireworks are ready...</div><div class="line">Sweets are probably ready too...</div>
    <h1 id="hey">HEY %%HEYU%%! 🪔</h1><p class="line" id="sub" style="font-size:1.3rem">Your personal Diwali surprise is here!</p></div></div>"""
    js = """
    const L=$$('.line');setTimeout(()=>$('#spark').classList.add('grow'),400);
    setTimeout(()=>$('#dv').classList.add('on'),2600);
    L.slice(0,3).forEach((l,i)=>setTimeout(()=>l.classList.add('on'),3400+i*1200));
    setTimeout(()=>{L.slice(0,3).forEach(l=>l.style.display='none');$('#hey').classList.add('on');salvo(3)},7400);
    setTimeout(()=>$('#sub').classList.add('on'),8600);"""
    show(body, js, css, 640)
    st.markdown('<div class="cta">', unsafe_allow_html=True)
    st.button("ENTER THE FESTIVE WORLD ✨", key="enter", on_click=go, args=("hero",))
    st.markdown("</div>", unsafe_allow_html=True)


def hero():
    body = f"""<div class="garland"></div><h1 style="font-size:clamp(1.5rem,5vw,3rem)">A Festival Full of Lights, Laughter &amp; Good Vibes!</h1>
    <p style="font-size:1.2rem">Welcome to your little Diwali celebration%%COMMA%%.</p>
    {DIYA % 'lit big'}<button class="btn" onclick="salvo(5)">Fireworks! 🎆</button>{MUSIC_BTN}<p>Tap anywhere for a rocket 🚀 and wave your cursor around!</p>"""
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


def treasure():
    back_bar()
    css = """
    .chest{position:relative;width:220px;height:150px;margin:60px auto 20px}
    .base{position:absolute;bottom:0;width:100%;height:95px;background:linear-gradient(#b8770f,#6e3f06);border:4px solid var(--gold);border-radius:6px 6px 14px 14px}
    .lid{position:absolute;top:0;width:100%;height:60px;background:linear-gradient(#d99a1f,#8a5208);border:4px solid var(--gold);
      border-radius:60px 60px 4px 4px;transform-origin:top left;transition:transform 1s cubic-bezier(.3,1.4,.5,1)}
    .open .lid{transform:rotate(-65deg) translateY(-20px)}
    .glow{position:absolute;left:10%;width:80%;top:50px;height:20px;border-radius:50%;opacity:0;transition:1s;
      background:#ffe08a;box-shadow:0 0 80px 40px #ffb62e}.open .glow{opacity:1}
    .coin{position:absolute;left:50%;top:60px;width:26px;height:26px;border-radius:50%;z-index:3;
      background:radial-gradient(#fff2a8,#e8a817);border:2px solid #b87a0a;animation:burst 1.4s ease-out forwards}
    @keyframes burst{to{transform:translate(var(--dx),var(--dy)) rotate(720deg);opacity:0}}
    #big{width:90px;height:90px;border-radius:50%;margin:20px auto;cursor:pointer;font-size:2.4rem;font-weight:800;
      background:radial-gradient(#fff2a8,#e8a817);border:4px solid #b87a0a;color:#8a5208;transition:.3s;animation:pulse 2s infinite}
    #big:hover{transform:rotateY(180deg) scale(1.1)}@keyframes pulse{50%{box-shadow:0 0 40px 10px #ffb62e}}
    #msg{opacity:0;transition:opacity 1.2s;font-size:1.25rem}#msg.on{opacity:1}"""
    body = """<h1>Dhanteras Treasure 🪙</h1><div class="chest" id="ch"><div class="glow"></div>
    <div class="base"></div><div class="lid"></div></div>
    <button class="btn" id="ob" onclick="openT()">OPEN TREASURE</button>
    <div class="glass" id="msg">May this Dhanteras bring you prosperity, success, good health, and countless reasons to celebrate!</div>
    <p>Tap the golden coin for a wish:</p><div id="big" role="button" tabindex="0">₹</div>
    <div class="glass" id="w" style="min-height:70px;font-size:1.1rem">Your wish will appear here ✨</div>"""
    js = """
    const wishes=["May your wallet be as full as your plate during Diwali!","May every coin you touch turn into a good memory!",
    "May your year be golden, minus the price hikes!","May luck knock on your door and refuse to leave!",
    "May your savings grow faster than the sweet box empties!","May good health be your biggest treasure!"];
    function openT(){$('#ch').classList.add('open');$('#ob').disabled=true;$('#ob').textContent='Treasure opened!';
      const ch=$('#ch');for(let i=0;i<32;i++){const c=document.createElement('div');c.className='coin';
        c.style.setProperty('--dx',(Math.random()*400-200)+'px');c.style.setProperty('--dy',(Math.random()*-260-30)+'px');
        c.style.animationDelay=Math.random()*.4+'s';ch.appendChild(c);setTimeout(()=>c.remove(),2200)}
      salvo(3);confetti(100);shake();setTimeout(()=>$('#msg').classList.add('on'),900)}
    function wish(){$('#w').textContent=pick(wishes);boom(W/2,H/3)}
    $('#big').onclick=wish;$('#big').onkeydown=e=>{if(e.key==='Enter'||e.key===' ')wish()};"""
    show(body, js, css, 860)


def days():
    back_bar()
    css = """.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
    .card{cursor:pointer;text-align:left;transition:.3s;border:1px solid rgba(245,192,74,.4);color:inherit;font-family:inherit}
    .card:hover{transform:translateY(-4px);box-shadow:0 0 24px rgba(255,153,51,.5)}
    .card b{color:var(--gold);font-size:1.05rem}.m{max-height:0;overflow:hidden;opacity:0;transition:all .7s;margin-top:0}
    .card.on .m{max-height:140px;opacity:1;margin-top:10px}.card.on{background:rgba(255,153,51,.18)}"""
    D = [("Day 1 — Dhanteras", "May your life be filled with prosperity and opportunities."),
         ("Day 2 — Choti Diwali", "May all negativity disappear and positive vibes take over!"),
         ("Day 3 — Diwali", "May your home shine with happiness, laughter, and beautiful memories."),
         ("Day 4 — Govardhan Puja", "Wishing you strength, blessings, and good fortune."),
         ("Day 5 — Bhai Dooj", "May your family bonds always remain strong and joyful."),
         ("Day 6 — Festival Vibes", "May you get unlimited happiness and unlimited holidays!"),
         ("Day 7 — The Grand Finale", "May the coming year be full of achievements and exciting adventures.")]
    cards = "".join(f'<button class="glass card" onclick="t(this)"><b>{a}</b><div class="m">{b}</div></button>' for a, b in D)
    body = f'<h1>Seven Days of Diwali 🪔</h1><p>Tap a day to reveal its wish.</p><div class="grid">{cards}</div>'
    js = "function t(e){e.classList.toggle('on');if(e.classList.contains('on')){const r=e.getBoundingClientRect();boom(r.left+r.width/2,r.top)}}"
    show(body, js, css, 760)


def diyas():
    back_bar()
    css = ".row{display:flex;flex-wrap:wrap;justify-content:center;gap:26px;margin:40px 0}.row .diya{cursor:pointer;transition:.3s}.row .diya:hover{transform:scale(1.12)}"
    body = """<h1>Light Up the Diyas ✨</h1><p>Tap each diya to light it. <b id="c">0 / 7</b></p>
    <div class="row" id="row"></div><div class="glass" id="m" style="min-height:70px;font-size:1.15rem">Tap a diya to begin.</div>"""
    js = """
    const M=["Good vibes loading... 100%!","Today's forecast: sweets with a chance of fireworks.","You make every room brighter.",
    "Success is heading your way. Keep the door open!","Smiles are free. Spread them like diyas.","Your sparkle is officially on trend.","Peak festive energy detected!"];
    let n=0;for(let i=0;i<7;i++){const d=document.createElement('div');d.className='diya';d.tabIndex=0;
      d.innerHTML='<div class="flame"></div><div class="bowl"></div>';
      const f=()=>{if(d.classList.contains('lit'))return;d.classList.add('lit');n++;$('#c').textContent=n+' / 7';
        const r=d.getBoundingClientRect();boom(r.left+45,r.top);
        $('#m').textContent=n==7?'Congratulations! You just upgraded this website\\'s brightness by 1000%!':pick(M);
        if(n==7){salvo(6);confetti(200);shake();document.body.style.filter='brightness(1.25)'}};
      d.onclick=f;d.onkeydown=e=>{if(e.key==='Enter'||e.key===' ')f()};$('#row').appendChild(d)}"""
    show(body, js, css, 640)


def fun():
    back_bar()
    css = """.q button{display:block;width:100%;margin:6px 0;padding:12px;border-radius:12px;border:1px solid rgba(245,192,74,.5);
      background:rgba(255,255,255,.08);color:inherit;font-family:inherit;cursor:pointer;font-size:1rem}
    .q button:hover{background:rgba(255,153,51,.3)}.sec{margin:18px 0}"""
    body = """<h1>Festival Fun Zone 🎉</h1>
    <div class="glass sec"><button class="btn" onclick="salvo(8)">MAKE SOME NOISE! 🎆</button></div>
    <div class="glass sec"><button class="btn" onclick="$('#w').textContent=pick(WI);boom(W/2,H/4)">SURPRISE ME!</button>
      <p id="w" style="font-size:1.15rem">Press the button for a random wish.</p></div>
    <div class="glass sec"><button class="btn" onclick="$('#md').textContent=pick(MO);boom(W/2,H/4)">Generate my Diwali mood</button>
      <h3 id="md">Your mood: ???</h3></div>
    <div class="glass sec q" id="qz"></div>"""
    js = """
    const WI=["May your sweets be endless and your diet be on holiday!","May your phone camera survive all the festive photos!",
    "May your diyas stay lit and your WiFi stay strong!","May the only crackers around you be the fireworks!",
    "May your leftovers outlast your willpower!","May all your Mondays feel like Diwali holidays!"];
    const MO=["Sweets Overload Mode 🍬","Fireworks Enthusiast 🎆","Professional Diya Lighter 🪔","Festival Photography Expert 📸","Holiday Enjoyment Specialist 🏖️"];
    const Q=[["Which sweet is a Diwali classic?",["Kaju Katli","Plain boiled rice","Raw onion"],0],
    ["Diwali is known as the festival of...",["Snow","Lights","Sand"],1],
    ["What do we light in rows at home?",["Diyas","Candles shaped like pizza","Ice cubes"],0],
    ["Dhanteras is the day for...",["Ignoring prosperity","Welcoming prosperity","Sleeping through the festival"],1],
    ["Best way to handle the sweet box?",["Share generously (and sneak one)","Hide it forever","Give it to the fireworks"],0]];
    let qi=0,sc=0;function qr(){const z=$('#qz');
      if(qi>=Q.length){const r=sc==5?"Diwali Legend! Sweets are on you.":sc>=3?"Festival Pro! Almost perfect.":"Festival Rookie, but the sweets still love you!";
        z.innerHTML='<h3>Quiz done! Score: '+sc+'/5</h3><p>'+r+'</p><button class="btn" onclick="qi=0;sc=0;qr()">Play again</button>';salvo(5);return}
      const q=Q[qi];z.innerHTML='<h3>Question '+(qi+1)+' of 5</h3><p>'+q[0]+'</p>';
      q[1].forEach((o,i)=>{const b=document.createElement('button');b.textContent=o;
        b.onclick=()=>{if(i==q[2])sc++;qi++;qr()};z.appendChild(b)})}qr();"""
    show(body, js, css, 1250)


def note():
    back_bar()
    css = ".card{max-width:640px;margin:30px auto;text-align:left;line-height:1.8;font-size:1.08rem;border:2px solid var(--gold)}"
    body = """<div class="garland"></div><h1>A Little Festive Note</h1><div class="glass card">
    <p>Hey %%HEY%%!</p><p>Just dropping by with a little digital Diwali surprise!</p>
    <p>Hope this festive season brings you loads of happiness, success, good health, delicious sweets, amazing memories, and plenty of reasons to smile.</p>
    <p>May your Dhanteras be prosperous and your Diwali week be full of fun, laughter, and positive vibes.</p>
    <p>Keep shining and keep being awesome!</p><p>Wishing you a very Happy Diwali and a fantastic Diwali week!</p>
    <p><b>Happy Diwali! 🪔✨</b></p></div><div class="garland"></div>"""
    show(body, "salvo(2)", css, 900)


def finale():
    css = """.rg{position:fixed;width:360px;height:360px;border-radius:50%;opacity:.4;z-index:0;animation:spin 40s linear infinite;
      background:repeating-conic-gradient(#ff9933 0 8deg,#2a0f4a 8deg 16deg);-webkit-mask:radial-gradient(circle,transparent 25%,#000 26% 60%,transparent 61%);mask:radial-gradient(circle,transparent 25%,#000 26% 60%,transparent 61%)}
    @keyframes spin{to{transform:rotate(360deg)}}.stage{min-height:600px;display:flex;flex-direction:column;justify-content:center;align-items:center}
    .big{font-size:clamp(1.8rem,7vw,4rem);background:linear-gradient(90deg,#ff9933,#fff1b8,#ff7eb6,#f5c04a);background-size:300%;
      -webkit-background-clip:text;background-clip:text;color:transparent;animation:sh 4s linear infinite;text-shadow:none}
    @keyframes sh{to{background-position:300%}}.row{display:flex;gap:30px;justify-content:center;margin-top:60px}
    .fade{opacity:0;transition:opacity 1.5s}.fade.on{opacity:1}"""
    body = f"""<div class="rg" style="left:-120px;top:-120px"></div><div class="rg" style="right:-120px;bottom:-120px"></div>
    <div class="stage"><h1 class="big">LET THE FESTIVAL OF LIGHTS BEGIN!</h1>
    <h2 class="fade" id="a" style="font-size:clamp(1.2rem,4vw,2.2rem)">HAPPY DHANTERAS &amp; HAPPY DIWALI WEEK%%COMMAU%%! 🪔🎆</h2>
    <p class="fade" id="b" style="font-size:1.3rem">Stay awesome, keep smiling, and enjoy all the sweets!</p>
    <div class="row">{DIYA % 'lit'}{DIYA % 'lit'}{DIYA % 'lit'}{DIYA % 'lit'}{DIYA % 'lit'}</div>{MUSIC_BTN}</div>"""
    js = "salvo(8);confetti(220);setInterval(()=>{salvo(5);confetti(80);shake()},5000);setTimeout(()=>$('#a').classList.add('on'),1500);setTimeout(()=>$('#b').classList.add('on'),3000);"
    show(body, js, css, 680)
    st.markdown('<div class="cta">', unsafe_allow_html=True)
    st.button("EXPERIENCE IT AGAIN ✨", key="again", on_click=go, args=("intro",))
    st.markdown("</div>", unsafe_allow_html=True)
    st.button("⬅ Back to festival", key="back_f", on_click=go, args=("hero",))



def game():
    back_bar()
    css = "#g{width:100%;max-width:700px;border-radius:18px;border:2px solid var(--gold);touch-action:none;background:linear-gradient(#1b0a33,#0a0614)}"
    body = """<h1>Sweet Catch 🧺</h1><p>Move your mouse or finger to catch sweets 🍡 (+1), coins 🪙 (+2) and diyas 🪔 (+3). Dodge the crackers 💥 (-3)! You get 30 seconds.</p>
    <canvas id="g"></canvas><br><button class="btn" id="go" onclick="start()">START GAME</button>
    <div class="glass" id="r" style="min-height:60px">Ready when you are!</div>"""
    js = """
    const g=$('#g'),gx=g.getContext('2d');g.width=700;g.height=420;
    let run=false,sc=0,tl=30,bx=350,I=[],hi=0,lt;
    const K=[['🍡',1],['🪔',3],['🪙',2],['💥',-3]];
    g.addEventListener('pointermove',e=>{const r=g.getBoundingClientRect();bx=(e.clientX-r.left)*700/r.width});
    function start(){run=true;sc=0;tl=30;I=[];$('#go').disabled=true;$('#r').textContent='Go go go!';
      lt=setInterval(()=>{tl--;if(tl<=0)end()},1000)}
    function end(){run=false;clearInterval(lt);$('#go').disabled=false;hi=Math.max(hi,sc);confetti(160);salvo(4);
      $('#r').textContent='Score: '+sc+' | '+(sc>=40?'Diwali Champion! Sweets are on you.':sc>=20?'Sweet Master! Impressive.':'Warm-up round, hit start again!')}
    function spawn(){const r=Math.random();I.push({x:Math.random()*660+20,y:-20,v:2+Math.random()*2+(30-tl)*.06,k:r<.5?0:r<.7?1:r<.9?2:3})}
    (function gl(){gx.clearRect(0,0,700,420);gx.textAlign='center';
      if(run&&Math.random()<.07+(30-tl)*.003)spawn();
      I=I.filter(i=>{i.y+=i.v;if(run&&i.y>370&&i.y<405&&Math.abs(i.x-bx)<50){sc+=K[i.k][1];
        const r=g.getBoundingClientRect();if(K[i.k][1]<0)shake();else if(i.k>0)boom(r.left+i.x*r.width/700,r.top+i.y*r.height/420);return false}return i.y<440});
      gx.font='32px serif';I.forEach(i=>gx.fillText(K[i.k][0],i.x,i.y));gx.font='44px serif';gx.fillText('🧺',bx,410);
      gx.font='bold 20px sans-serif';gx.fillStyle='#ffe9b0';gx.fillText('Score '+sc+'   Time '+tl+'   Best '+hi,350,28);
      requestAnimationFrame(gl)})();"""
    show(body, js, css, 820)

# ---------------------------------------------------------------- router
{"intro": intro, "hero": hero, "treasure": treasure, "days": days, "diyas": diyas,
 "fun": fun, "note": note, "finale": finale, "game": game}[st.session_state.page]()