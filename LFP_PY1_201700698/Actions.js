var radio = document.querySelectorAll('.radio')
var texto = document.getElementById('tx')
var option = document.getElementById('grupo-option') 
var btnif = document.getElementById('btnInfo')
var btn = document.getElementById('btn')
var s 
console.log(btn.value)
f()
function f (){
        if(btn.value == 'info'){
                btn.addEventListener("click",()=>{
                        radio.forEach(e => {
                       
                                if(e.checked == true){
                                         window.s = e.value
                                        console.log( " es box" + s)
                                        
                                        
                                }else{
                                       
                                }
                               
                        });
                console.log(window.s)
                console.log('Click')
                var iframe = document.createElement('iframe')
                        
                var html = '<div><h2><ur>'     
                                +texto.value+'<br>'+
                                window.s+'<br>'+
                               option.value+'<br>'+
                 
                                                '</ur></h2></div>';
        
                iframe.src = 'data:text/html;charset=utf-8,' + encodeURI(html);
                document.getElementById('contenido').appendChild(iframe);

                });
        }else if(btn.value =='entrada'){
                btn =document.addEventListener("click", () => {

                        var iframe = document.createElement('iframe')
                        iframe.src =  encodeURI('infoAnalizador.txt');
                        document.getElementById('contenido').appendChild(iframe);
                          
                
                        
                }); 
        }
       
}

/*
var btn = document.getElementById('btnInfo').addEventListener("click", () => {
        
        radio.forEach(e => {
                       
                        if(e.checked == true){
                                 window.s = e.value
                                console.log( " es box" + s)
                                
                                
                        }else{
                               
                        }
                       
                });
        console.log(window.s)
        console.log('Click')
        var iframe = document.createElement('iframe')
                
        var html = '<div><h2><ur>'     
                        +texto.value+'<br>'+
                        window.s+'<br>'+
                       option.value+'<br>'+
         
                                        '</ur></h2></div>';

        iframe.src = 'data:text/html;charset=utf-8,' + encodeURI(html);
        document.getElementById('contenido').appendChild(iframe);
          

        
});*/
/*var btn2 =document.getElementById('btnEntrada').addEventListener("click", () => {

        var iframe = document.createElement('iframe')
        iframe.src = 'ejemploP1.form' ;
        document.getElementById('contenido').appendChild(iframe);
          

        
});*/
