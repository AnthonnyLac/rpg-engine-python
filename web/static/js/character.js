const VALID_ATTRIBUTES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"];
let availableRolls = [];
let selectedValues = [];

// Funções de rolagem de dados
function rollD6() {
    return Math.floor(Math.random() * 6) + 1;
}

function roll3d6() {
    return rollD6() + rollD6() + rollD6();
}

function roll4d6DropLowest() {
    const rolls = [rollD6(), rollD6(), rollD6(), rollD6()];
    rolls.sort((a, b) => a - b);
    return rolls[1] + rolls[2] + rolls[3];
}

function rollAttributes(distributionStyle) {
    let rolls = [];

    if (distributionStyle === "classic" || distributionStyle === "adventurer") {
        for (let i = 0; i < 6; i++) {
            rolls.push(roll3d6());
        }
    } else if (distributionStyle === "heroic") {
        for (let i = 0; i < 6; i++) {
            rolls.push(roll4d6DropLowest());
        }
    }

    return rolls;
}

function organizeAttributesClassic(rolls) {
    const attributes = {};
    VALID_ATTRIBUTES.forEach((attr, index) => {
        attributes[attr] = rolls[index];
    });
    return attributes;
}

async function rollDice() {
    const distribution = document.getElementById('distribution').value;
    const rolls = rollAttributes(distribution);
    availableRolls = [...rolls]; // Mantém uma cópia dos rolls disponíveis
    selectedValues = []; // Reseta os valores selecionados

    document.getElementById('rolls-display').innerText = `Rolagens: ${rolls.join(', ')}`;
    document.getElementById('rolls').value = JSON.stringify(rolls);

    if (distribution === 'classic') {
        const attributes = organizeAttributesClassic(rolls);
        displayAttributes(attributes);
        document.getElementById('attributes').value = JSON.stringify(attributes);
    } else {
        setupManualDistribution(rolls);
    }
}

function displayAttributes(attributes) {
    let html = '<h3>Atributos Distribuídos:</h3>';
    for (const [attr, value] of Object.entries(attributes)) {
        html += `<p>${attr.charAt(0).toUpperCase() + attr.slice(1)}: ${value}</p>`;
    }
    document.getElementById('attributes-display').innerHTML = html;
}

function setupManualDistribution(rolls) {
    availableRolls = [...rolls]; // Inicializa os rolls disponíveis
    selectedValues = []; // Reseta os valores selecionados

    let html = `
        <h3>Distribua os Valores Manualmente</h3>
        <p>Rolagens disponíveis: ${rolls.join(', ')}</p>
        <p id="available-rolls">Valores restantes: ${availableRolls.join(', ')}</p>
    `;

    VALID_ATTRIBUTES.forEach(attr => {
        html += `
            <div class="attribute-row">
                <label>${attr.charAt(0).toUpperCase() + attr.slice(1)}:</label>
                <select name="${attr}" data-attribute="${attr}">
                    <option value="">Selecione um valor</option>
                    ${rolls.map(val => `<option value="${val}">${val}</option>`).join('')}
                </select>
            </div>
        `;
    });

    document.getElementById('attributes-display').innerHTML = html;
    document.getElementById('rolls').value = JSON.stringify(rolls);
}

function updateAvailableOptions() {
    // Coleta todos os valores já selecionados
    selectedValues = [];
    VALID_ATTRIBUTES.forEach(attr => {
        const select = document.querySelector(`select[name="${attr}"]`);
        if (select && select.value) {
            selectedValues.push(parseInt(select.value));
        }
    });

    // Cria uma cópia dos availableRolls para trabalhar
    let remainingRolls = [...availableRolls];

    // Remove apenas UMA ocorrência de cada valor selecionado
    selectedValues.forEach(selectedValue => {
        const index = remainingRolls.indexOf(selectedValue);
        if (index !== -1) {
            remainingRolls.splice(index, 1);
        }
    });

    // Atualiza as opções disponíveis em cada select
    VALID_ATTRIBUTES.forEach(attr => {
        const select = document.querySelector(`select[name="${attr}"]`);
        const currentValue = select.value ? parseInt(select.value) : null;

        // Limpa as opções
        select.innerHTML = '<option value="">Selecione um valor</option>';

        // Adiciona os valores restantes + o valor atual deste select (se houver)
        const optionsToAdd = [...remainingRolls];
        if (currentValue) {
            optionsToAdd.push(currentValue);
        }

        // Remove duplicatas e ordena
        const uniqueOptions = [...new Set(optionsToAdd)].sort((a, b) => a - b);

        uniqueOptions.forEach(val => {
            const option = document.createElement('option');
            option.value = val;
            option.textContent = val;
            select.appendChild(option);
        });

        // Restaura a seleção atual se ainda estiver disponível
        if (currentValue && Array.from(select.options).some(opt => parseInt(opt.value) === currentValue)) {
            select.value = currentValue;
        } else {
            select.value = "";
        }
    });

    // Atualiza a exibição dos valores restantes
    document.getElementById('available-rolls').textContent =
        `Valores restantes: ${remainingRolls.length > 0 ? remainingRolls.join(', ') : 'Nenhum'}`;
}

function updateManualAttributes() {
    const attributes = {};
    let allSelected = true;

    VALID_ATTRIBUTES.forEach(attr => {
        const select = document.querySelector(`select[name="${attr}"]`);
        if (select && select.value) {
            attributes[attr] = parseInt(select.value);
        } else {
            allSelected = false;
        }
    });

    if (allSelected) {
        document.getElementById('attributes').value = JSON.stringify(attributes);
    }

    updateAvailableOptions(); // Atualiza as opções disponíveis
}

async function submitCharacter(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const attributes = JSON.parse(document.getElementById('attributes').value || '{}');
    const rolls = JSON.parse(document.getElementById('rolls').value || '[]');

    const characterData = {
        name: formData.get('name'),
        race: formData.get('race'),
        class: formData.get('class'),
        distribution: formData.get('distribution'),
        attributes: attributes
    };

    try {
        const response = await fetch('/characters/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(characterData)
        });

        const result = await response.json();

        if (result.success) {
            alert('Personagem criado com sucesso!');
            window.location.href = '/characters';
        } else {
            alert('Erro: ' + result.error);
        }
    } catch (error) {
        alert('Erro ao criar personagem: ' + error.message);
    }
}

function updateDistributionUI() {
    const distribution = document.getElementById('distribution').value;
    const manualDistributions = ['heroic', 'adventurer'];

    if (manualDistributions.includes(distribution)) {
        document.getElementById('roll-button').style.display = 'block';
        document.getElementById('attributes-display').innerHTML =
            '<p>Clique em "Rolar Dados" para gerar os valores</p>';
    } else {
        document.getElementById('roll-button').style.display = 'block';
        document.getElementById('attributes-display').innerHTML = '';
    }
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('character-form');
    const distributionSelect = document.getElementById('distribution');
    const rollButton = document.getElementById('roll-button');
    
    form.addEventListener('submit', submitCharacter);
    distributionSelect.addEventListener('change', updateDistributionUI);
    rollButton.addEventListener('click', rollDice);
    
    // Adicionar event listeners para os selects de atributos
    document.addEventListener('change', function(e) {
        if (e.target.name && VALID_ATTRIBUTES.includes(e.target.name)) {
            updateManualAttributes();
        }
    });
});