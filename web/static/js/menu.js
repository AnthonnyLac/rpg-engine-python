function navigateTo(url) {
    // Efeito de loading no card clicado
    const card = event.currentTarget;
    card.style.opacity = '0.7';
    card.style.transform = 'scale(0.95)';
    card.style.cursor = 'wait';

    // Pequeno delay para o efeito visual
    setTimeout(() => {
        window.location.href = url;
    }, 300);
}

function showComingSoon() {
    // Efeito visual no card
    const card = event.currentTarget;
    card.style.animation = 'shake 0.5s ease';

    // Remove a animação após execução
    setTimeout(() => {
        card.style.animation = '';
    }, 500);

    // Mostra mensagem
    alert('Funcionalidade em desenvolvimento! 🚀\nEm breve disponível.');
}

// Adicionar estilos de animação dinamicamente
const style = document.createElement('style');
style.textContent = `
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        75% { transform: translateX(5px); }
    }
    
    .menu-card:active {
        transform: scale(0.95) !important;
    }
`;
document.head.appendChild(style);

// Efeitos de interação
document.addEventListener('DOMContentLoaded', function() {
    console.log('Menu carregado com sucesso!');

    // Adicionar event listeners para teclado
    document.addEventListener('keydown', function(e) {
        // Atalhos de teclado
        if (e.key === '1') navigateTo('/create-form');
        if (e.key === '2') navigateTo('/characters');
        if (e.key === 'Escape') window.location.href = '/';
    });

    // Tooltip para atalhos
    const cards = document.querySelectorAll('.menu-card');
    cards[0].title = 'Atalho: Tecla 1';
    cards[1].title = 'Atalho: Tecla 2';
});

// Efeito de parallax no background
document.addEventListener('mousemove', function(e) {
    const x = (e.clientX / window.innerWidth - 0.5) * 20;
    const y = (e.clientY / window.innerHeight - 0.5) * 20;

    document.body.style.backgroundPosition = `${50 + x}% ${50 + y}%`;
});