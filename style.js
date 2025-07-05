async function getMotivation() {
    const mood = document.getElementById('mood').value;

    const response = await fetch('/generate_motivation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ mood: mood })
    });

    const data = await response.json();

    if (data.motivation) {
        document.getElementById('output').textContent = `"${data.motivation}"`;
    } else {
        document.getElementById('output').textContent = "Something went wrong. Try again!";
    }
}

