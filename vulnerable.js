// Vulnerability 1: Cross-Site Scripting (XSS)
const userInput = '<script>alert("XSS attack!");</script>';
document.getElementById('output').innerHTML = userInput;

// Vulnerability 2: SQL Injection
const username = 'admin';
const password = "' OR '1'='1";
const query = `SELECT * FROM users WHERE username='${username}' AND password='${password}'`;
db.execute(query);

// Vulnerability 3: Command Injection
const filename = 'file.txt';
const command = `cat ${filename}`;
exec(command);

// Vulnerability 4: Insecure Direct Object References
const userId = 123;
const userData = db.query(`SELECT * FROM users WHERE id=${userId}`);
if (userData) {
    // Display user data
} else {
    // Show error message
}

// Vulnerability 5: Cross-Site Request Forgery (CSRF)
const csrfToken = 'abc123';
const transferAmount = 1000;
const transferUrl = `https://example.com/transfer?amount=${transferAmount}&token=${csrfToken}`;
fetch(transferUrl, { method: 'POST' });

// Vulnerability 6: Insecure Deserialization
const serializedData = 'eyJpZCI6MTIzLCJ1c2VybmFtZSI6ImFkbWluIn0=';
const userData = deserialize(serializedData);
