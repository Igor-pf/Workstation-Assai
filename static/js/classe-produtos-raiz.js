let ctx = document.getElementById("classe_produto_raiz"); let dados = { datasets: [{ data: ['0'], backgroundColor: ["rgb(255, 99, 132)", "#52697c", "#d5c832", "#00377a", "#fec9ff", "rgb(255, 199, 132)", "rgb(55, 99, 132)", "#9f2d67", "#afafaf", "#fd0000", "#420e0e", "#585726", "#787861", "#db4985", "#52e9aa", "#818187", "#620000"]}], labels: ['BAZAR']}; let opcoes = { cutoutPercentage: 40};let meuDonutChart = new Chart(ctx, {type: "doughnut", data: dados, options: opcoes});