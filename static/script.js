document.getElementById('raffle-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const quantity = document.getElementById('quantity').value;
  
    const response = await fetch('/raffle/buy', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, email, quantity }),
    });

    const data = await response.json();
    document.getElementById('result').innerHTML = `
      Seus números da rifa: ${data.tickets.join(', ')}
      <br>
      <img src="${data.pix_qr_code}" alt="QR Code PIX">
      <br>
      Válido até: ${new Date(data.pix_expiration_date).toLocaleString()}
    `;
  });
  