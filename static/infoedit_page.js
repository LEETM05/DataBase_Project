document.getElementById("password-form").addEventListener("submit", function(event) {
  const newPassword = document.getElementById("new_password").value;
  const confirmPassword = document.getElementById("confirm_password").value;

  // 비밀번호 유효성 검사 패턴
  const passwordPattern = /^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;

  // 유효성 검사
  if (!passwordPattern.test(newPassword)) {
    alert("비밀번호는 영어, 숫자, 특수문자를 포함해야 하며, 최소 8자 이상이어야 합니다.");
    event.preventDefault();
    return;
  }

  // 비밀번호 일치 확인
  if (newPassword !== confirmPassword) {
    alert("비밀번호가 일치하지 않습니다.");
    event.preventDefault();
    return;
  }
});
