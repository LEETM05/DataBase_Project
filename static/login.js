// const loginButton = document.getElementById('login-submit');// const registerButton = document.getElementById('register-submit');//// function showTab(tab) {//     document.querySelectorAll('.tab-button').forEach(button => {//         button.classList.remove('active');//     });//     document.querySelectorAll('.form-content').forEach(content => {//         content.classList.remove('active');//     });//     document.querySelector(`.tab-button[onclick="showTab('${tab}')"]`).classList.add('active');//     document.getElementById(tab).classList.add('active');// }//// function handleRegister(event) {//     event.preventDefault();  // 폼 제출을 막음////     const username = document.getElementById('register-id').value;//     const password = document.getElementById('register-password').value;//     const confirmPassword = document.getElementById('register-confirm-password').value;////     const usernameRegex = /^[a-zA-Z0-9]+$/;  // 아이디는 영어와 숫자만 가능//     const passwordRegex = /^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;  // 비밀번호는 영어, 숫자, 특수문자 포함, 8자 이상////     if (!usernameRegex.test(username)) {//         alert('아이디는 영어와 숫자만 가능합니다.');//         return;  // 유효성 검사 실패 시 폼 제출 차단//     }////     if (!passwordRegex.test(password)) {//         alert('비밀번호는 영어, 숫자, 특수문자를 포함해야 하며, 최소 8자 이상이어야 합니다.');//         return;  // 유효성 검사 실패 시 폼 제출 차단//     }////     if (password !== confirmPassword) {//         alert('비밀번호가 일치하지 않습니다.');//         return;  // 유효성 검사 실패 시 폼 제출 차단//     }////     // 모든 유효성 검사를 통과한 경우에만 폼을 서버로 제출//     event.target.submit();// }//// // 실시간으로 비밀번호 확인 필드 검사// document.getElementById('register-confirm-password').addEventListener('input', function () {//     const password = document.getElementById('register-password').value;//     const confirmPassword = this.value;//     const confirmPasswordMessage = document.getElementById('confirm-password-message');////     if (confirmPassword !== password) {//         confirmPasswordMessage.textContent = '비밀번호가 다릅니다';//         confirmPasswordMessage.style.color = 'red';//     } else {//         confirmPasswordMessage.textContent = '';//     }// });//// document.addEventListener("DOMContentLoaded", function () {//     const registerButton = document.getElementById('register-submit');//     const checkUsernameButton = document.getElementById('check-username-btn');//     const usernameInput = document.getElementById('register-id');//     const passwordInput = document.getElementById('register-password');//     const confirmPasswordInput = document.getElementById('register-confirm-password');//     const nameInput = document.getElementById('register-name');//     const usernameMessage = document.getElementById('username-message');////     // 아이디와 비밀번호에서 한글 입력 방지 함수//     function preventKoreanInput(event) {//         const value = event.target.value;//         if (/[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/.test(value)) {//             event.target.value = value.replace(/[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/g, '');//         }//     }////     // 한글 입력 방지 이벤트 리스너 추가//     usernameInput.addEventListener('input', preventKoreanInput);//     passwordInput.addEventListener('input', preventKoreanInput);//     confirmPasswordInput.addEventListener('input', preventKoreanInput);////     // 아이디 중복 확인 버튼 클릭 시//     window.checkUsername = function () {//         const username = usernameInput.value;////         if (username.length > 0) {//             // Ajax 요청을 사용하여 서버에 아이디 중복 여부 확인//             fetch(`/login_page/check_username/?username=${username}`)//                 .then(response => response.json())//                 .then(data => {//                     if (data.exists) {//                         usernameMessage.textContent = '이미 존재하는 아이디입니다.';//                         usernameMessage.style.color = 'red';////                         // 입력란 비활성화//                         passwordInput.disabled = true;//                         confirmPasswordInput.disabled = true;//                         nameInput.disabled = true;//                         registerButton.disabled = true;//                     } else {//                         usernameMessage.textContent = '사용 가능한 아이디입니다.';//                         usernameMessage.style.color = 'green';////                         // 입력란 활성화//                         passwordInput.disabled = false;//                         confirmPasswordInput.disabled = false;//                         nameInput.disabled = false;//                         registerButton.disabled = false;//                     }//                 })//                 .catch((error) => {//                     console.error('Error:', error);//                 });//         } else {//             usernameMessage.textContent = '아이디를 입력해 주세요.';//             usernameMessage.style.color = 'red';//         }//     };// });//// 탭 전환 기능function showTab(tab) {    document.querySelectorAll('.tab-button').forEach(button => {        button.classList.remove('active');    });    document.querySelectorAll('.form-content').forEach(content => {        content.classList.remove('active');    });    document.querySelector(`.tab-button[onclick="showTab('${tab}')"]`).classList.add('active');    document.getElementById(tab).classList.add('active');}// 회원가입 폼 제출 핸들러function handleRegister(event) {    event.preventDefault();  // 폼 제출을 막음    const username = document.getElementById('register-id').value;    const password = document.getElementById('register-password').value;    const confirmPassword = document.getElementById('register-confirm-password').value;    const usernameRegex = /^[a-zA-Z0-9]+$/;  // 아이디는 영어와 숫자만 가능    const passwordRegex = /^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;  // 비밀번호는 영어, 숫자, 특수문자 포함, 8자 이상    if (!usernameRegex.test(username)) {        alert('아이디는 영어와 숫자만 가능합니다.');        return;  // 유효성 검사 실패 시 폼 제출 차단    }    if (!passwordRegex.test(password)) {        alert('비밀번호는 영어, 숫자, 특수문자를 포함해야 하며, 최소 8자 이상이어야 합니다.');        return;  // 유효성 검사 실패 시 폼 제출 차단    }    if (password !== confirmPassword) {        alert('비밀번호가 일치하지 않습니다.');        return;  // 유효성 검사 실패 시 폼 제출 차단    }    // 모든 유효성 검사를 통과한 경우에만 폼을 서버로 제출    event.target.submit();}// 실시간으로 비밀번호 확인 필드 검사document.getElementById('register-confirm-password').addEventListener('input', function () {    const password = document.getElementById('register-password').value;    const confirmPassword = this.value;    const confirmPasswordMessage = document.getElementById('confirm-password-message');    if (confirmPassword !== password) {        confirmPasswordMessage.textContent = '비밀번호가 다릅니다';        confirmPasswordMessage.style.color = 'red';    } else {        confirmPasswordMessage.textContent = '';    }});document.addEventListener("DOMContentLoaded", function () {    const registerButton = document.getElementById('register-submit');    const checkUsernameButton = document.getElementById('check-username-btn');    const usernameInput = document.getElementById('register-id');    const passwordInput = document.getElementById('register-password');    const confirmPasswordInput = document.getElementById('register-confirm-password');    const nameInput = document.getElementById('register-name');    const usernameMessage = document.getElementById('username-message');    // 아이디와 비밀번호에서 한글 입력 방지 함수    function preventKoreanInput(event) {        const value = event.target.value;        if (/[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/.test(value)) {            event.target.value = value.replace(/[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/g, '');        }    }    // 한글 입력 방지 이벤트 리스너 추가    usernameInput.addEventListener('input', preventKoreanInput);    passwordInput.addEventListener('input', preventKoreanInput);    confirmPasswordInput.addEventListener('input', preventKoreanInput);    // 아이디 중복 확인 버튼 클릭 시    window.checkUsername = function () {        const username = usernameInput.value;        if (username.length > 0) {            // Ajax 요청을 사용하여 서버에 아이디 중복 여부 확인            fetch(`/login_page/check_username/?id=${username}`)                .then(response => response.json())                .then(data => {                    if (data.exists) {                        usernameMessage.textContent = '이미 존재하는 아이디입니다.';                        usernameMessage.style.color = 'red';                        // 입력란 비활성화                        passwordInput.disabled = true;                        confirmPasswordInput.disabled = true;                        nameInput.disabled = true;                        registerButton.disabled = true;                    } else {                        usernameMessage.textContent = '사용 가능한 아이디입니다.';                        usernameMessage.style.color = 'green';                        // 입력란 활성화                        passwordInput.disabled = false;                        confirmPasswordInput.disabled = false;                        nameInput.disabled = false;                        registerButton.disabled = false;                    }                })                .catch((error) => {                    console.error('Error:', error);                });        } else {            usernameMessage.textContent = '아이디를 입력해 주세요.';            usernameMessage.style.color = 'red';        }    };});