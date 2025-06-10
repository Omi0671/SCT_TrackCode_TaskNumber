# SCT_TrackCode_TaskNumber 1
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Caesar Cipher Encrypt & Decrypt</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;800&display=swap');
  :root {
    --color-bg: #ffffff;
    --color-text: #6b7280;
    --color-primary: #000000;
    --color-shadow: rgba(0,0,0,0.05);
    --border-radius: 0.75rem;
    --transition-speed: 0.3s;
  }
  * {
    box-sizing: border-box;
  }
  body {
    margin: 0;
    font-family: 'Inter', sans-serif;
    background-color: var(--color-bg);
    color: var(--color-text);
    line-height: 1.5;
    display: flex;
    justify-content: center;
    padding: 2rem 1rem 4rem;
    min-height: 100vh;
  }
  .container {
    max-width: 700px;
    width: 100%;
  }
  header {
    position: sticky;
    top: 0;
    background: var(--color-bg);
    padding: 1rem 0 1.5rem;
    margin-bottom: 3rem;
    border-bottom: 1px solid #e5e7eb;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 10;
  }
  header h1 {
    font-size: 1.75rem;
    font-weight: 800;
    color: var(--color-primary);
    margin: 0;
  }
  nav a {
    color: var(--color-primary);
    text-decoration: none;
    font-weight: 600;
    margin-left: 1.5rem;
    transition: color var(--transition-speed);
  }
  nav a:hover, nav a:focus {
    color: #2563eb;
  }
  main {
    background: white;
    padding: 2.5rem 2rem;
    border-radius: var(--border-radius);
    box-shadow: 0 4px 12px var(--color-shadow);
  }
  h2 {
    font-size: 3rem;
    font-weight: 800;
    margin: 0 0 0.5rem;
    color: var(--color-primary);
  }
  p.lead {
    margin-top: 0;
    font-size: 1.125rem;
    font-weight: 500;
    color: var(--color-text);
    margin-bottom: 2rem;
  }
  form {
    display: grid;
    gap: 1.25rem;
  }
  label {
    display: flex;
    flex-direction: column;
    font-weight: 600;
    color: var(--color-primary);
    font-size: 1rem;
  }
  input[type="text"],
  input[type="number"] {
    margin-top: 0.5rem;
    padding: 0.75rem 1rem;
    font-size: 1rem;
    border: 1px solid #d1d5db;
    border-radius: 0.5rem;
    transition: border-color var(--transition-speed);
  }
  input[type="text"]:focus,
  input[type="number"]:focus {
    border-color: #2563eb;
    outline: none;
  }
  .buttons {
    margin-top: 1rem;
    display: flex;
    gap: 1rem;
  }
  button {
    background-color: var(--color-primary);
    color: white;
    border: none;
    border-radius: 0.5rem;
    padding: 0.75rem 1.5rem;
    font-size: 1.125rem;
    font-weight: 600;
    cursor: pointer;
    transition: background-color var(--transition-speed), transform var(--transition-speed);
    flex: 1;
  }
  button:hover, button:focus {
    background-color: #2563eb;
    transform: scale(1.03);
    outline: none;
  }
  .result {
    margin-top: 2rem;
    background-color: #f9fafb;
    padding: 1.5rem;
    border-radius: var(--border-radius);
    font-family: monospace;
    font-size: 1.125rem;
    color: #111827;
    min-height: 4rem;
    white-space: pre-wrap;
    word-break: break-word;
  }
  footer {
    margin-top: 4rem;
    text-align: center;
    font-size: 0.875rem;
    color: var(--color-text);
  }
</style>
</head>
<body>
  <div class="container" role="main">
    <header>
      <h1>Caesar Cipher Tool</h1>
      <nav aria-label="Primary navigation">
        <a href="#encrypt">Encrypt</a>
        <a href="#decrypt">Decrypt</a>
      </nav>
    </header>
    <main>
      <h2 id="encrypt">Encrypt / Decrypt Text</h2>
      <p class="lead">Enter a message and a shift value to encrypt or decrypt using the Caesar Cipher algorithm.</p>
      <form id="cipher-form" aria-describedby="result-label">
        <label for="message-input">
          Message
          <input type="text" id="message-input" name="message" required autocomplete="off" aria-required="true" placeholder="Enter your message here" />
        </label>
        <label for="shift-input">
          Shift Value (Number)
          <input type="number" id="shift-input" name="shift" required aria-required="true" min="0" max="25" value="0" />
        </label>
        <div class="buttons">
          <button type="button" id="encrypt-btn" aria-controls="result" aria-label="Encrypt message">Encrypt</button>
          <button type="button" id="decrypt-btn" aria-controls="result" aria-label="Decrypt message">Decrypt</button>
        </div>
      </form>
      <div id="result-label" style="position: absolute; left: -9999px;">Result</div>
      <div class="result" id="result" aria-live="polite" aria-atomic="true"></div>
    </main>
    <footer>
      &copy; 2024 Caesar Cipher Tool. Created by Developer.
    </footer>
  </div>

<script>
  // Caesar Cipher function for encrypt or decrypt
  function caesarCipher(str, shift, decrypt = false) {
    if (decrypt) shift = (26 - shift) % 26;
    return str.replace(/[a-z]/gi, function(char) {
      const start = char <= 'Z' ? 65 : 97;
      return String.fromCharCode((char.charCodeAt(0) - start + shift) % 26 + start);
    });
  }

  const messageInput = document.getElementById('message-input');
  const shiftInput = document.getElementById('shift-input');
  const resultDiv = document.getElementById('result');
  const encryptBtn = document.getElementById('encrypt-btn');
  const decryptBtn = document.getElementById('decrypt-btn');

  encryptBtn.addEventListener('click', () => {
    const message = messageInput.value.trim();
    const shift = parseInt(shiftInput.value, 10);
    if (!message) {
      resultDiv.textContent = 'Please enter a message.';
      return;
    }
    if (isNaN(shift) || shift < 0 || shift > 25) {
      resultDiv.textContent = 'Shift value must be between 0 and 25.';
      return;
    }
    const encrypted = caesarCipher(message, shift, false);
    resultDiv.textContent = encrypted;
  });

  decryptBtn.addEventListener('click', () => {
    const message = messageInput.value.trim();
    const shift = parseInt(shiftInput.value, 10);
    if (!message) {
      resultDiv.textContent = 'Please enter a message.';
      return;
    }
    if (isNaN(shift) || shift < 0 || shift > 25) {
      resultDiv.textContent = 'Shift value must be between 0 and 25.';
      return;
    }
    const decrypted = caesarCipher(message, shift, true);
    resultDiv.textContent = decrypted;
  });
</script>
</body>
</html>

