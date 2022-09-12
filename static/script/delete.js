function cargarPregunta(){
    $.ajax({
        url:"/listaPreguntas",
        type:"GET",
        //data: {"value":valor},
        success: function(response){
            console.log(response)
            let preguntas = response.map(i => i.pregunta)
            let txt = "";
            for(let i=0 ; i<preguntas.length ; i++){
                txt += `<option value="${preguntas[i]}" data-id="${response[i].id_pregunta}" >${preguntas[i]}</option><br>`
            };
            document.getElementById('preg').innerHTML += txt;
                
        },
        error: function(error){
            //console.log(error);
    }, });
}

window.onload = cargarPregunta()


function mostrarPreg(){
    let valor = document.getElementById('preg')
    let id = valor.options[valor.selectedIndex].dataset.id
    
    let divSelect = document.getElementById('editar')
    
    let txt = `
    <h2>Pregunta seleccionada:</h2>
    <input readonly type="text" value="${valor.value}" name="textoPregunta" id="textoPregunta" style="width:90vw" >
    <input type="text" value="${id}" readonly style="display:none" name="idPregunta" id="idPregunta">
    <br><br>
    <button onclick="enviarDel()" type="button">BORRAR pregunta</button>
    `
    divSelect.innerHTML = txt;
}

function enviarDel(){
    let idPregunta = document.getElementById('idPregunta').value
    
    $.ajax({
    url:"/borrarPregunta",
    type:"DELETE",
    data: {idPregunta:idPregunta},
    success: function(response){
        alert('Pregunta borrada con exito')
        cargarPregunta()
    },
    error: function(error){
        console.log(error);
}, });
}