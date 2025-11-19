function confirmarExclusao(event) {
    // Mostra uma janelinha de confirmação no navegador
    if (!confirm("Tem certeza que deseja excluir este filme?")) {
        event.preventDefault(); // Cancela o clique se a pessoa disser "Cancelar"
    }
}