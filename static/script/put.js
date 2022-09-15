function cargarPreguntas(){
    $.ajax({
        url:"/listaPreguntas",
        type:"GET",
        //data: {"value":valor},
        success: function(response){
            cargarRespuestas(response)     
        },
        error: function(error){
            //console.log(error);
    }, });
}

function cargarRespuestas(preguntas){
    $.ajax({
        url:"/listaRespuestas",
        type:"GET",
        //data: {"value":valor},
        success: function(response){
            console.log(response)
            console.log(preguntas)
            let respuestas = response.map(i => i.respuesta)
            let txt = "";
            
            txt += "<option selected disabled>Ninguna seleccionada</option><br>"
            
            for(let i=0 ; i<respuestas.length ; i++){
                
                txt += `
                <optgroup label="${preguntas[i].pregunta}">
                <option value="${respuestas[i]}" data-id="${response[i].id_respuesta}" >${respuestas[i]}</option><br>
                </optgroup>`
                

            };

            document.getElementById('preg').innerHTML = txt;
                
        },
        error: function(error){
            //console.log(error);
    }, });
}

window.onload = cargarPreguntas()


function mostrarPreg(){
    let valor = document.getElementById('preg')
    let id = valor.options[valor.selectedIndex].dataset.id
    
    let divSelect = document.getElementById('editar')
    
    let txt = `
    <h2>Pregunta seleccionada:</h2>
    <input class="form-control mb-2" type="text" value="${valor.value}" name="textoRespuesta" id="textoRespuesta" style="width:90vw">
    <input type="text" value="${id}" readonly style="display:none" name="idRespuesta" id="idRespuesta">
    <br><br>
    <button onclick="enviarMod()" type="button">Enviar modificaciones</button>
    `
    divSelect.innerHTML = txt;
}

function enviarMod(){
    let textoRespuesta = document.getElementById('textoRespuesta').value
    let idRespuesta = document.getElementById('idRespuesta').value
    
    $.ajax({
    url:"/modificarRespuesta",
    type:"PUT",
    data: {textoRespuesta:textoRespuesta, idRespuesta:idRespuesta},
    success: function(response){
        if(response[0] == 'True'){
            alert(`Modificaciones guardadas con exito . ${response[1]}.`)
            cargarPreguntas()
        }else{
            alert('Ha ocurrido un error con la base de datos')
        }
       
        
    },
    error: function(error){
        console.log(error);
}, });
}