function mostrar(){
    $.ajax({
        url:"/listaPreguntas",
        type:"GET",
        //data: {"value":valor},
        success: function(response){
            console.log(response)
            let preguntas = response.map(i => i.pregunta)
            let txt = "<br>";
            for(let i=0 ; i<preguntas.length ; i++){
                txt += `${preguntas[i]}<br>`
            };
            document.getElementById('preguntas').innerHTML = txt;
                
        },
        error: function(error){
            //console.log(error);
    }, });
}