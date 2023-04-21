const container = document.querySelector('.message-con')
const inputmessage = document.querySelector('.inputmessage')
const btnsub = document.querySelector('.btnsub')
const token = document.querySelector('.token')
const idUser = document.querySelector('.idUser').innerHTML
const isactives = document.querySelector('.isactive').innerHTML
console.log('sdsw',idUser);
let innerh =""
const urls = 'http://127.0.0.1:8000/fetchat'
function mainchatbvox(chat) {
   
    chat.forEach(e => {
      
          if(isactives != 'None'  )  {

                
        innerh +=`
        <div class="user-sending sdddda" style=" ${e.sender ? ''  :  'display:none;'}">
        <p class="client" >${e.sender  ? e.messaga  :''  } 
        
            </p>
    </div>
    <div class="friend-sending  sdddda" style=" ${e.sender ? 'display:none;'  :  ''}"  >
        <p >
        ${e.sender ? 'null'  :  e.messaga} </p>
    </div>
    
        `

    }
     else{
         innerh +=`
         <div class="user-sending sdddda" style=" ${e.sender ? 'display:none;'  :  ''}">
         <p class="client" >${e.sender  ?   '':  e.messaga} 
  
             </p>
     </div>
     <div class="friend-sending  sdddda" style=" ${e.sender ? ''  :  'display:none;'}" >
         <p >
         ${e.sender ?   e.messaga: '' } </p>
     </div>
         `
     }
    
    
    container.innerHTML =  innerh
    // console.log(innerh);
});


}
function ajaxdeposite() {
    
    fetch(urls +`/${idUser}/`)
    .then(res => res.json())
    .then(data  =>{
        
        
        console.log(data.datamessage);
        
        mainchatbvox(data.datamessage)
        
       
      
    })
    
    
    
}
ajaxdeposite()
btnsub.addEventListener('click',e =>{
    e.preventDefault()
   
    fetch(urls +`/${idUser}/`,{
        method:"POST",
        headers:{
            'Content-Type' :'application/json',
            'X-CSRFToken':token.value,
        },
        body: JSON.stringify({
            messaga: inputmessage.value,
            sender: isactives | null,
           
         
    
        })
    })
    .then(resp => resp.json())
    .then(data => {
    postArr = []
    postArr.push(data.datamessage)
    mainchatbvox(postArr)
    // location.reload()
    console.log(data);
    }
    
        )
        inputmessage.value = ''
    })