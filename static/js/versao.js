
    

    function verificar_versao() {
        versao_atual = 2.0
        var versao_local = document.getElementById("versao-local").value;
        var versao_local_id = document.getElementById("versao-local");

        if (versao_atual > versao_local.value) {
            
            versao_local_id.style.display = 'block';}
        
        
        
    
    }
