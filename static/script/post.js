function enviar(){
    let form = document.getElementById("form").elements;
    let textoPregunta = form["textoPregunta"].value;
    let nivel = form["nivel"].value;
    let categoria = form["categoria"].value;

    if(nivel == "" || categoria == "" || /[a-zA-Z]/.test(textoPregunta) == false){
        return alert('Deben completarse todos los datos del formulario')
    }else{
        console.log(textoPregunta, nivel, categoria)
        $.ajax({
            url:"/agregarPreguntas",
            type:"POST",
            data: {textoPregunta:textoPregunta, nivel:nivel,categoria:categoria},
            success: function(response){
                if(response == 'True'){
                    alert('Pregunta agregada con exito a la base')
                }else{
                    alert('Ha ocurrido un error con la base de datos')
                }
            },
            error: function(error){
                console.log(error);
        }, });
    }
    
    
}