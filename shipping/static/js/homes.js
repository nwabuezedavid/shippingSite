

// const   chevron_right= document.querySelector('.bi-chevron-right')
const box_slit = document.querySelectorAll('.bi-chevron-rightw')
const box_slit2 = document.querySelectorAll('.lds')
const main_holider_peronves = document.querySelector('.main-holider-peronves')
const main_holider_peronves2 = document.querySelector('.main-holider-peronves2')
const slide_investores = document.querySelectorAll('.main-disv-invesy')
 let investor= slide_investores[0].clientWidth
 let normail = 0




function jjd() {
   
        main_holider_peronves2.style.transform = `translateX(${- investor * normail }px)`
        
        main_holider_peronves2.style.transition = "all 2s" 
   
}



function investore() {

box_slit[0].classList.add('currentx')

    if (normail == slide_investores.length) {
        

        normail = 0
    } else {
        main_holider_peronves2.style.transform = `translateX(${- investor * normail }px)`
        
        main_holider_peronves2.style.transition = "all 2s" 
        normail++
    }

    ;}
let auto = true
function slir() {
  box_slit.forEach((esl,vlasw) => {
    if (vlasw == normail) {
        esl.classList.add('currentx')
       
    }else if(normail == box_slit.length ){
   normail = 0
    }
     else {
        esl.classList.remove('currentx')
        
    }
});  
}
let normail2 = 0
box_slit2.forEach((edd22,valesdd) => {
    slide_investores.forEach((edd2,valesdd2) => {
    edd22.addEventListener('click',()=>{
        if (valesdd ==  valesdd2) {
            jjd()
        edd22.classList.add('currentx2')
        console.log(normail)
        clearInterval(clesx)
        normail = valesdd2

        }else if (valesdd !=  valesdd2) {
        edd22.classList.remove('currentx2')
       
        clesx
 
        }
    })
    })

});


  let clesx = setInterval(() => {

investore()
slir()
}, 9000);


