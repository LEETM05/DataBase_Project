// // 비밀번호 변경 토글
// function togglePasswordChange() {
//     const form = document.getElementById("password-change-form");
//     form.style.display = form.style.display === "none" ? "block" : "none";
// }
//
// // 현재 비밀번호 확인
// async function verifyCurrentPassword() {
//     const currentPassword = document.getElementById("current_password").value;
//     const errorField = document.getElementById("current-password-error");
//
//     const response = await fetch('/userinfo_edit/verify_password/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': getCSRFToken()
//         },
//         body: JSON.stringify({ current_password: currentPassword })
//     });
//
//     const result = await response.json();
//
//     if (result.success) {
//         document.getElementById("new-password-fields").style.display = "block";
//         errorField.textContent = '';
//     } else {
//         errorField.textContent = '현재 비밀번호가 올바르지 않습니다.';
//     }
// }
//
// // 비밀번호 일치 확인
// function validatePasswordMatch() {
//     const newPassword = document.getElementById("new_password").value;
//     const confirmPassword = document.getElementById("confirm_password").value;
//     const errorField = document.getElementById("password-match-error");
//
//     if (newPassword && confirmPassword && newPassword !== confirmPassword) {
//         errorField.textContent = '새 비밀번호가 일치하지 않습니다.';
//     } else {
//         errorField.textContent = '';
//     }
// }
//
// // CSRF 토큰 가져오기
// function getCSRFToken() {
//     const cookies = document.cookie.split(';');
//     for (let cookie of cookies) {
//         const [name, value] = cookie.trim().split('=');
//         if (name === 'csrftoken') {
//             return value;
//         }
//     }
//     return '';
// }

// 비밀번호 변경 토글
function togglePasswordChange() {
    const form = document.getElementById("password-change-form");
    form.style.display = form.style.display === "none" ? "block" : "none";
}

// 현재 비밀번호 확인
async function verifyCurrentPassword() {
    const currentPassword = document.getElementById("current_password").value;
    const errorField = document.getElementById("current-password-error");

    const response = await fetch('/userinfo_edit/verify_password/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({ current_password: currentPassword })
    });

    const result = await response.json();

    if (result.success) {
        document.getElementById("new-password-fields").style.display = "block";
        errorField.textContent = '';
    } else {
        errorField.textContent = '현재 비밀번호가 올바르지 않습니다.';
    }
}

// 비밀번호 일치 확인
function validatePasswordMatch() {
    const newPassword = document.getElementById("new_password").value;
    const confirmPassword = document.getElementById("confirm_password").value;
    const errorField = document.getElementById("password-match-error");

    if (newPassword && confirmPassword && newPassword !== confirmPassword) {
        errorField.textContent = '새 비밀번호가 일치하지 않습니다.';
    } else {
        errorField.textContent = '';
    }
}