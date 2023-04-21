const click__nav = document.querySelector('.toggle')
const conTainer__respo = document.querySelector('.linkholder')
const chat__customer_btn = document.querySelector('.submite')
const chat__customer_close_btn = document.querySelector('.click__chat_click')
const input__chat = document.querySelector('.input__chat')
const OUTPUT__con = document.querySelector('.textAre')
const TExtOutput = document.querySelectorAll('.TExtOutput')
const open__assistabnce = document.querySelector('.open__assistabnce')
const chat__customer_container= document.querySelector('.assistance__fixed__bar')
const main__Testimony= document.querySelector('.main__Testimony')
const play__btn= document.querySelector('.play__btn')
const video__into= document.querySelector('.video__into')
let paly_count  = 0

let allCon = document.querySelectorAll('.activeFre')

    allCon.forEach((e)=>{
        e.addEventListener('click',()=>{
            e.styles.color ='red'
            console.log('s,s')
        })
    })









let TExtOutputs = []
let INput__var = []
let Item = ""
// chat__customer_btn.addEventListener('click',()=>{
//    let anhh = INput__var.push(input__chat.value)
//     // alert(anhh);
//     console.log(INput__var);
//     INput__var.forEach(e => {
        
//         Item +=`
//         <t class="TExtOutput" >
//         <p>${e}</p>
//     </t>
//     <strong>
//     <p>${e}</p>
// </strong>
//         `
//         OUTPUT__con.innerHTML = Item
//         item = ""
//     })
//     // console.log(INput__var.concat (input__chat));
// })




click__nav.addEventListener('click',() =>{
conTainer__respo.classList.toggle('linkholder__clse')
})