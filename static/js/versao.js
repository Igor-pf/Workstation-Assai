
    

    function verificar_versao() {
        versao_atual = 2.7
        var versao_local = document.getElementById("versao-local").value;
        var versao_local_id = document.getElementById("versao-local-id");

        if (versao_atual > versao_local) {
            
            versao_local_id.style.display = 'block';
        }
        
        
        
    
    }

    verificar_versao();
