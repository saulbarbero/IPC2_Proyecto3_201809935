////////////////////////cargar/////////////////////////////////////
function cargar(){
    actualizar()
    let file = document.getElementById("carga").files[0];
    if (file) {
        let reader = new FileReader();
        reader.readAsText(file, "UTF-8");
        reader.onload = function (evt) {
            let cuerpo = {
                data:evt.target.result
            }
            actualizar()
            console.log(JSON.stringify(cuerpo))
            fetch('http://localhost:5000/cargamasivaPintura', { 
            method: 'POST',
            headers,
            body: JSON.stringify(cuerpo),
            })
            .then(response => response.json())
            .then(result => {
              actualizar()
                console.log('Success:', result);
                actualizar()
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
  
        }
        reader.onerror = function (evt) {
            
        }
    }
  }