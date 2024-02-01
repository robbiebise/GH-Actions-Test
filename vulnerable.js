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

// Vulnerability 7: XML External Entity (XXE) Injection
const xmlData = '<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>';
parseXml(xmlData);

// Vulnerability 8: Server-Side Request Forgery (SSRF)
const url = 'http://example.com/api/data';
fetch(url);

// Vulnerability 9: Remote Code Execution (RCE)
const command = 'ls';
exec(command);

// Vulnerability 10: Insecure Cryptographic Storage
const password = 'password123';
const hashedPassword = md5(password

// Vulnerability 11: Security Misconfiguration
const debugMode = true;
if (debugMode) {
    // Display debug information
}

// Vulnerability 12: Insufficient Logging and Monitoring
const logFile = 'app.log';
logToFile(logFile, 'User accessed sensitive data');

// Vulnerability 13: Using Components with Known Vulnerabilities
const vulnerableLibrary = require('vulnerable-library');
vulnerableLibrary.doSomething();

// Vulnerability 14: Unvalidated Redirects and Forwards
const redirectUrl = 'http://example.com';
res.redirect
