const loginButton = document.getElementById('login-submit');
const registerButton = document.getElementById('register-submit');

function showTab(tab) {
  document.querySelectorAll('.tab-button').forEach(button => {
    button.classList.remove('active');
  });
  document.querySelectorAll('.form-content').forEach(content => {
    content.classList.remove('active');
  });
  document.querySelector(`.tab-button[onclick="showTab('${tab}')"]`).classList.add('active');
  document.getElementById(tab).classList.add('active');
}

function handleLogin(event) {
  event.preventDefault();
  loginButton.disabled = true;
  loginButton.textContent = '처리 중...';

  setTimeout(() => {
    loginButton.disabled = false;
    loginButton.textContent = '로그인';
    window.location.href = './main-menu.html'; // 로그인 후 메인 메뉴 페이지로 이동
  }, 1000);
}

function handleRegister(event) {
  event.preventDefault();
  registerButton.disabled = true;
  registerButton.textContent = '처리 중...';

  setTimeout(() => {
    registerButton.disabled = false;
    registerButton.textContent = '회원가입';
    alert("회원가입이 완료되었습니다.");
  }, 1000);
}

