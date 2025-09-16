function editCharacter(characterId) {
    if (confirm('Deseja editar este personagem?')) {
        window.location.href = `/characters/edit/${characterId}`;
    }
}

function deleteCharacter(characterId) {
    if (confirm('Tem certeza que deseja excluir este personagem?\nEsta ação não pode ser desfeita.')) {
        // Mostrar loading
        const btn = event.target;
        const originalText = btn.textContent;
        btn.textContent = 'Excluindo...';
        btn.disabled = true;

        fetch(`/characters/delete/${characterId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na resposta do servidor');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert('Personagem excluído com sucesso!');
                window.location.reload();
            } else {
                throw new Error(data.error || 'Erro desconhecido');
            }
        })
        .catch(error => {
            alert('Erro ao excluir personagem: ' + error.message);
            btn.textContent = originalText;
            btn.disabled = false;
        });
    }
}

// Adicionar event listeners quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    console.log('Página de lista de personagens carregada');

    // Adicionar animação de entrada aos cards
    const cards = document.querySelectorAll('.character-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.classList.add('fade-in');
    });
});

// Adicionar estilos de animação dinamicamente
const style = document.createElement('style');
style.textContent = `
    .fade-in {
        animation: fadeInUp 0.6s ease forwards;
        opacity: 0;
        transform: translateY(20px);
    }
    
    @keyframes fadeInUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);