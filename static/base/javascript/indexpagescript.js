// for index page java script
const a = document.getElementById('l');
    a.addEventListener('click', function f() {
      if (document.getElementById('i').style.display == 'none') {
        document.getElementById('i').style.display = 'flex';
        document.getElementById('left').style.background = 'black';
      } else {
        document.getElementById('i').style.display = 'none';
        document.getElementById('left').style.background = 'none';
      }
    })

function myfunction(){
  window.location.href = "/logoutt"
}
function my(){
  window.location.href = "/sign"
}
const e=document.getElementById('teams')
e.addEventListener('click',function s(){
  window.location.href="/AllTeams"
})

function team(teamurl){
  window.location.href= teamurl
}
const f=document.getElementById('pointstable')
f.addEventListener('click',function x(){
  window.location.href="/pointstable"
})
const g=document.getElementById('shop')
g.addEventListener('click',function y(){
  window.location.href="/shop"
})
