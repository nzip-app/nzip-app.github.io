(function(){
 var os=/Mac/i.test(navigator.platform)?'mac':/Linux|X11/i.test(navigator.userAgent)&&!/Android/i.test(navigator.userAgent)?'linux':'win';
 var b=document.getElementById('dlmain');if(b){var t=b.getAttribute('data-'+os);if(t){b.href=t;b.querySelector('.os').textContent=b.getAttribute('data-name-'+os);}}
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');e.target.querySelectorAll('[data-w]').forEach(function(i){i.style.width=i.getAttribute('data-w')});io.unobserve(e.target);}})},{threshold:.15});
 document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});
 document.querySelectorAll('.tab').forEach(function(t){t.addEventListener('click',function(){
  document.querySelectorAll('.tab').forEach(function(x){x.classList.toggle('on',x===t)});
  document.querySelectorAll('.set').forEach(function(s){var on=s.id===t.getAttribute('data-set');s.hidden=!on;if(on)s.querySelectorAll('[data-w]').forEach(function(i){i.style.width='0';requestAnimationFrame(function(){requestAnimationFrame(function(){i.style.width=i.getAttribute('data-w')})})})});
 })});
 document.querySelectorAll('a.mail').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();
  location.href='mailto:'+atob(a.getAttribute('data-m')).split('').reverse().join('')+'?subject=NZip';})});
 var sel=document.getElementById('lang');if(sel)sel.addEventListener('change',function(){try{localStorage.setItem('nzip-lang',sel.value)}catch(e){}var sub=sel.getAttribute('data-sub');location.href=(sub?'../../':'../')+sel.value+'/'+(sub||'')});
})();
