// function togglePasswordChange() {
//     const form = document.getElementById('password-change-form');
//     form.style.display = form.style.display === 'none' ? 'block' : 'none';
// }
//
// function validatePasswordMatch() {
//     const newPasswordInput = document.getElementById('new_password');
//     const confirmPasswordInput = document.getElementById('confirm_password');
//     const errorElement = document.getElementById('password-match-error');
//     if (newPasswordInput.value !== confirmPasswordInput.value) {
//         errorElement.textContent = '새 비밀번호가 일치하지 않습니다.';
//     } else {
//         errorElement.textContent = '';
//     }
// }
//
// function verifyCurrentPassword() {
//     const currentPasswordInput = document.getElementById('current_password');
//     const errorElement = document.getElementById('current-password-error');
//     const newPasswordFields = document.getElementById('new-password-fields');
//
//     if (currentPasswordInput.value.trim() === '') {
//         errorElement.textContent = '현재 비밀번호를 입력해주세요.';
//     } else {
//         // AJAX 요청
//         fetch("/userinfo_edit/", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/x-www-form-urlencoded",
//                 "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
//             },
//             body: `current_password=${currentPasswordInput.value}&action=verify_password`
//         })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.valid) {
//                     errorElement.textContent = '';
//                     newPasswordFields.style.display = 'block';
//                 } else {
//                     errorElement.textContent = '현재 비밀번호가 다릅니다.';
//                     newPasswordFields.style.display = 'none';
//                 }
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//                 errorElement.textContent = '비밀번호 확인 중 오류가 발생했습니다.';
//             });
//     }
// }
//
// // function verifyCurrentPassword() {
// //     const currentPasswordInput = document.getElementById('current_password');
// //     const errorElement = document.getElementById('current-password-error');
// //     const newPasswordFields = document.getElementById('new-password-fields');
// //
// //     if (currentPasswordInput.value.trim() === '') {
// //         errorElement.textContent = '현재 비밀번호를 입력해주세요.';
// //     } else {
// //         // Simulate an AJAX request to check current password
// //         // In a real application, you would need to implement a backend view for this validation
// //         const isValid = true; // Replace with actual validation result
// //
// //         if (isValid) {
// //             errorElement.textContent = '';
// //             newPasswordFields.style.display = 'block';
// //         } else {
// //             errorElement.textContent = '현재 비밀번호가 다릅니다.';
// //             newPasswordFields.style.display = 'none';
// //         }
// //     }
// // }

function togglePasswordChange() {
    const form = document.getElementById('password-change-form');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
}

function validatePasswordMatch() {
    const newPasswordInput = document.getElementById('new_password');
    const confirmPasswordInput = document.getElementById('confirm_password');
    const errorElement = document.getElementById('password-match-error');
    if (newPasswordInput.value !== confirmPasswordInput.value) {
        errorElement.textContent = '새 비밀번호가 일치하지 않습니다.';
    } else {
        errorElement.textContent = '';
    }
}

function verifyCurrentPassword() {
    const currentPasswordInput = document.getElementById('current_password');
    const errorElement = document.getElementById('current-password-error');
    const newPasswordFields = document.getElementById('new-password-fields');

    if (currentPasswordInput.value.trim() === '') {
        errorElement.textContent = '현재 비밀번호를 입력해주세요.';
    } else {
        // AJAX 요청
        fetch("/userinfo_edit/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: `current_password=${encodeURIComponent(currentPasswordInput.value)}&action=verify_password`
        })
            .then(response => response.json())
            .then(data => {
                if (data.valid) {
                    errorElement.textContent = '';
                    newPasswordFields.style.display = 'block';
                } else {
                    errorElement.textContent = '현재 비밀번호가 다릅니다.';
                    newPasswordFields.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                errorElement.textContent = '비밀번호 확인 중 오류가 발생했습니다.';
            });
    }
}
