function enviar(){
    let form = document.getElementById("form").elements;
    let textoPregunta = form["textoPregunta"].value;
    let nivel = form["nivel"].value;
    let categoria = form["categoria"].value;
    
    console.log(textoPregunta, nivel, categoria)
    $.ajax({
        url:"/agregarPreguntas",
        type:"POST",
        data: {textoPregunta:textoPregunta, nivel:nivel,categoria:categoria},
        success: function(response){
            alert('Pregunta agregada con exito a la base')
        },
        error: function(error){
            console.log(error);
    }, });
}